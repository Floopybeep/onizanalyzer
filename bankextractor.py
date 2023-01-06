from binascii import b2a_hex
import logging
from more_itertools import peekable
import mpyq
from s2protocol import versions
from s2repdump.types import *
from s2repdump.bank import GameBankStorage


PROTO_VERSION_MAPPINGS = {
    # 4.12.X
    80188: 79998,
}

outpath = "C:/Users/USER/Downloads/replaybanks"


# https://github.com/Blizzard/s2protocol/blob/master/docs/tutorial_API.rst
# https://github.com/Talv/sc2-repdump

@resource
class S2Replay:
    proto_build: int
    protocol: __module__
    features: ProtoFeatures = ProtoFeatures()

    header: dict
    details: dict
    init_data: dict

    info: ReplayInfo
    participants: GameParticipantsList
    banks: List[GameBankMeta]

    def __init__(self, filename, strict=False):
        def read_archive_contents(name):
            content = self.archive.read_file(name)
            return content

        def must_read_archive_contents(name):
            content = read_archive_contents(name)
            return content

        self.archive = mpyq.MPQArchive(filename)

        content = self.archive.header['user_data_header']['content']
        self.header = versions.latest().decode_replay_header(content)

        self.proto_build = self.header['m_version']['m_baseBuild']
        logging.info('Protocol build %d' % (self.proto_build))

        self.features.user_id_driven = self.proto_build >= 24764
        self.features.working_slots = self.proto_build >= 24764

        self.features.tracker_present = self.proto_build >= 25604

        self.features.tracker_player_pid = self.proto_build >= 25604

        try:
            self.protocol = versions.build(self.proto_build)
        except ImportError as e:
            logging.warning('Unsupported protocol: (%s)' % (str(e)))

        # read files
        self.details = self.protocol.decode_replay_details(must_read_archive_contents('replay.details'))
        self.init_data = self.protocol.decode_replay_initdata(must_read_archive_contents('replay.initData'))
        self.gameevents = peekable(self.protocol.decode_replay_game_events(must_read_archive_contents('replay.game.events')))
        content = read_archive_contents('replay.message.events')
        self.messageevents = peekable(self.protocol.decode_replay_message_events(content) if content else None)
        content = read_archive_contents('replay.tracker.events')
        self.features.tracker_present = bool(content)
        self.trackerevents = peekable(self.protocol.decode_replay_tracker_events(content) if content else None)

        # setup
        self.info = setup_info(self)
        self.participants = setup_participants(self)
        self.banks = setup_banks(self)


def setup_info(s2rep: S2Replay):
    info = ReplayInfo()
    info.title = s2rep.details['m_title'].decode('utf8')
    info.client_version = '.'.join([
        str(s2rep.header['m_version']['m_major']),
        str(s2rep.header['m_version']['m_minor']),
        str(s2rep.header['m_version']['m_revision']),
        str(s2rep.header['m_version']['m_build']),
    ])
    info.region = None
    info.timestamp = int((s2rep.details['m_timeUTC'] / 10000000) - 11644473600)
    info.elapsed_game_loops = s2rep.header['m_elapsedGameLoops']

    info.map_info = MapInfo()
    info.map_info.cache_handles = [*map(
        # lambda x: '%s.%s' % (b2a_hex(x[16:]).decode(), x[0:4].decode('ascii')),
        lambda x: '%s' % (b2a_hex(x[16:]).decode()),
        s2rep.details['m_cacheHandles']
    )]
    info.map_info.author_handle = s2rep.init_data['m_syncLobbyState']['m_gameDescription']['m_mapAuthorName'].decode() or None
    if info.map_info.author_handle:
        info.region = int(info.map_info.author_handle[0])

    return info


def setup_participants(s2rep: S2Replay):
    plist = GameParticipantsList(s2rep.features)

    for key, dp_entry in enumerate(s2rep.details['m_playerList']):
        if dp_entry['m_control'] in [EPlayerControl.OPEN]: continue

        pinfo = GameParticipant()
        plist.append(pinfo)

        pinfo.idx = key + 1

        if dp_entry['m_control'] == EPlayerControl.HUMAN:
            if dp_entry['m_toon']['m_region']:
                pinfo.handle = '%d-S2-%d-%d' % (dp_entry['m_toon']['m_region'], dp_entry['m_toon']['m_realm'], dp_entry['m_toon']['m_id'])
            else:
                pinfo.handle = None
        pinfo.ctrl = EPlayerControl[dp_entry['m_control']]

        if dp_entry['m_name']:
            tmp = dp_entry['m_name'].decode('utf8').split('<sp/>')
            if len(tmp) > 1:
                pinfo.name = tmp[1]
                pinfo.clan = tmp[0].replace('&lt;', '<').replace('&gt;', '>')
            else:
                pinfo.name = tmp[0]

        mcol = dp_entry['m_color']
        pinfo.color = PlayerColor(mcol['m_r'], mcol['m_g'], mcol['m_b'], mcol['m_a'])

        if s2rep.features.working_slots:
            if dp_entry['m_workingSetSlotId'] is None:
                # entry without a "working" slot in the lobby might indicate:
                # - game recovered from replay - where particuplar player was either replaced or excluded
                # - game started without lobby (test document mode etc.)
                # - a referee or an observer ??
                # - player that dropped from the game before it has even started ??
                logging.warning('"%s" has no working slot assigned' % (pinfo.name))
                pinfo.uid = plist[-2].uid + 1 if len(plist) > 1 else 0
                continue

            for slot_index, sl_slot in enumerate(s2rep.init_data['m_syncLobbyState']['m_lobbyState']['m_slots']):
                if dp_entry['m_workingSetSlotId'] != sl_slot['m_workingSetSlotId']: continue

                pinfo.working_slot = slot_index
                pinfo.uid = sl_slot['m_userId']
                break
        else:
            next_slot = plist[-2].working_slot + 1 if len(plist) > 1 else 0
            sl_slot = s2rep.init_data['m_syncLobbyState']['m_lobbyState']['m_slots'][next_slot]
            pinfo.working_slot = next_slot
            pinfo.uid = sl_slot['m_userId']

        if dp_entry['m_observe'] == EObserve.NONE or not s2rep.features.working_slots:
            # attempt to determine the player_id
            # in newer protos we'll relay on `SPlayerSetupEvent` event from the tracker that will be fetched later
            pinfo.pid = pinfo.working_slot + 1

        if dp_entry['m_control'] == EPlayerControl.COMPUTER:
            assert pinfo.working_slot is not None

        if dp_entry['m_control'] == EPlayerControl.HUMAN:
            assert pinfo.uid is not None

    if s2rep.features.tracker_player_pid:
        while True:
            ev = s2rep.trackerevents.peek()
            if ev['_event'] != 'NNet.Replay.Tracker.SPlayerSetupEvent': break
            ev = next(s2rep.trackerevents)
            if ev['m_slotId'] is None: continue
            p = plist.get_player(slot_id=ev['m_slotId'])
            if p is None:
                logging.warning('Failed to match a slot_id of %d with a pid of %d' % (ev['m_slotId'], ev['m_playerId']))
                continue
            p.pid = ev['m_playerId']

    return plist


def setup_banks(s2rep: S2Replay) -> List[GameBankMeta]:
    BANK_EVENTS = [
        'NNet.Game.SBankFileEvent',
        'NNet.Game.SBankSectionEvent',
        'NNet.Game.SBankKeyEvent',
        'NNet.Game.SBankValueEvent',
        'NNet.Game.SBankSignatureEvent',
    ]

    banks = {}

    for x in s2rep.participants:
        if s2rep.features.user_id_driven:
            if x.uid is None: continue
            banks[x.uid] = []
        else:
            if x.pid is None: continue
            banks[x.pid] = []

    for ev in s2rep.gameevents:
        if ev['_event'] in BANK_EVENTS:
            puid = s2rep.features.puid_from_ev(ev)

            if ev['_event'] == 'NNet.Game.SBankFileEvent':
                player = s2rep.participants.get_player(puid)
                banks[puid].append(GameBankMeta(ev['m_name'].decode('ascii'), player))

            banks[puid][-1].append_event(ev)
        else:
            if ev['_gameloop'] > 0:
                break
            else:
                continue

    tmpl = []
    for x in banks.values():
        for y in x:
            tmpl.append(y)
    return tmpl


def extract_banks(path):
    s2rep = S2Replay(path)
    sections = {}

    #bank_rebuild
    sections['sc2banks'] = []

    for gbmeta in s2rep.banks:
        pname = '%s' % (gbmeta.player.name)
        if gbmeta.player.handle:
            pname += ' [%s]' % (gbmeta.player.handle)
        logging.info(f'Rebuilding "{gbmeta.name}.SC2Bank" for player {pname} ..')
        bank_store = GameBankStorage()
        bank_store.rebuild_from_meta(gbmeta)

        expected_signature = bank_store.signature()
        computed_signature = bank_store.compute_signature(s2rep.info.map_info.author_handle, gbmeta.player.handle)
        if expected_signature is not None and expected_signature != computed_signature:
            logging.warning(
                'Signature missmatch for player: %s bank: %s! expected: %s computed: %s',
                pname,
                bank_store.name,
                expected_signature,
                computed_signature
            )

        sections['sc2banks'].append({
            'uid': gbmeta.player.uid,
            'name': bank_store.name,
            'expected_signature': expected_signature,
            'computed_signature': computed_signature,
            'filename': bank_store.filename(s2rep.info.map_info.author_handle, gbmeta.player.handle),
            'content': bank_store.tostring(),
        })

        filename = bank_store.write_sc2bank(outpath, True, "{}".format(gbmeta.player.name))
        print(f'File saved at "{filename}"')


if __name__ == '__main__':
    reppath = "C:/Users/USER/PycharmProjects/onizanalyzer/replays/Oh No It's Zombies Arctic Map (249).SC2Replay"
    extract_banks(reppath)
import s2protocol
import mpyq
import datetime
from infodict import bankplayerdict, bankloaddict


class bankinfoextractionclass:
    def __init__(self, handle, pid):
        self.username = ""                      # needs update
        self.handle = handle
        self.signature = ""
        self.date = None                        # needs update
        self.pid = pid

        self.player_bankinfo = bankplayerdict.copy()
        self.load_bankinfo = bankloaddict.copy()

    def setplayerbankinfo(self, option):
        if option['m_name'].decode('utf-8') in bankplayerdict:
            self.player_bankinfo[option['m_name'].decode('utf-8')] = option['m_data'].decode('utf-8')

    def setloadbankinfo(self, option):
        if option['m_name'].decode('utf-8') in bankloaddict:
            self.load_bankinfo[option['m_name'].decode('utf-8')] = option['m_data'].decode('utf-8')


def timeconvert(timestamp, offset):
    return datetime.datetime.fromtimestamp((timestamp - 116444880000000000 + offset) // 10000000)


def bankinfoprocess(inputqueue, msgqueue, outputqueue):
    protocol = s2protocol.versions.build(88500)
    while True:
        replaypath = inputqueue.get()
        if replaypath is None:
            msgqueue.put(None)
            outputqueue.put(None)
            break
        # try:
        archive = mpyq.MPQArchive(replaypath)
        init_data = archive.read_file('replay.initdata')
        init_data = protocol.decode_replay_initdata(init_data)
        game_events = archive.read_file('replay.game.events')
        game_events = protocol.decode_replay_game_events(game_events)
        details = archive.read_file('replay.details')
        details = protocol.decode_replay_details(details)

        playerdict = setup_bank_players(init_data)
        extract_bank_events(game_events, playerdict)
        extract_replay_details(details, playerdict)

        # except Exception as errormessage:
        #     outputqueue.put(-1)
        #     msgqueue.put(f"Error occured while analzying\n{replaypath}\n")
        #     print(errormessage)
        print("Analysis Done")
        outputqueue.put([*playerdict.values()])


def setup_bank_players(init_data):
    """
    :param init_data:
    :return: dictionary of {pid : {handle : BIEclass}}
    """
    lobbystate = init_data['m_syncLobbyState']['m_lobbyState']
    playerdict = {}
    resultdict = {}

    for player in lobbystate['m_slots']:
        if player['m_userId'] is None: continue
        else:
            playerdict[player['m_toonHandle']] = bankinfoextractionclass(player['m_toonHandle'], player['m_userId'] + 1)

    for key in playerdict:
        player = playerdict[key]
        resultdict[player.pid] = {key: player}

    return resultdict


def extract_bank_events(game_events, playerdict):
    # resultdict = {}
    for event in game_events:
        if event['_gameloop'] > 0:
            break
        if event['_event'] == 'NNet.Game.SBankKeyEvent':
            # print(event['m_name'], event['_userid']['m_userId'])
            player = next(iter(playerdict[event['_userid']['m_userId'] + 1].values()))
            player.setplayerbankinfo(event)
            player.setloadbankinfo(event)
        elif event['_event'] == 'NNet.Game.SBankSignatureEvent':
            next(iter(playerdict[event['_userid']['m_userId'] + 1].values())).signature = calculate_signature(event['m_signature'])

    # for key in playerdict:
    #     resultdict.update(playerdict[key])
    #
    # return resultdict


def extract_replay_details(details, playerdict):
    counter = 1
    for obj in details['m_playerList']:
        objname = obj['m_name'].decode('utf-8')
        if objname == 'Security' or obj['m_workingSetSlotId'] == 7: break
        player = next(iter(playerdict[counter].values()))
        player.date = timeconvert(details['m_timeUTC'], details['m_timeLocalOffset'])
        objname = objname.split('<sp/>')[-1]
        player.username = objname
        counter += 1


def calculate_signature(numlist):
    resultlist = []
    for num in numlist:
        resultlist.append(format(num, 'x').upper())
    return ''.join(resultlist)


def append_bankinfo_data(handledict):
    bankclasslist = list(handledict.values())
    resultlist = []

    for bankclass in bankclasslist:
        data = {}

        data['Player Name'] = bankclass.username
        data['Handle'] = bankclass.handle
        data['Last Play Date'] = bankclass.date
        data['Human Rank'] = bankclass.player_bankinfo['HumanRank']
        data['Human Games'] = bankclass.player_bankinfo['GamesPlayedAsHuman']
        data['Human Wins'] = bankclass.player_bankinfo['HumanWinsNormal']
        data['# of Deaths'] = bankclass.player_bankinfo['NumberOfTimesCaptured']
        data['# of Saves'] = bankclass.player_bankinfo['HumansRescued']
        data['Zombies Killed'] = bankclass.player_bankinfo['ZombiesKilled']
        data['Turrets Built'] = bankclass.player_bankinfo['TurretsBuilt']
        data['Vespene Harvested'] = bankclass.player_bankinfo['VespeneHarvested']
        data['# of Diverts'] = bankclass.player_bankinfo['FuelDiverted']
        data['Zombie Rank'] = bankclass.player_bankinfo['ZombieRank']
        data['Zombie Games'] = bankclass.player_bankinfo['GamesPlayedAsZombie']
        data['Zombie Wins'] = bankclass.player_bankinfo['ZombieWins']
        data['Humans Captured'] = bankclass.player_bankinfo['HumansCaptured']
        data['# of Security Killed'] = bankclass.player_bankinfo['SecurityForcesKilled']

        resultlist.append(data)

    return resultlist

import mpyq

from fnvhash import fnv1a_32
from s2protocol import versions
from humanupgradecomplete import *


def winloss_to_victory(result):
    if result == 'Win':
        return True
    elif result == 'Loss':
        return False
    else:
        return None


def round(x):
    if x >= 0:
        return int(x+0.5)
    else:
        return int(x-0.5)


def extract_playerbanks(replay, humandict, zombieplayer):
    reppath = replay.filename
    game_events = extract_s2protocol_events(reppath)
    extract_bank_events(game_events, humandict, zombieplayer)
    set_player_ranks(humandict, zombieplayer)
    set_bank_date(replay, humandict, zombieplayer)
    extract_game_advantage_events(replay, humandict, zombieplayer)


def set_player_ranks(humandict, zplayer):
    for key in humandict:
        humandict[key].setrank()
    zplayer.setrank()


def set_bank_date(replay, humandict, zplayer):
    for key in humandict:
        humandict[key].bankinfo.date = replay.date
    zplayer.bankinfo.date = replay.date


def extract_s2protocol_events(reppath):
    archive = mpyq.MPQArchive(reppath)
    protocol = versions.build(88500)
    contents = archive.read_file('replay.game.events')
    game_events = protocol.decode_replay_game_events(contents)

    return game_events


def extract_bank_events(game_events, humandict, zombieplayer):
    for event in game_events:
        if event['_gameloop'] > 0:
            break
        if event['_event'] == 'NNet.Game.SBankKeyEvent':
            if (event['_userid']['m_userId'] + 1) == zombieplayer.pid:
                zombieplayer.bankinfo.setplayeropt(event)
                zombieplayer.bankinfo.setloadopt(event)
            else:
                humandict[event['_userid']['m_userId'] + 1].bankinfo.setplayeropt(event)
                humandict[event['_userid']['m_userId'] + 1].bankinfo.setloadopt(event)
        elif event['_event'] == 'NNet.Game.SBankSignatureEvent':
            if (event['_userid']['m_userId'] + 1) == zombieplayer.pid:
                zombieplayer.bankinfo.signature = calculate_signature(event['m_signature'])
            else:
                humandict[event['_userid']['m_userId'] + 1].bankinfo.signature = calculate_signature(event['m_signature'])


def calculate_signature(list):
    resultlist = []
    for decimal in list:
        resultlist.append(format(decimal, 'x').upper())
    return ''.join(resultlist)


def extract_game_advantage_events(replay, humandict, zplayer):
    calculate_game_id(humandict, zplayer)
    check = calculate_isprivate(replay, humandict, zplayer)
    if check and zplayer.bankinfo.load_bankinfo['Difficulty'] != '5':
        advantage = advantagedict[-1 * int(zplayer.bankinfo.load_bankinfo['Difficulty'])]
        for key in humandict:
            humandict[key].bankinfo.advantage = advantage
        zplayer.bankinfo.advantage = advantage
    # else:
    #     calculate_game_advantage(humandict, zplayer)


def calculate_game_id(humandict, zplayer):
    signaturelist = []
    for key in humandict:
        signaturelist.append(humandict[key].bankinfo.signature)

    signature = ''.join([sig for sig in signaturelist])
    gameid = fnv1a_32(signature.encode('utf-8'))

    for key in humandict:
        humandict[key].gameid = gameid
    zplayer.gameid = gameid


def calculate_isprivate(replay, humandict, zplayer):
    if replay.map_name == "Oh No It's Zombies Arctic Updated":
        if replay.is_private:
            set_info_to_private(humandict, zplayer, isbeforepatch=True)
            return True
    else:
        if zplayer.bankinfo.load_bankinfo['Difficulty'] != '5':
            set_info_to_private(humandict, zplayer)
            return True
    return False


def set_info_to_private(humandict, zplayer, isbeforepatch=False):
    for key in humandict:
        humandict[key].bankinfo.isprivate = True
        if isbeforepatch:
            humandict[key].bankinfo.isbeforepatch = True
    zplayer.bankinfo.isprivate = True
    if isbeforepatch:
        zplayer.bankinfo.isbeforepatch = True


def extract_playerinfo(replay):                                         # input: replay / output: list of h/z objects
    humandict, zombieplayer = {}, None

    for human in replay.humans:
        victory = winloss_to_victory(human.result)

        if human.play_race == 'Terran':
            humandict[human.pid] = marineinfo(name=human.name, pid=human.pid, handle=human.toon_handle, role='Human',
                                              victory=victory)
            humandict[human.pid].kills = len(human.killed_units)

        elif human.play_race == 'Zerg':
            zombieplayer = zombieinfo(name=human.name, pid=human.pid, handle=human.toon_handle, role='Zombie',
                                      victory=victory)
            z_player_hangar_kill_check(human.killed_units, zombieplayer)

    if zombieplayer is None:
        return [], None

    if victory is None:
        for human in replay.humans:
            if human.pid > 8: pass
            if human.play_race == 'Terran':
                for unit in human.units:
                    if dropship_player_check(unit):
                        humandict[human.pid].victory = True
                        zombieplayer.victory = False
                if humandict[human.pid].victory is None:
                    humandict[human.pid].victory = False
        if zombieplayer.victory is None:
            zombieplayer.victory = True

    return humandict, zombieplayer


def dropship_player_check(unit):
    if 188 <= unit.location[0] <= 211 and 212 <= unit.location[1] <= 255:
        return 1
    elif 212 <= unit.location[0] <= 235 and 212 <= unit.location[1] <= 255:
        return 2
    elif 236 <= unit.location[0] <= 256 and 212 <= unit.location[1] <= 255:
        return 3
    else:
        return 0


def z_player_hangar_kill_check(units, zombieplayer):
    for unit in units:
        # Alpha, Beta, Delta hangar
        if unit.location == (30, 55):
            zombieplayer.hangarcaptures[0] = True
        elif unit.location == (150, 225):
            zombieplayer.hangarcaptures[1] = True
        elif unit.location == (204, 40):
            zombieplayer.hangarcaptures[2] = True


def extract_eventinfo(replay, humandict, zombieplayer):
    examine_fixedrankplayers(humandict, zombieplayer)

    humanlist = []
    for key in humandict:
        humanlist.append(humandict[key].pid)
    humanset = set(humanlist)
    z_id = zombieplayer.pid

    for event in replay.events:
        if event.name in upgradeeventset:
            if event.name == 'UpgradeCompleteEvent':
                UpgradeCompleteEventCheck(event, humandict, humanset, zombieplayer)
            elif event.name == 'UnitTypeChangeEvent':
                UnitTypeChangeEventCheck(event, humandict, zombieplayer)
            elif event.name == 'UnitBornEvent':
                UnitBornEventCheck(event, humandict, zombieplayer)
            elif event.name == 'UnitInitEvent':
                UnitInitEventCheck(event, humandict, zombieplayer)
            elif event.name == 'PlayerStatsEvent':
                PlayerStatsEventCheck(event, zombieplayer, z_id)


def examine_fixedrankplayers(humandict, zplayer):
    for key in humandict:
        if humandict[key].handle in fixedrankplayerhandleset:
            set_fixedrankplayerrank(humandict[key])
    if zplayer.handle in fixedrankplayerhandleset:
        set_fixedrankplayerrank(zplayer)
    if zplayer.bankinfo.advantage is None:         # automatic advantage = calculate
        calculate_game_advantage(humandict, zplayer)


def calculate_game_advantage(humandict, zplayer):
    totalmarinerank = 0
    for key in humandict:
        totalmarinerank += float(humandict[key].bankinfo.player_bankinfo['HumanRank'])
    averagemarinerank = totalmarinerank / 6
    zombierank = float(zplayer.bankinfo.player_bankinfo['ZombieRank'])

    advantage = ((averagemarinerank - zombierank) / 7 + (averagemarinerank + zombierank - 31)) / 31

    for key in humandict:
        humandict[key].bankinfo.averagerank = averagemarinerank
        humandict[key].bankinfo.advantage = advantagedict[round(advantage)]
    zplayer.bankinfo.advantage = advantagedict[round(advantage)]
    zplayer.bankinfo.averagerank = averagemarinerank

    return advantagedict[round(advantage)]


def set_fixedrankplayerrank(player):
    player.rank = 16
    player.bankinfo.player_bankinfo['HumanRank'] = '31'
    player.bankinfo.player_bankinfo['ZombieRank'] = '31'


def UpgradeCompleteEventCheck(event, humandict, humanset, zombieplayer):
    name = event.upgrade_type_name
    z_id = zombieplayer.pid
    humanUCEcheck(event, name, humandict, humanset, zombieplayer)
    zombieUCEcheck(event, name, zombieplayer, z_id)


def UnitTypeChangeEventCheck(event, humandict, zombieplayer):                      # for t2 alphas (and structure changes maybe)
    name = event.unit_type_name

    if name == 'MassiveCocoon':
        # zombieplayer.cocoonsmade += 1
        zombieplayer.cocoonids.add(event.unit_id_index)
    elif name in t2alphadict and event.unit_id_index in zombieplayer.cocoonids:
        zombieplayer.t2alpha_create(name)
        zombieplayer.cocoonids.discard(event.unit_id_index)
        if event.unit.killed_by is not None and event.unit.killed_by.pid is not None and event.unit.killed_by.pid != zombieplayer.pid:
            humandict[event.unit.killed_by.pid].alphakills[t2alphadict[name]][1] += 1
            humandict[event.unit.killed_by.pid].alphakills[t2alphadict[name]][0] -= 1
        elif event.unit.killing_unit is not None and event.unit.killing_unit.name == 'AutoTurret':
            humandict[event.unit.killing_unit.owner.pid].alphakills[t2alphadict[name]][1] += 1
            humandict[event.unit.killing_unit.owner.pid].alphakills[t2alphadict[name]][0] -= 1


def UnitBornEventCheck(event, humandict, zombieplayer):                 # for drop pods, t1 cocoons, and t1 alphas
    name = event.unit_type_name

    if name == 'ZergDropPod':
        zombieplayer.droppodsused += 1
    elif name == 'MassiveCocoon' or name == 'RoyalCocoon':
        zombieplayer.cocoonsmade += 1
        if event.unit.killed_by is not None and event.unit.killed_by.pid is not None and event.unit.killed_by.pid != zombieplayer.pid:
            humandict[event.unit.killed_by.pid].cocoonkills += 1
        elif event.unit.killing_unit is not None and event.unit.killing_unit.name == 'AutoTurret':
            humandict[event.unit.killing_unit.owner.pid].cocoonkills += 1
    elif name in t1alphadict:
        zombieplayer.t1alpha_create(name)
        if zombieplayer.startingalpha is None:
            zombieplayer.startingalpha = t1alphatonamedict[name]
        if event.unit.killed_by is not None and event.unit.killed_by.pid is not None and event.unit.killed_by.pid != zombieplayer.pid:
            humandict[event.unit.killed_by.pid].alphakills[t1alphadict[name]][0] += 1
        elif event.unit.killing_unit is not None and event.unit.killing_unit.name == 'AutoTurret':
            humandict[event.unit.killing_unit.owner.pid].alphakills[t1alphadict[name]][0] += 1
    elif name == 'InfestedCocoon' and event.frame > 0 and event.control_pid < 8:
        zombieplayer.marinecaptures += 1
        humandict[event.control_pid].captures += 1
    elif name == 'QueenCoop':
        zombieplayer.t2alpha_create(name)
        if event.unit.killed_by is not None and event.unit.killed_by.pid is not None and event.unit.killed_by.pid != zombieplayer.pid:
            humandict[event.unit.killed_by.pid].alphakills[t2alphadict[name]][1] += 1
        elif event.unit.killing_unit is not None and event.unit.killing_unit.name == 'AutoTurret':
            humandict[event.unit.killing_unit.owner.pid].alphakills[t2alphadict[name]][1] += 1


def UnitInitEventCheck(event, humandict, zombieplayer):                         # for z structures
    name = event.unit_type_name

    if name in structurecountset:
        humandict[event.control_pid].add_structurecounter(name, event)
    elif name == 'ExplorationDroid':
        humandict[event.control_pid].explorationdroidsmade += 1
    elif name in zstructuredict:
        zombieplayer.structure_create(name)
        zombieplayer.structurebuilt += 1
        if event.unit.killed_by is not None and event.unit.killed_by.pid != zombieplayer.pid:
            humandict[event.unit.killed_by.pid].zstructurekills[zstructuredict[name]] += 1
        elif event.unit.killing_unit is not None and event.unit.killing_unit.name == 'AutoTurret':
            humandict[event.unit.killing_unit.owner.pid].zstructurekills[zstructuredict[name]] += 1
    elif name == 'GreaterNydusWorm':
        zombieplayer.greaternydustimings.append(event.second)


def PlayerStatsEventCheck(event, zombieplayer, z_id):
    if event.pid == z_id:
        zombieplayer.totalgasspent = event.resources_used_current
        zombieplayer.totalgasincome = event.resources_used_current + event.vespene_current

import sc2reader

from bankextractor import S2Replay
from playerclasses import *
from functions import *
from humanupgradecomplete import *


def extract_playerinfo(replay):                                         # input: replay / output: list of h/z objects
    humandict, zombieplayer = {}, None

    for human in replay.humans:
        if human.pid > 8: pass

        victory = winloss_to_victory(human.result)
        if human.play_race == 'Terran':
            humandict[human.pid] = marineinfo(name=human.name, pid=human.pid, handle=human.toon_handle, role='Human', victory=victory)
        elif human.play_race == 'Zerg':
            zombieplayer = zombieinfo(name=human.name, pid=human.pid, handle=human.toon_handle, role='Zombie', victory=victory)

    return humandict, zombieplayer


def detailed_victory_determine_z(player, zplayer):
    if player.result == 'Loss':
        zplayer.victory = False
    elif player.result == 'Win':
        zplayer.victory = True

    else:
        for unit in player.killed_units:
            # Alpha, Beta, Delta hangar
            if unit.location == (30, 55):                                   # add check for player in drop-ship later
                zplayer.hangarcaptures[0] = True
            elif unit.location == (150, 225):
                zplayer.hangarcaptures[1] = True
            elif unit.location == (204, 40):
                zplayer.hangarcaptures[2] = True

        if False not in zplayer.hangarcaptures:
            zplayer.victory = True
        else:
            zplayer.victory = False


def dropship_player_check(unit):
    if 188 <= unit.location[0] <= 211 and 212 <= unit.location[1] <= 255:
        return 1
    elif 212 <= unit.location[0] <= 235 and 212 <= unit.location[1] <= 255:
        return 2
    elif 236 <= unit.location[0] <= 256 and 212 <= unit.location[1] <= 255:
        return 3
    else:
        return False


def extract_eventinfo(replay, humandict, zombieplayer):
    humanlist = []
    for key in humandict:
        humanlist.append(humandict[key].pid)
    humanset = set(humanlist)

    for event in replay.events:
        if event.name == 'UpgradeCompleteEvent':
            UpgradeCompleteEventCheck(event, humandict, humanset, zombieplayer)
        elif event.name == 'UnitTypeChangeEvent':
            UnitTypeChangeEventCheck(event, zombieplayer)
        elif event.name == 'UnitBornEvent':
            UnitBornEventCheck(event, zombieplayer)
        elif event.name == 'UnitInitEvent':
            UnitInitEventCheck(event, humandict, humanset, zombieplayer)


    # extract the following information
    # 1. roomcaptures
    # 4. totalgasincome
    # 5. totalgasspent


def UpgradeCompleteEventCheck(event, humandict, humanset, zombieplayer):
    name = event.upgrade_type_name
    z_id = zombieplayer.pid
    humanUCEcheck(event, name, humandict, humanset, zombieplayer)
    zombieUCEcheck(event, name, zombieplayer, z_id)


def UnitTypeChangeEventCheck(event, zombieplayer):
    name = event.unit_type_name
    cocoonids = set()

    if name == 'MassiveCocoon':
        zombieplayer.cocoonsmade += 1
        cocoonids.add(event.unit_id_index)
    elif name in t2alphadict and event.unit_id_index in cocoonids:
        zombieplayer.t2alpha_create(name)
        cocoonids.discard(event.unit_id_index)


def UnitBornEventCheck(event, zombieplayer):
    name = event.unit_type_name

    if name == 'ZergDropPod':
        zombieplayer.droppodsused += 1
    elif name == 'MassiveCocoon':
        zombieplayer.cocoonsmade += 1
    elif name in t1alphadict:
        zombieplayer.t1alpha_create(name)
        if zombieplayer.startingalpha is None:
            zombieplayer.startingalpha = t1alphatonamedict[name]


def UnitInitEventCheck(event, humandict, humanset, zombieplayer):
    name = event.unit_type_name

    if name == 'ExplorationDroid':
        humandict[event.control_pid].explorationdroidsmade += 1
    elif name in zstructuredict:
        zombieplayer.structure_create(name)
        zombieplayer.structuresbuilt += 1
    elif name == 'GreaterNydusWorm':
        zombieplayer.greaternydustimings.append(event.second)

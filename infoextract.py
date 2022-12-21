import sc2reader

from bankextractor import S2Replay
from playerclasses import *
from functions import *
from humanupgradecomplete import humanUCEcheck


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
    print(1)
    for event in replay.events:
        if event == 'UpgradeCompleteEvent':
            UpgradeCompleteEventCheck(event, humandict, zombieplayer)


    # extract the following information
    # 1. roomcaptures
    # 2. majorroomcaptures              (Power, Fuel, Containment, Security, Gates)
    # 3. marinecaptures
    # 4. totalgasincome
    # 5. totalgasspent
    # 6. alphasbuilt                    ([Type][Tiers], Type = (Abom, Gene, Anub, Legion, Predator))
    # 7. starting alpha                 string
    # 8. strain_purchases               ([Strain][Tiers], Strains = (Speed, Health, Damage, Volatile))
    # 9. upgradepurchases               (# [Type][Tiers], Type = (Speed, Regen, Constructive, Virulent))
    # 10. structurebuilt                count

def event_blacklist_check(event):
    UnitBornEventblacklist = {'InfestedCivilianBurrowed'}
    UpgradeCompleteEventblacklist = {'RefineryRoomInfestedExcavationZone', 'RefineryRoomInfestedManufacturingSector',
                                'RefineryRoomInfestedProcessingFacilities', 'RefineryRoomInfestedScienceLabs',
                                'VirophageroominfestedAlpha', 'VirophageroominfestedBeta', 'VirophageroominfestedDelta'}

    if event.frame == 0:
        return False
    if event.name == 'UnitBornEvent' and event.unit_type_name in UnitBornEventblacklist:
        return False
    elif event.name == 'UpgradeCompleteEvent' and event.upgrade_type_name in UpgradeCompleteEventblacklist:
        return False

    return True


def UpgradeCompleteEventCheck(event, humandict, zombieplayer):
    name = event.upgrade_type
    humanUCEcheck(event, name, humandict)
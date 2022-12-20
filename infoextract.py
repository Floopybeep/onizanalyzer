import sc2reader

from bankextractor import S2Replay
from playerclasses import *


def extract_playerinfo(path):
    replay = S2Replay(path)


def extract_z_info(replay, player_object, quickanalyze):
    # create playerclass for zombie player
    zplayer = zombieinfo(name=player_object.name, pid=player_object.pid, handle=player_object.toon_handle, role='Z')

    if quickanalyze:
        quick_victory_determine_z(player_object, zplayer)
        quick_info_extraction_z(player_object, zplayer, replay)
    else:
        detailed_victory_determine_z(player_object, zplayer)
        detailed_info_extraction_z(player_object, zplayer, replay)

    return zplayer


def quick_victory_determine_z(player, zplayer):
    if player.result is None:
        zplayer.victory = None
    else:
        if player.result == 'Loss':
            zplayer.victory = False
        else:
            zplayer.victory = True


def quick_info_extraction_z(player, zplayer, replay):
    print(1)


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


def detailed_info_extraction_z(player, zplayer, replay):
    for event in replay.events:
        if event_blacklist_check(event) is True:



            print(1)


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

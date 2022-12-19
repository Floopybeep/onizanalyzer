import sc2reader

from bankextractor import S2Replay
from playerclasses import *


def extract_playerinfo(path):
    replay = S2Replay(path)


def extract_z_info(replay, player_class, quickanalyze):
    # create playerclass for zombie player
    zplayer = zombieinfo(name=player_class.name, pid=player_class.pid, handle=player_class.toon_handle, role='Z')

    if quickanalyze:
        quick_victory_determine_z(player_class, zplayer)
    else:
        detailed_victory_determine_z(player_class, zplayer)
        detailed_info_extraction_z(player_class, zplayer)

    return zplayer


def quick_victory_determine_z(player, zplayer):
    if player.result is None:
        zplayer.victory = None
    else:
        if player.result == 'Loss':
            zplayer.victory = False
        else:
            zplayer.victory = True


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
    if () < unit.location < ():
        return 1
    elif () < unit.location < ():
        return 2
    elif () < unit.location < ():
        return 3
    else:
        return False


def detailed_info_extraction_z(player, zplayer):
    print(1)
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

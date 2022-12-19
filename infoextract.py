import sc2reader

from bankextractor import S2Replay
from playerclasses import *


def extract_playerinfo(path):
    replay = S2Replay(path)


def extract_z_info(replay, player_class, quickanalyze):
    # create playerclass for zombie player
    zplayer = zombieinfo(name=player_class.name, pid=player_class.pid, handle=player_class.toon_handle, role='Z')

    if quickanalyze:
        quick_victory_determine(player_class, zplayer)
    else:
        detailed_victory_determine(player_class, zplayer)
        detailed_info_extraction_z(player_class, zplayer)

    return zplayer


def quick_victory_determine(player, zplayer):
    if player.result is None:
        zplayer.victory = None
    else:
        if player.result == 'Loss':
            zplayer.victory = False
        else:
            zplayer.victory = True


def detailed_victory_determine(player, zplayer):
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


def detailed_info_extraction_z(player, zplayer):
    print(1)
    # extract the following information
        # 1. number of rooms captured
        # 2. number of marines killed
        # 3. gas income
        # 4. gas spent
        # 5.
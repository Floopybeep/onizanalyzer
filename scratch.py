import s2protocol
import sc2reader
from s2protocol import versions
import mpyq
import time
from os import listdir, walk
from os.path import isfile, join

from playerclasses import *
from bankextractor import extract_banks

quickanalyze = False

folderpath = "C:/Users/wooil/Documents/StarCraft II/Accounts/12861615/1-S2-1-5777751/Replays/Multiplayer/Oh No It's Zombies/"
savepath = "C:/Users/wooil/Downloads/analysis.txt"

# The path for replays in the folder and subfolders are saved in replaypaths(list)
replaypaths = []

for path, subdirs, files in walk(folderpath):
    for name in files:
        if isfile(join(path, name)): replaypaths.append(join(path, name))

for replaypath in replaypaths:
    t0 = time.time()
    try:
        replay = sc2reader.load_replay(replaypath, load_level=3)
    except Exception:
        print("Replay corrupted, deleting replay: ", replaypath)
        pass

    playerlist = []

    # Declare players according to their race(M/Z)
    for player in replay.humans:
        # if player.play_race == 'Zerg':
        #     playerlist.append(zombieinfo(name=player.name, pid=player.pid, handle=player.toon_handle, role='Z'))
        #     # if not quickanalyze:
        #     if player.result == 'Loss':
        #         print("Z Loss")
        #         for k in range(len(replay.active_units)):
        #             try:
        #                 if replay.active_units[k].id == 34078721:
        #                     print("Alpha dropship location: ", replay.active_units[k].location)
        #                 elif replay.active_units[k].id == 33554433:
        #                     print("Beta dropship location: ", replay.active_units[k].location)
        #                 elif replay.active_units[k].id == 33816577:
        #                     print("Delta dropship location: ", replay.active_units[k].location)
        #             except Exception:
        #                 pass
        #
        #     elif player.result not in ['Win', 'Loss']:
        #         print("Result is None")
        #         try:
        #             replay = sc2reader.load_replay(replaypath, load_level=3)
        #         except Exception:
        #             print("Replay corrupted, deleting replay: ", replaypath)
        #             pass
        #         for player in replay.players:
        #             if player.play_race == 'Zerg' and player.pid != 8:
        #                 for unit in player.killed_units:
        #                     if unit.location == (30, 55): print("A hangar killed")
        #                     elif unit.location == (150, 225): print("B hangar killed")
        #                     elif unit.location == (204, 40): print("D hangar killed")
        #
        #                 for k in range(len(replay.active_units)):
        #                     try:
        #                         if replay.active_units[k].id == 34078721:
        #                             print("Alpha dropship location: ", replay.active_units[k].location)
        #                         elif replay.active_units[k].id == 33554433:
        #                             print("Beta dropship location: ", replay.active_units[k].location)
        #                         elif replay.active_units[k].id == 33816577:
        #                             print("Delta dropship location: ", replay.active_units[k].location)
        #                     except Exception:
        #                         pass

        if player.play_race == 'Terran' and player.result == 'Win':
            count = 0
            for unit in player.units:
                if 190 < unit.location[0] and 190 < unit.location[1]:
                    count += 1

            print("For player", player.name, ": ", count)
            if count == 0:
                count = 0

        else:
            playerlist.append(marineinfo(name=player.name, pid=player.pid, handle=player.toon_handle, role='M'))
            # if not quickanalyze:
    t1 = time.time()
    timetaken = t1 - t0
    print("Time taken for replay analysis: ", timetaken)

    # print(1)

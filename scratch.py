import s2protocol
import sc2reader
from s2protocol import versions
import mpyq
import time
from os import listdir, walk
from os.path import isfile, join

from playerclasses import *
from bankextractor import extract_banks
from infoextract import *

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
        if player.play_race == 'Zerg':
            zplayer = extract_z_info(replay, player, quickanalyze)
            playerlist.append(zplayer)

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

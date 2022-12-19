import s2protocol
import sc2reader
from s2protocol import versions
import mpyq
from os import listdir, walk
from os.path import isfile, join

from playerclasses import *
from bankextractor import extract_banks

folderpath = "C:/Users/wooil/Documents/StarCraft II/Accounts/12861615/1-S2-1-5777751/Replays/Multiplayer/Oh No It's Zombies/"
savepath = "C:/Users/wooil/Downloads/analysis.txt"

# The path for replays in the folder and subfolders are saved in replaypaths(list)
replaypaths = []

for path, subdirs, files in walk(folderpath):
    for name in files:
        if isfile(join(path, name)): replaypaths.append(join(path, name))

for replaypath in replaypaths:
    replay = sc2reader.load_replay(replaypath, load_level=2)

    # Currently, main development is being done in scratch.py
    # Once verified, code will be moved to main.py

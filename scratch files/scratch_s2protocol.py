import s2protocol
from s2protocol import versions
import mpyq
from os import listdir, walk
from os.path import isfile, join

from playerclasses import *
from bankextractor import extract_banks, S2Replay


folderpath = "C:/Users/wooil/Documents/StarCraft II/Accounts/12861615/1-S2-1-5777751/Replays/Multiplayer/Oh No It's Zombies/"
savepath = "C:/Users/wooil/Downloads/analysis.txt"

# The path for replays in the folder and subfolders are saved in replaypaths(list)
replaypaths = []

for path, subdirs, files in walk(folderpath):
    for name in files:
        if isfile(join(path, name)): replaypaths.append(join(path, name))

for replaypath in replaypaths:
    replay = S2Replay(replaypath)

    # Players will be stored in players(list) as playerinfo(classes)
    players = []
    gameevents = []

    for event in replay.trackerevents:
        if event['_event'] == 'NNet.Replay.Tracker.SUnitOwnerChangeEvent':
            gameevents.append(event)

    # person: GameParticipant
    for person in replay.participants:
        if person.name != "Security":
            print(person.name)
            players.append(playerinfo(person.name, person.pid))


    print('1')
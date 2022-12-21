import sc2reader
from functions import *
from playerclasses import *
from infoextract import *
import time


def mainprocess(replaypath, quickanalysis, format='text'):                  # take a replay file, convert to txt format
    t0 = time.time()
    replay_load_level = quickanalysis_to_loadlevel(quickanalysis)
    replay = sc2reader.load_replay(replaypath, load_level=replay_load_level)

    humandict, zombieplayer = extract_playerinfo(replay)

    if len(humandict) < 6:
        print("Incomplete Lobby Detected!")
        return False

    extract_eventinfo(replay, humandict, zombieplayer)
    t1 = time.time()
    print(t1-t0)


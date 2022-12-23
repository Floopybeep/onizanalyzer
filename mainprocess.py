from infoextract import extract_eventinfo, extract_playerinfo
from infocondense import condense_eventinfo
# import time
import sc2reader


def quickanalysis_to_loadlevel(quickanalysis):
    if quickanalysis:
        return 2
    else:
        return 3


def mainprocess(replaypath, textoutputpath, quickanalysis=False, format='text'):                  # take a replay file, convert to txt format
    # t0 = time.time()
    eventlist = []
    replay_load_level = quickanalysis_to_loadlevel(quickanalysis)
    try:
        replay = sc2reader.load_replay(replaypath, load_level=replay_load_level)
        humandict, zombieplayer = extract_playerinfo(replay)

        if len(humandict) < 6:
            print("Incomplete Lobby Detected!")
            return False

        extract_eventinfo(replay, humandict, zombieplayer)
        condense_eventinfo(replay, textoutputpath, humandict, zombieplayer)
        print("textfile successfully created!")

    except Exception:
        print("Error in loading replay!")
        pass

    # t1 = time.time()
    # print(t1-t0)

if __name__ == "__main__":
    replaypath = "C:/Users/USER/PycharmProjects/onizanalyzer/replays/Oh No It's Zombies Arctic Map (249).SC2Replay"

    # replay_load_level = quickanalysis_to_loadlevel(False)
    try:
        replay = sc2reader.load_replay(replaypath, load_level=3)
        humandict, zombieplayer = extract_playerinfo(replay)

        if len(humandict) < 6:
            print("Incomplete Lobby Detected!")
            pass

        extract_eventinfo(replay, humandict, zombieplayer)
        print("textfile successfully created!")
        print(1)

    except Exception:
        print("Error in loading replay!")
        pass
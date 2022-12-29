from infoextract import extract_eventinfo, extract_playerinfo, extract_playerbanks, dupcheck
from infocondense import condense_eventinfo
from infoappend import append_replayinfo
# import time
import sc2reader


def quickanalysis_to_loadlevel(quickanalysis):
    if quickanalysis:
        return 2
    else:
        return 3


def mainprocess(replaypath, textoutputpath, total_replay_data, quickanalysis=False, format='text'):                  # take a replay file, convert to txt format
    replay_load_level = quickanalysis_to_loadlevel(quickanalysis)

    # try:
    replay = sc2reader.load_replay(replaypath, load_level=replay_load_level)
    humandict, zombieplayer = extract_playerinfo(replay)

    if len(humandict) < 6:
        print("Incomplete/Leaver Lobby Detected!")
        return False

    extract_playerbanks(replay, humandict, zombieplayer)

    if dupcheck(humandict, replaypath, textoutputpath, total_replay_data):
        print("Duplicate Replay detected!")
        pass

    extract_eventinfo(replay, humandict, zombieplayer)
    condense_eventinfo(replay, textoutputpath, humandict, zombieplayer)
    output1, output2 = append_replayinfo(replay, humandict, zombieplayer, total_replay_data)
    print("textfile successfully created!")

    # except Exception:
    #     print("Error in loading replay!")
    #     print(Exception)
    #     pass

    return output1, output2


# if __name__ == "__main__":
#     # replaypath = "C:/Users/USER/PycharmProjects/onizanalyzer/replays/wonky replays/Oh_No_Its_Zombies_Arctic_Map_880.SC2Replay"
#     replaypath = "C:/Users/USER/PycharmProjects/onizanalyzer/replays/Oh No It's Zombies Arctic Map (245).SC2Replay"
#     outputpath = "C:/Users/USER/PycharmProjects/onizanalyzer/replays/text file output"
#
#     replay = sc2reader.load_replay(replaypath, load_level=3)
#     humandict, zombieplayer = extract_playerinfo(replay)
#
#     if len(humandict) < 6:
#         print("Incomplete Lobby Detected!")
#         pass
#
#     extract_playerbanks(replay, humandict, zombieplayer)
#     extract_eventinfo(replay, humandict, zombieplayer)
#     condense_eventinfo(replay, outputpath, humandict, zombieplayer)
#     print("textfile successfully created!")
#     print(1)
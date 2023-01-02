from infoextract import extract_eventinfo, extract_playerinfo, extract_playerbanks
from infocondense import condense_eventinfo
from infoappend import append_replayinfo
# import time
import sc2reader


def mainprocess(inputqueue, messagequeue, outputqueue):                  # take a replay file, convert to txt format
    print("Mainprocess Started!")
    qoutput = inputqueue.get()
    replaypath, textoutputpath, total_replay_data = qoutput[0], qoutput[1], qoutput[2]
    # replaypath, textoutputpath, total_replay_data = inputargs[0], inputargs[1], inputargs[2]

    try:
        replay = sc2reader.load_replay(replaypath, load_level=3)
        humandict, zombieplayer = extract_playerinfo(replay)

        if len(humandict) < 6:
            print("Incomplete/Leaver Lobby Detected!")
            messagequeue.put("Incomplete/Leaver Lobby Detected!\n")
            return False

        extract_playerbanks(replay, humandict, zombieplayer)

        # if dupcheck(humandict, replaypath, textoutputpath, total_replay_data):
        #     print("Duplicate Replay detected!")
        #     pass

        extract_eventinfo(replay, humandict, zombieplayer)
        condense_eventinfo(replay, textoutputpath, humandict, zombieplayer)
        output1, output2 = append_replayinfo(replay, humandict, zombieplayer, total_replay_data)
        print("textfile successfully created!")
        outputqueue.put("textfile successfully created!")

    except Exception:
        print("Error in loading replay!")
        print(Exception)
        return False

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
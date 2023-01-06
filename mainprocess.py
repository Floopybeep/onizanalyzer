from infoextract import extract_eventinfo, extract_playerinfo, extract_playerbanks
from infocondense import condense_eventinfo
from infoappend import append_replayinfo
import os
# import time
import sc2reader


def mainprocess(inputqueue, messagequeue, outputqueue):                  # take a replay file, convert to txt format
    """
    :param inputqueue: provides replay/text path
    :param messagequeue: used to display messages
    :param outputqueue: outputs (humandata(list), zdata) for analysis
    :return:
    """
    print("Mainprocess Started!")
    while True:
        input = inputqueue.get()
        if input is None:
            print("Analysis Complete!")
            messagequeue.put(None)
            outputqueue.put(None)
            break
        replaypath, textoutputpath = input[0], input[1]

        try:
            replay = sc2reader.load_replay(replaypath, load_level=3)
            humandict, zombieplayer = extract_playerinfo(replay)

            if len(humandict) < 6 or zombieplayer is None:
                print("Incomplete/Leaver Lobby Detected!")
                messagequeue.put(f"Incomplete/Leaver Lobby Detected!\n{os.path.basename(replaypath)}\n")
                outputqueue.put(-1)
                continue

            else:
                extract_playerbanks(replay, humandict, zombieplayer)

                extract_eventinfo(replay, humandict, zombieplayer)
                condense_eventinfo(replay, textoutputpath, humandict, zombieplayer)
                humandata, zombiedata = append_replayinfo(replay, humandict, zombieplayer)
                print("textfile successfully created!")
                messagequeue.put(f"Replay analyzed!\n{os.path.basename(replaypath)}\n")
            outputqueue.put((humandata, zombiedata))

        except Exception as errormessage:
            messagequeue.put(f"Error in loading {replaypath}\n")
            outputqueue.put(-1)
            print("Error in loading replay!")
            print(errormessage)




# if __name__ == "__main__":
#     # replaypath = "C:/Users/USER/PycharmProjects/onizanalyzer/replays/wonky replays/Oh_No_Its_Zombies_Arctic_Map_874.SC2Replay"
#     replaypath = "C:/Users/USER/PycharmProjects/onizanalyzer/replays/Oh No It's Zombies Arctic Map (270).SC2Replay"
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
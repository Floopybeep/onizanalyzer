import multiprocessing

from os import listdir, walk
from os.path import join, isfile
from mainprocess import mainprocess


def splitlist(list, n):
    len_list = len(list)
    len_sublist = len_list//n
    result = []
    count = 0
    for i in range(n-1):
        result.append(list[count:count+len_sublist])
        count += len_sublist
    result.append(list[count:])
    return result


def replay_file_parser(folderpath):
    filepaths = []
    count = 0
    for path, subdirs, files in walk(folderpath):
        for name in files:
            extension = name[-9:]
            if isfile(join(path, name)) and extension == 'SC2Replay':
                filepaths.append(join(path, name))
                count += 1

    return filepaths, count


def separate_replays_analysis(repl_list):
    print("analysis started!")
    for rep in repl_list:
        mainprocess(rep)


def separate_replaypool(repl_list, num_of_proc):
    pool = multiprocessing.Pool(num_of_proc)
    pool.map(mainprocess, repl_list)


# def initiate_multiprocessing()


class mainfunctionclass:
    def __init__(self):
        self.replayfolderpath = ""
        self.textfolderpath = ""
        self.replayfilepaths = []
        self.replaycount = 0
        self.quickanalysis = False
        self.quickcheck = "mainclass load complete!"

        self.numberofprocesses = 3

    # Depreciated in favor of GUI-local functions (no real reason, these still work)
    def get_replays_from_folder(self):
        self.replayfilepaths, self.replaycount = replay_file_parser(self.replayfolderpath)

    # Depreciated in favor of local functions (they cause multiple instances of GUI to pop up)
    def send_replays_to_self(self):
        if len(self.replayfilepaths) > 1:
            # self.replaypool_loop(self.replayfilepaths)
            separate_replaypool(self.replayfilepaths, self.numberofprocesses)
        else:
            print("No replays detected!")
            pass

    def analyze_replays(self, replaypaths):          # pass multiple analyze_replays w different lists to replayque_loop
        print("analysis started!")
        for replaypath in replaypaths:
            mainprocess(replaypath, self.quickanalysis)

    def replaypool_loop(self, list_of_replays):
        pool = multiprocessing.Pool(self.numberofprocesses)
        pool.map(separate_replays_analysis, list_of_replays)

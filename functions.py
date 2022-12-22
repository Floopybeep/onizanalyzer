from os import listdir, walk
from os.path import join, isfile
from mainprocess import mainprocess


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


def quickanalysis_to_loadlevel(quickanalysis):
    if quickanalysis:
        return 2
    else:
        return 3


class mainfunctionclass:
    def __init__(self):
        self.replayfolderpath = ""
        self.textfolderpath = ""
        self.replayfilepaths = []
        self.replaycount = 0
        self.quickanalysis = False
        self.quickcheck = "mainclass load complete!"

    def get_replays_from_folder(self):
        self.replayfilepaths, self.replaycount = replay_file_parser(self.replayfolderpath)

    def analyze_replays(self, list_of_replaypaths):
        for replaypath in list_of_replaypaths:
            mainprocess(replaypath, self.quickanalysis)

    def send_replays_to_self(self):
        if len(self.replayfilepaths) > 1:
            self.analyze_replays(self.replayfilepaths)

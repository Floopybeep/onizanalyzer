from os import listdir, walk
from os.path import join, isfile


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


def winloss_to_victory(result):
    if result == 'Win':
        return True
    elif result == 'Loss':
        return False
    else:
        return None


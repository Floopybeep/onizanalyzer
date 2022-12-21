import sc2reader

from playerclasses import *
from bankextractor import extract_banks
from functions import *
from mainprocess import mainprocess

folderpath = "C:/Users/USER/PycharmProjects/onizanalyzer/replays"
savepath = "C:/Users/wooil/Downloads/analysis.txt"
replaypaths, replaycount = replay_file_parser(folderpath)     # replaypaths: list of replay paths / replaycount : number of replays

quickanalysis = False


for replaypath in replaypaths:
    mainprocess(replaypath, quickanalysis)

import multiprocessing
from functions import maininfoclass
from guifunctions import NewClass


if __name__ == '__main__':
    multiprocessing.freeze_support()
    mainclass = maininfoclass()
    mainclass.numberofprocesses = multiprocessing.cpu_count() - 1
    NC = NewClass(mainclass)
#     replaypath = "C:/Users/wooil/Documents/StarCraft II/Accounts/12861615/1-S2-1-5777751/Replays/Multiplayer/Oh No It's Zombies"
#     textfilepath = "C:/Users/wooil/Documents/StarCraft II/Accounts/12861615/1-S2-1-5777751/Replays/Multiplayer/Oh No It's Zombies/textfile"
#
#     mainclass.replayfolderpath = replaypath
#     mainclass.textfolderpath = textfilepath
#     mainclass.get_replays_from_folder()
#     mainclass.send_replays_to_self()



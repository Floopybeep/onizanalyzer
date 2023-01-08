import multiprocessing
from functions import maininfoclass
from guifunctions import GUIstart


if __name__ == '__main__':
    multiprocessing.freeze_support()
    multiprocessing.set_start_method("spawn")
    mainclass = maininfoclass()
    mainclass.numberofprocesses = multiprocessing.cpu_count() - 1
    # mainclass.numberofprocesses = 3
    mainclass.version = "1.0.10"
    GUIstart(mainclass)

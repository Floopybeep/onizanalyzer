import multiprocessing
from functions import maininfoclass
from guifunctions import NewClass


if __name__ == '__main__':
    multiprocessing.freeze_support()
    multiprocessing.set_start_method("spawn")
    mainclass = maininfoclass()
    mainclass.numberofprocesses = multiprocessing.cpu_count()
    # mainclass.numberofprocesses = 3
    mainclass.version = "1.0.4"
    NC = NewClass(mainclass)

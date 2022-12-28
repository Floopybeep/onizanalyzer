import multiprocessing
from functions import maininfoclass
from guifunctions import NewClass


if __name__ == '__main__':
    multiprocessing.freeze_support()
    mainclass = maininfoclass()
    mainclass.numberofprocesses = multiprocessing.cpu_count() - 1
    mainclass.version = "1.0.3"
    NC = NewClass(mainclass)



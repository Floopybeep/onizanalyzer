import multiprocessing
from functions import maininfoclass
from guifunctions import NewClass


if __name__ == '__main__':
    multiprocessing.freeze_support()
    mainclass = maininfoclass()
    mainclass.numberofprocesses = multiprocessing.cpu_count() - 1
    NC = NewClass(mainclass)



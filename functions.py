import multiprocessing

from os import listdir, walk
from os.path import join, isfile
from mainprocess import mainprocess


def splitlist(list, n):
    len_list = len(list)
    if len_list == 1: return list
    len_sublist = len_list//n + 1
    result = []
    count = 0
    for i in range(n-1):
        result.append(list[count:count+len_sublist])
        count += len_sublist
        if count > len_list:
            break
    if count < len(list):
        result.append([list[count:]])
    return result


def rep_txt_wrapper(replist, txtout):
    result = []
    for rep in replist:
        result.append(tuple((rep, txtout)))
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


def separate_replays_analysis(repl_list, textoutputpath):
    for rep in repl_list:
        mainprocess(rep, textoutputpath)


def separate_replaypool(repl_list, textoutputpath, num_of_proc):
    # inputlist = rep_txt_wrapper(repl_list, textoutputpath)
    # pool = multiprocessing.Pool(num_of_proc)
    # pool.starmap(mainprocess, inputlist)
    # processlist = []
    sublist = splitlist(repl_list, num_of_proc)
    multiprocessing.set_start_method("spawn")
    if num_of_proc != len(sublist):
        print("Sublist length: ", len(sublist))
        print("Number of Processors: ", num_of_proc)

    for i in range(num_of_proc):
        p = multiprocessing.Process(target=separate_replays_analysis, args=(sublist[i], textoutputpath))
        p.start()

    #     processlist.append(p)
    # for i, p in enumerate(processlist):
    #     if i == 0:
    #         p.start()
    #     else:
    #         p.join()

# def check_analyzer_status(p):
#     if p.is_alive(): # Then the process is still running
#         label.config(text = "MP Running")
#         mp_button.config(state = "disabled")
#         not_mp_button.config(state = "disabled")
#         root.after(200, lambda p=p: check_status(p)) # After 200 ms, it will check the status again.
#     else:
#         label.config(text = "MP Not Running")
#         mp_button.config(state = "normal")
#         not_mp_button.config(state = "normal")
#     return


class maininfoclass:
    def __init__(self):
        self.replayfolderpath = ""
        self.textfolderpath = ""
        self.replayfilepaths = []
        self.replaycount = 0
        self.quickanalysis = False
        self.quickcheck = "mainclass load complete!"
        self.version = ""

        self.numberofprocesses = 3

    # Depreciated in favor of GUI-local functions (no real reason, these still work)
    def get_replays_from_folder(self):
        self.replayfilepaths, self.replaycount = replay_file_parser(self.replayfolderpath)

    # Depreciated in favor of local functions (they cause multiple instances of GUI to pop up)
    # def send_replays_to_self(self):
    #     if len(self.replayfilepaths) > 1:
    #         # self.replaypool_loop(self.replayfilepaths)
    #         separate_replaypool(self.replayfilepaths, self.numberofprocesses)
    #     else:
    #         print("No replays detected!")
    #         pass
    #
    # def analyze_replays(self, replaypaths):          # pass multiple analyze_replays w different lists to replayque_loop
    #     print("analysis started!")
    #     for replaypath in replaypaths:
    #         mainprocess(replaypath, self.quickanalysis)
    #
    # def replaypool_loop(self, list_of_replays):
    #     pool = multiprocessing.Pool(self.numberofprocesses)
    #     pool.map(separate_replays_analysis, list_of_replays)



# https://docs.python.org/3/library/multiprocessing.html
# https://towardsdatascience.com/multiprocessing-in-python-9d498b1029ca
# https://superfastpython.com/multiprocessing-in-python/#How_to_Run_a_Function_In_a_Process

# https://superfastpython.com/multiprocessing-semaphore-in-python/
# check out the above if data leak happens

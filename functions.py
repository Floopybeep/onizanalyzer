import multiprocessing
import threading
import pandas as pd
import mpyq
import time
import os

from os import walk
from os.path import join, isfile
from s2protocol import versions
from mainprocess import mainprocess
from bankinfoprocess import bankinfoprocess, append_bankinfo_data
from infodict import total_df_human_column_list, total_df_zombie_column_list


# pd.set_option('display.max_colwidth', None)
# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)
# pd.set_option('display.width', 2000)
# pd.set_option("expand_frame_repr", True)

global protocol
protocol = versions.build(88500)


def splitlist(list, n):
    len_list = len(list)
    len_sublist = len_list//n + 1
    result = []
    count = 0
    len_list, result, count = len(list), [], 0

    if len_list == 1: return list
    if len_list % n:
        len_sublist = len_list//n + 1
    else:
        len_sublist = len_list//n

    for i in range(n-1):
        result.append(list[count:count+len_sublist])
        count += len_sublist
        if count > len_list:
            break
    if count < len(list):
        result.append([list[count:]])
    return result


def get_col_widths(dataframe):
    idx_max = max([len(str(s)) for s in dataframe.index.values] + [len(str(dataframe.index.name))])
    return [idx_max] + [max([len(str(s)) for s in dataframe[col].values] + [len(col)]) for col in dataframe.columns]


def numtobool(num):
    if num == 0:
        return False
    elif num == 1:
        return True
    else:
        return None


def rep_txt_wrapper(replist, txtout):
    result = []
    for rep in replist:
        result.append((rep, txtout))
    return result


def replay_file_parser(folderpath):
    filepaths = []
    count = 0
    for path, subdirs, files in walk(folderpath):
        for name in files:
            extension = name[-9:]
            mapname = name[:10]
            if isfile(join(path, name)) and extension == 'SC2Replay' and \
                    (mapname == "Oh No It's" or mapname == "Oh_No_Its_"):
                filepaths.append(join(path, name))
                count += 1

    return filepaths, count


class replay_bank_analysis_class:
    def __init__(self, repl_list, outpath, num_proc, pbar, scrolltext, remainingtimelabel):
        self.replay_list = repl_list
        self.outpath = outpath
        self.num_process = num_proc
        self.outputlist = []

        self.pbar = pbar
        self.scrolltext = scrolltext
        self.remainingtimelabel = remainingtimelabel

    def mainprocess(self):
        self.scrolltext.insert(index="1.0", chars="Bankfile Accumulation Started!\n\n")
        self.pbar.configure(maximum=len(self.replay_list))
        self.num_process_update(self.num_process, len(self.replay_list))

        manager = multiprocessing.Manager()
        inputqueue, msgqueue, outputqueue = manager.Queue(), manager.Queue(), manager.Queue()

        self.input_queue_fill(inputqueue, self.replay_list)

        messagereader = threading.Thread(target=self.update_scrolltext, args=(msgqueue,))
        pbarupdater = threading.Thread(target=self.update_pbar, args=(outputqueue,))
        timeupdater = threading.Thread(target=self.update_remainingtime, args=(inputqueue,))

        for _ in range(self.num_process):
            p = multiprocessing.Process(target=bankinfoprocess, args=(inputqueue, msgqueue, outputqueue,))
            p.start()

        messagereader.start()
        pbarupdater.start()
        timeupdater.start()

        messagereader.join()
        pbarupdater.join()
        timeupdater.join()

        total_data = self.data_update(self.outputlist)
        self.data_analysis(total_data)
        self.scrolltext.insert(index="1.0", chars="Bank Accumulation Finished!\n")

    def num_process_update(self, processor_number, replay_num):
        if processor_number > replay_num:
            self.num_process = replay_num

    def input_queue_fill(self, inputqueue, replay_list):
        for item in replay_list:
            inputqueue.put(item)
        for _ in range(self.num_process):
            inputqueue.put(None)

    def update_pbar(self, outputqueue):
        counter = 0
        while True:
            output = outputqueue.get()
            if output is None:
                counter += 1
                if counter == self.num_process:
                    break
            else:
                if output != -1:
                    self.outputlist.append(output)
                self.pbar.step(1)

    def update_scrolltext(self, msgqueue):
        counter = 0
        while True:
            message = msgqueue.get()
            if message is None:
                counter += 1
                if counter == self.num_process:
                    break
            else:
                self.scrolltext.insert(index="1.0", chars=message)

    def update_remainingtime(self, outputqueue):
        while True:
            remainingtime = outputqueue.qsize() * 4 / self.num_process
            if outputqueue.qsize() == 0:
                break
            self.remainingtimelabel.config(text=f"{int(remainingtime)} seconds")
            time.sleep(1)

    def data_update(self, dictlist):
        total_data = {}
        for replay in dictlist:
            for player in replay:
                handle = next(iter(player))
                if handle in total_data:
                    prevvalue = total_data[handle].date
                    currentvalue = player[handle].date
                    if prevvalue < currentvalue:
                        total_data[handle] = player[handle]
                else:
                    total_data.update(player)
        return total_data

    def data_analysis(self, datadict):
        datalist = append_bankinfo_data(datadict)
        dataframe_human = pd.DataFrame.from_records(datalist)
        writer = pd.ExcelWriter(f'{self.outpath}/#Bankdata.xlsx', engine='xlsxwriter')
        dataframe_human.to_excel(writer, sheet_name='Bank Data', startrow=1, header=False, index=False)
        worksheet = writer.sheets['Bank Data']

        (max_row, max_col) = dataframe_human.shape
        column_settings = [{'header': column} for column in dataframe_human.columns]

        worksheet.add_table(0, 0, max_row, max_col - 1, {'columns': column_settings})
        for i, width in enumerate(get_col_widths(dataframe_human)):
            worksheet.set_column(i-1, i, width+2)
        writer.close()


class replay_analysis_replaypool:
    def __init__(self, repl_list, textoutpath, num_proc, pbar, scrolltext, remainingtimelabel):
        self.replay_list = repl_list
        self.textoutpath = textoutpath
        self.num_process = num_proc
        self.replaydataclass = totalreplaydataclass()
        self.inputlist = []
        self.outputlist = []

        self.pbar = pbar
        self.scrolltext = scrolltext
        self.remainingtimelabel = remainingtimelabel

    def replaypool_analysis(self):
        self.scrolltext.insert(index="1.0", chars="Replay Analysis Started!\n\n")
        self.pbar.configure(maximum=len(self.replay_list))
        self.inputlist = rep_txt_wrapper(self.replay_list, self.textoutpath)
        self.num_process_update(self.num_process, len(self.inputlist))

        # Create queues
        manager = multiprocessing.Manager()
        inputqueue, messagequeue, outputqueue = manager.Queue(), manager.Queue(), manager.Queue()
        # inputqueue = manager.Queue()
        # outputqueue = manager.Queue()
        # messagequeue = manager.Queue()

        # Input replays to Queue
        self.input_que_fill(inputqueue, self.inputlist)

        # Define message reader & progressbar updater
        # messagereader = multiprocessing.Process(target=self.update_scrolltext, args=(messagequeue,))
        messagereader = threading.Thread(target=self.update_scrolltext, args=(messagequeue,))
        # pbarupdater = multiprocessing.Process(target=self.update_pbar, args=(outputqueue,))
        pbarupdater = threading.Thread(target=self.update_pbar, args=(outputqueue,))
        timeupdater = threading.Thread(target=self.update_remainingtime, args=(inputqueue,))

        # Define replay analyzer and execute all processes
        for _ in range(self.num_process):
            p = multiprocessing.Process(target=mainprocess, args=(inputqueue, messagequeue, outputqueue,))
            p.start()

        # pool = multiprocessing.Pool(self.num_process, mainprocess, (inputqueue, messagequeue, outputqueue,))             # pickle issues
        # pool.imap(mainprocess, (inputqueue, messagequeue, outputqueue,))

        messagereader.start()
        pbarupdater.start()
        timeupdater.start()
        messagereader.join()
        pbarupdater.join()
        timeupdater.join()

        # Compile and send output data for analysis
        self.analyze_data(self.outputlist)
        self.scrolltext.insert(index="1.0", chars="Excel File Created!\n")
        self.scrolltext.insert(index="1.0", chars="Analysis Finished!\n")
        print("Task Finished!")

    def num_process_update(self, processor_number, replay_num):
        if processor_number > replay_num:
            self.num_process = replay_num

    def input_que_fill(self, queue, list):
        for item in list:
            queue.put(item)
        for _ in range(self.num_process):
            queue.put(None)

    def update_pbar(self, queue):
        counter = 0
        while True:
            output = queue.get()
            if output is None:
                counter += 1
                if counter == self.num_process:
                    # self.pbar.step(1)
                    break
            else:
                if output != -1:
                    self.outputlist.append(output)
                self.pbar.step(1)

    def update_scrolltext(self, queue):
        counter = 0
        while True:
            message = queue.get()
            if message is None:
                counter += 1
                if counter == self.num_process:
                    break
            else:
                self.scrolltext.insert(index="1.0", chars=message)

    def update_remainingtime(self, queue):
        while True:
            remainingtime = queue.qsize() * 4 / self.num_process
            if queue.qsize() == 0:
                break
            self.remainingtimelabel.config(text=f"{int(remainingtime)} seconds")
            time.sleep(1)

    # def execute_mainprocess(self, queues):
    #     inputqueue, outputqueue, messagequeue = queues[0], queues[1], queues[2]
    #     while True:
    #         input = inputqueue.get()
    #         if input is None:
    #             break
    #         humandata, zombiedata = mainprocess(input, outputqueue, messagequeue)
    #         self.outputlist.append((humandata, zombiedata))


    def analyze_data(self, data):
        print("data analysis started")
        for output in data:
            if output is not False:
                self.replaydataclass.appendtoself(output[0], output[1])

        self.replaydataclass.create_dataframes()
        self.replaydataclass.create_excel_file(self.textoutpath)
        print("Analysis finished")


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

def replay_duplicate_check(repl_list, textoutpath, num_of_proc, deldupes, scrolltext, pbar, remainingtimelabel):
    signatureset, duplicate_list = set(), []
    counter = len(duplicate_list)
    pbar.configure(maximum=len(repl_list))
    deldupes = numtobool(deldupes)
    repl_list.reverse()
    scrolltext.insert(index="1.0", chars="Duplicate check started!\n")
    open(f"{textoutpath}/#DuplicateReplays.txt", 'w').close()


    # ts = time.time()

    pool = multiprocessing.Pool(processes=num_of_proc)
    output = pool.imap(extract_signatures, repl_list)                             # outputs tuple of (signature, path)

    with open(f"{textoutpath}/#DuplicateReplays.txt", 'a') as f:
        for out in output:
            pbar.step(1)
            remainingtimelabel.config(text=f"{int(counter/60)} seconds")
            if dupcheck(out[0], out[1], signatureset, f):
                if not deldupes:
                    duplicate_list.append(out[1])
                else:
                    os.remove(out[1])
    f.close()
    print(duplicate_list)
    if len(duplicate_list) > 0:
        if deldupes:
            scrolltext.insert(index="1.0", chars="Duplicate replays deleted!\n")
        else:
            scrolltext.insert(index="1.0", chars=f"Duplicate replays exported to \n{textoutpath}/#DuplicateReplays.txt!\n")
    else:
        scrolltext.insert(index="1.0", chars="No duplicates found!\n")

    # scrolltext.insert(index='1.0', chars=f"{time.time()-ts} seconds!\n")


def extract_signatures(reppath):
    signaturelist, result = [], ""
    archive = mpyq.MPQArchive(reppath)
    contents = archive.read_file('replay.game.events')
    game_events = protocol.decode_replay_game_events(contents)

    for event in game_events:
        if event['_gameloop'] > 1:
            break

        if event['_event'] == 'NNet.Game.SBankSignatureEvent':
            signature = calculate_signature(event['m_signature'])
            signaturelist.append(signature)

    for signature in signaturelist:
        result = f"{result}{signature}"

    return tuple([result, reppath])


def calculate_signature(list):
    resultlist = []
    for decimal in list:
        resultlist.append(format(decimal, 'x').upper())
    return ''.join(resultlist)


def dupcheck(signature, replaypath, signatureset, f):
    if signature not in signatureset:
        signatureset.add(signature)
        return False
    else:
        f.write(f"{replaypath}\n")
        return True


class totalreplaydataclass:
    def __init__(self):
        self.dataframe_human = None
        self.dataframe_zombie = None
        self.replays_data_human_list = []
        self.replays_data_zombie_list = []
        self.replaysignatures = set()
        self.duplicatereplaylist = []

    def appendtoself(self, hdata, zdata):
        self.replays_data_human_list.extend(hdata)
        self.replays_data_zombie_list.append(zdata)

    def create_dataframes(self):
        self.dataframe_human = pd.DataFrame.from_records(self.replays_data_human_list, columns=total_df_human_column_list)
        self.dataframe_zombie = pd.DataFrame.from_records(self.replays_data_zombie_list, columns=total_df_zombie_column_list)

    def create_excel_file(self, path):
        h_writer = pd.ExcelWriter(f'{path}/#Humandata.xlsx', engine='xlsxwriter')
        z_writer = pd.ExcelWriter(f'{path}/#Zombiedata.xlsx', engine='xlsxwriter')

        self.adjust_excel_data(h_writer, self.dataframe_human)
        self.adjust_excel_data(z_writer, self.dataframe_zombie)

    def adjust_excel_data(self, writer, df):
        df.to_excel(writer, sheet_name='Human Data', startrow=1, header=False, index=False)
        worksheet = writer.sheets['Human Data']

        (max_row, max_col) = df.shape
        column_settings = [{'header': column} for column in df.columns]

        worksheet.add_table(0, 0, max_row, max_col - 1, {'columns': column_settings})

        for i, width in enumerate(get_col_widths(df)):
            worksheet.set_column(i-1, i, width+2)

        writer.close()


# https://xlsxwriter.readthedocs.io/working_with_pandas.html
# https://stackoverflow.com/questions/52052184/how-to-use-xlsxwriter-add-table-method-with-a-dataframe
# https://xlsxwriter.readthedocs.io/example_pandas_table.html


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


# https://docs.python.org/3/library/multiprocessing.html
# https://towardsdatascience.com/multiprocessing-in-python-9d498b1029ca
# https://superfastpython.com/multiprocessing-in-python/#How_to_Run_a_Function_In_a_Process

# https://superfastpython.com/multiprocessing-semaphore-in-python/
# check out the above if data leak happens

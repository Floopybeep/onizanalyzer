import multiprocessing
import pandas as pd
import mpyq

import os
from os import listdir, walk
from os.path import join, isfile
from s2protocol import versions
from mainprocess import mainprocess
from infodict import total_df_human_column_list, total_df_zombie_column_list, \
    total_df_human_excel_column_list, total_df_zombie_excel_column_list


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

def rep_txt_wrapper(replist, txtout, obj):
    result = []
    for rep in replist:
        result.append((rep, txtout, obj))
    return result


def replay_file_parser(folderpath):
    filepaths = []
    count = 0
    for path, subdirs, files in walk(folderpath):
        for name in files:
            extension = name[-9:]
            mapname = name[:10]
            if isfile(join(path, name)) and extension == 'SC2Replay' and mapname == "Oh No It's":
                filepaths.append(join(path, name))
                count += 1

    return filepaths, count


def separate_replays_analysis(repl_list, textoutputpath, total_replay_data):
    for rep in repl_list:
        mainprocess(rep, textoutputpath, total_replay_data)


def separate_replaypool(repl_list, textoutputpath, num_of_proc, pbar, scrolltext):
    total_replay_data = totalreplaydataclass()
    pbar.configure(maximum=len(repl_list))
    inputlist = rep_txt_wrapper(repl_list, textoutputpath, total_replay_data)

    # Input replays to queue(rpaq - replay analysis queue)
    m = multiprocessing.Manager()
    inputqueue = m.Queue()
    p = multiprocessing.Process(target=fill_queue_with_replays, args=(inputqueue, inputlist))
    p.start()

    # mainprocess outputs to outputqueue(actual files) and messagequeue(errors and other msgs)
    messagequeue = m.Queue()
    outputqueue = m.Queue()

    # Define queue reading?
    pbarp = multiprocessing.Process(target=update_progressbar, args=(outputqueue, pbar))
    msgp = multiprocessing.Process(target=output_scrolltext, args=(messagequeue, scrolltext))

    # Define mainprocess pool and execute
    pool = multiprocessing.Pool(num_of_proc, mainprocess, (inputqueue, messagequeue, outputqueue,))
    output = pool.map(mainprocess, (inputqueue, messagequeue, outputqueue,))
    pbarp.start()
    msgp.start()
    # p = multiprocessing.Process(target=update_progressbar, args=[pbar, output])   # unpickable pbar
    # p.start()



    for out in output:
        if out is not False:
            total_replay_data.appendtoself(out[0], out[1])

    total_replay_data.create_dataframes()
    total_replay_data.create_excel_file(textoutputpath)

    print("All Processes Finished")


def fill_queue_with_replays(queue, list):
    for item in list:
        queue.put(item)
    for _ in range(multiprocessing.cpu_count() - 1):
        queue.put(None)


def update_progressbar(outputqueue, pbar):
    outputqueue.get()
    pbar.increment(1)


def output_scrolltext(msgqueue, scrolltext):
    while True:
        msg = msgqueue.get()
        scrolltext.insert(index="1.0", chars=msg)

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

def replay_duplicate_check(repl_list, textoutpath, num_of_proc, deldupes, pbar):
    signatureset, duplicate_list = set(), []
    deldupes = numtobool(deldupes)
    repl_list.reverse()
    open(f"{textoutpath}/#DuplicateReplays.txt", 'w').close()

    pool = multiprocessing.Pool(processes=num_of_proc)
    output = pool.imap(extract_signatures, repl_list)                             # outputs tuple of (signature, path)

    with open(f"{textoutpath}/#DuplicateReplays.txt", 'a') as f:
        for out in output:
            if dupcheck(out[0], out[1], signatureset, f):
                if not deldupes:
                    duplicate_list.append(out[1])
                else:
                    os.remove(out[1])
    f.close()
    print(duplicate_list)

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
        self.replays_data_human = None
        self.replays_data_zombie = None
        self.replays_data_human_list = []
        self.replaynum = 1
        self.replays_data_zombie_list = []
        self.replaysignatures = set()
        self.duplicatereplaylist = []

    def appendtoself(self, hdata, zdata):
        self.replays_data_human_list.extend(hdata)
        self.replays_data_zombie_list.append(zdata)

    def create_dataframes(self):
        self.replays_data_human = pd.DataFrame.from_records(self.replays_data_human_list, columns=total_df_human_column_list)
        self.replays_data_zombie = pd.DataFrame.from_records(self.replays_data_zombie_list, columns=total_df_zombie_column_list)

    def create_excel_file(self, path):
        h_writer = pd.ExcelWriter(f'{path}/#Humandata.xlsx', engine='xlsxwriter')
        z_writer = pd.ExcelWriter(f'{path}/#Zombiedata.xlsx', engine='xlsxwriter')

        self.adjust_excel_data(h_writer, self.replays_data_human)
        self.adjust_excel_data(z_writer, self.replays_data_zombie)

    def adjust_excel_data(self, writer, df):
        df.to_excel(writer, sheet_name='Sheet1', startrow=1, header=False, index=False)
        worksheet = writer.sheets['Sheet1']

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

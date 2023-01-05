import tkinter as tk
import tkinter.ttk as ttk
import threading
import multiprocessing
import os

from tkinter import scrolledtext
from tkinter import filedialog
from PIL import Image, ImageTk
from pathlib import Path
from functions import replay_file_parser, replay_analysis_replaypool, replay_duplicate_check

global mainclass_copy

class GUIstart:
    def __init__(self, mainclass):
        global mainclass_copy
        mainclass_copy = mainclass
        self.ui = onizGUI()
        self.ui.add_frame("frame1")

        self.ui.add_canvas("canvas", 1440, 810)
        # self.ui.register_image("canvas", "C:/Users/USER/PycharmProjects/onizanalyzer/410542.jpg")
        self.ui.register_image("canvas", "410542.jpg")
        # self.ui.register_image("canvas", str(Path(__file__).absolute())[:-16] + "410542.jpg")

        self.ui.add_button("startbutton", "canvas", 8, "Start")
        self.ui.add_button("closebutton", "canvas", 8, "Close")
        self.ui.add_button("dupcheckbutton", "canvas", 20, "Check Duplicate Replays")
        self.ui.add_button("repentrybutton", "canvas", 15, "Designate Path")
        self.ui.add_button("textentrybutton", "canvas", 15, "Designate Path")
        self.ui.add_button("savepathbutton", "canvas", 8, "Save Path")
        self.ui.add_button("loadpathbutton", "canvas", 8, "Load Path")
        self.ui.register_button("canvas", 1260, 748, "startbutton")
        self.ui.register_button("canvas", 1344, 748, "closebutton")
        self.ui.register_button("canvas", 1260, 708, "dupcheckbutton")
        self.ui.register_button("canvas", 1300, 48, "repentrybutton")
        self.ui.register_button("canvas", 1300, 98, "textentrybutton")
        self.ui.register_button("canvas", 1272, 138, "savepathbutton")
        self.ui.register_button("canvas", 1350, 138, "loadpathbutton")
        self.ui.register_function("closebutton", self.ui.window.destroy)
        self.ui.register_function("savepathbutton", self.ui.save_paths)
        self.ui.register_function("loadpathbutton", self.ui.load_paths)

        self.ui.add_checkbox("deletedupes", "Delete Duplicates?", "white", "black", "canvas")
        self.ui.register_checkbox("canvas", 1260, 678, "deletedupes")

        self.ui.add_progress_bar("replayprogressbar", 1200, 1200)
        self.ui.register_progress_bar("canvas", 30, 750, "replayprogressbar")

        self.ui.add_ttk_entry("replayfolderpathentry", 70)
        self.ui.add_ttk_entry("textfolderpathentry", 70)
        self.ui.register_ttk_entry("canvas", 800, 50, "replayfolderpathentry")
        self.ui.register_ttk_entry("canvas", 800, 100, "textfolderpathentry")
        self.ui.register_function("repentrybutton", self.ui.select_replay_folder)
        self.ui.register_function("textentrybutton", self.ui.select_text_output_folder)
        self.ui.register_function("startbutton", self.ui.press_start)
        self.ui.register_function("dupcheckbutton", self.ui.press_duplicate_replay_check)

        self.ui.add_scrolltext_window("outputscroll", 40, 70)
        self.ui.register_scrolltext_window("canvas", 30, 30, "outputscroll")

        self.ui.add_labels("remainingtimelabel", 60, "white", "black")
        self.ui.register_labels("canvas", 220, 724, "remainingtimelabel")

        self.ui.add_text_on_canvas("canvas", 800, 30, 300, "white", "ONIZ replay root folder path:")
        self.ui.add_text_on_canvas("canvas", 800, 80, 300, "white", "ONIZ replay text file output folder path:")
        self.ui.add_text_on_canvas("canvas", 30, 725, 500, "white", "Estimated time remaining: ")
        self.ui.add_text_on_canvas("canvas", 810, 130, 700, "white", "NOTE: You must change the font in Notepad to "
                                                                     "Consolas (otherwise unreadable!)")
        self.ui.add_text_on_canvas("canvas", 1350, 780, 200, "white", ''.join(['Version: ', mainclass_copy.version]))

        self.ui.start()


class onizGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.frames = {}
        self.buttons = {}
        self.checkboxes = {}
        self.canvases = {}
        self.images = {}
        self.progressbars = {}
        self.entries = {}
        self.functions = {}
        self.scrolltexts = {}
        self.labels = {}
        self.labeltextvariables = {}
        self.labelconfigs = {}
        self.variables = {}
        self.styles = {}

    def start(gui):
        class Threader(threading.Thread):
            def run(self):
                gui.window.mainloop()

        # class GUIinput(threading.Thread):
        #     def run(self):
        #         gui.inputqueue()

        Threader().run()
        # threading.Thread()

    def inputqueue(self):
        inputqueue = multiprocessing.Queue()

    def pbarupdate(self, increment):
        self.progressbars["replayprogressbar"].step(increment)

    def add_frame(self, name):
        tmp = ttk.Frame(self.window)
        tmp.pack()
        self.frames[name] = tmp

    def add_button(self, name, canvasname, width, text):
        tmp = ttk.Button(self.canvases[canvasname], width=width, text=text)
        self.buttons[name] = tmp

    def add_checkbox(self, name, text, fg, bg, canvasname):
        self.variables[name] = tk.IntVar()
        self.styles[name] = ttk.Style()
        self.styles[name].configure(f'{self.styles[name]}.TCheckbutton', foreground=fg, background=bg)
        tmp = ttk.Checkbutton(self.canvases[canvasname], text=text, style=f"{self.styles[name]}.TCheckbutton",
                              variable=self.variables[name])
        self.checkboxes[name] = tmp

    def register_button(self, canvasname, x, y, buttonname):
        self.canvases[canvasname].create_window(x, y, anchor=tk.NW, window=self.buttons[buttonname])

    def register_function(self, name, function, functionname=False):
        if functionname:
            self.buttons[name].config(command=self.functions[functionname])
        else:
            self.buttons[name].config(command=function)

    def register_checkbox(self, canvasname, x, y, checkboxname):
        self.canvases[canvasname].create_window(x, y, anchor=tk.NW, window=self.checkboxes[checkboxname])

    def add_canvas(self, name, width, height):
        tmp = tk.Canvas(self.window, width=width, height=height)
        tmp.pack()
        self.canvases[name] = tmp

    def register_image(self, canvasname, imagepath):
        tmp = Image.open(imagepath)
        tmp = ImageTk.PhotoImage(tmp.resize((1440, 810)))
        self.images[canvasname] = tmp
        self.canvases[canvasname].create_image(0, 0, anchor=tk.NW, image=self.images[canvasname])

    def add_progress_bar(self, name, length, maximum):
        tmp = ttk.Progressbar(orient="horizontal", length=length, maximum=maximum, mode="determinate")
        self.progressbars[name] = tmp

    def register_progress_bar(self, canvasname, x, y, name):
        self.canvases[canvasname].create_window(x, y, anchor=tk.NW, window=self.progressbars[name])

    def add_ttk_entry(self, name, width):
        tmp = ttk.Entry(width=width)
        self.entries[name] = tmp

    def register_ttk_entry(self, canvasname, x, y, entryname):
        self.canvases[canvasname].create_window(x, y, anchor=tk.NW, window=self.entries[entryname])

    def add_scrolltext_window(self, name, height, width):
        tmp = tk.scrolledtext.ScrolledText(master=self.window, height=height, width=width)
        self.scrolltexts[name] = tmp

    def register_scrolltext_window(self, canvasname, x, y, name):
        self.canvases[canvasname].create_window(x, y, anchor=tk.NW, window=self.scrolltexts[name])

    def add_text_on_canvas(self, canvasname, x, y, width, fill, text):
        self.canvases[canvasname].create_text(x, y, text=text, width=width, anchor=tk.NW, fill=fill)

    def add_labels(self, name, width, foreground, background):
        self.labeltextvariables[name] = ""
        tmp = ttk.Label(background=background, foreground=foreground, width=width,
                        textvariable=self.labeltextvariables[name])
        self.labels[name] = tmp
        # self.labelconfigs[name] = self.labels[name].config

    def register_labels(self, canvasname, x, y, name):
        self.canvases[canvasname].create_window(x, y, anchor=tk.NW, window=self.labels[name])

    # Function Declarations
    def save_paths(self):
        repentry = self.entries["replayfolderpathentry"].get()
        txtentry = self.entries["textfolderpathentry"].get()

        savepath = os.path.expanduser('~/documents/ONIZanalyzersettings.txt')
        with open(savepath, 'w') as f:
            f.write(f"{repentry}\n")
            f.write(f"{txtentry}")
        f.close()

    def load_paths(self):
        savepath = os.path.expanduser('~/documents/ONIZanalyzersettings.txt')
        with open(savepath, 'r') as f:
            repentry = f.readline().strip()
            txtentry = f.readline().strip()
        f.close()

        self.entries["replayfolderpathentry"].delete(0, 'end')
        self.entries["replayfolderpathentry"].insert(0, repentry)
        self.entries["textfolderpathentry"].delete(0, 'end')
        self.entries["textfolderpathentry"].insert(0, txtentry)

    def press_start(self):
        print("Button pressed!")
        repentry = self.entries["replayfolderpathentry"].get()
        txtentry = self.entries["textfolderpathentry"].get()
        replist, repcount = replay_file_parser(repentry)
        arg=[replist, txtentry, mainclass_copy.numberofprocesses,
             self.progressbars["replayprogressbar"], self.scrolltexts["outputscroll"]]

        replay_analyzer_class = replay_analysis_replaypool(replist, txtentry, mainclass_copy.numberofprocesses,
                                                           self.progressbars["replayprogressbar"], self.scrolltexts["outputscroll"],
                                                           self.labels["remainingtimelabel"])

        p = threading.Thread(name="replay analysis", target=replay_analyzer_class.replaypool_analysis)
        p.start()

    def select_replay_folder(self):
        replayfolderpath = filedialog.askdirectory(title="Select the root directory for ONIZ replays")
        self.entries["replayfolderpathentry"].delete(0, tk.END)
        self.entries["replayfolderpathentry"].insert(0, replayfolderpath)

    def select_text_output_folder(self):
        textfolderpath = filedialog.askdirectory(title="Select the output directory for text files")
        self.entries["textfolderpathentry"].delete(0, tk.END)
        self.entries["textfolderpathentry"].insert(0, textfolderpath)

    def press_duplicate_replay_check(self):
        print("Button pressed!")
        repentry = self.entries["replayfolderpathentry"].get()
        txtentry = self.entries["textfolderpathentry"].get()
        delcheck = self.variables["deletedupes"].get()
        replist, _ = replay_file_parser(repentry)
        replay_duplicate_check(replist, txtentry, mainclass_copy.numberofprocesses,
                               delcheck, self.scrolltexts["outputscroll"], self.progressbars["replayprogressbar"],
                               self.labels["remainingtimelabel"])

# https://hhj6212.github.io/programming/python/2021/04/18/python-multi.html
# https://web.archive.org/web/20201111190045id_/https://effbot.org/tkinterbook/entry.htm


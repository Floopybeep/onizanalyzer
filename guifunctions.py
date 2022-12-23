import tkinter as tk
import tkinter.ttk as ttk
import threading
import multiprocessing

from tkinter import scrolledtext
from tkinter import filedialog
from PIL import Image, ImageTk
from functions import replay_file_parser, separate_replaypool

global mainclass_copy

class NewClass:
    def __init__(self, mainclass):
        global mainclass_copy
        mainclass_copy = mainclass
        self.ui = onizGUI()
        self.ui.add_frame("frame1")

        self.ui.add_canvas("canvas", 1440, 810)
        self.ui.register_image("canvas", "C:/Users/USER/PycharmProjects/onizanalyzer/410542.jpg")
        # self.ui.register_image("canvas", "410542.jpg")

        self.ui.add_button("startbutton", "canvas", 8, "Start")
        self.ui.add_button("closebutton", "canvas", 7, "Close")
        self.ui.add_button("repentrybutton", "canvas", 15, "Designate Path")
        self.ui.add_button("textentrybutton", "canvas", 15, "Designate Path")
        self.ui.register_button("canvas", 1260, 748, "startbutton")
        self.ui.register_button("canvas", 1340, 748, "closebutton")
        self.ui.register_button("canvas", 1300, 48, "repentrybutton")
        self.ui.register_button("canvas", 1300, 98, "textentrybutton")
        self.ui.register_function("closebutton", self.ui.window.destroy)

        self.ui.add_progress_bar("replayprogressbar", 1200, 1200)
        self.ui.register_progress_bar("canvas", 30, 750, "replayprogressbar")

        self.ui.add_ttk_entry("replayfolderpathentry", 70)
        self.ui.add_ttk_entry("textfolderpathentry", 70)
        self.ui.register_ttk_entry("canvas", 800, 50, "replayfolderpathentry")
        self.ui.register_ttk_entry("canvas", 800, 100, "textfolderpathentry")
        self.ui.register_function("repentrybutton", self.ui.select_replay_folder)
        self.ui.register_function("textentrybutton", self.ui.select_text_output_folder)
        self.ui.register_function("startbutton", self.ui.press_start)

        self.ui.add_scrolltext_window("outputscroll", 40, 100)
        self.ui.register_scrolltext_window("canvas", 30, 30, "outputscroll")

        self.ui.add_labels("remainingtimelabel", 60, "white", "black")
        self.ui.register_labels("canvas", 230, 724, "remainingtimelabel")

        self.ui.add_text_on_canvas("canvas", 800, 30, 300, "white", "ONIZ replay root folder path:")
        self.ui.add_text_on_canvas("canvas", 800, 80, 300, "white", "ONIZ replay text file output folder path:")
        self.ui.add_text_on_canvas("canvas", 30, 725, 500, "white", "Estimated time remaining: ")

        self.ui.start()


class onizGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.frames = {}
        self.buttons = {}
        self.canvases = {}
        self.images = {}
        self.progressbars = {}
        self.entries = {}
        self.functions = {}
        self.scrolltexts = {}
        self.labels = {}

    def start(gui):
        class Threader(threading.Thread):
            def start(self):
                gui.window.mainloop()
        Threader().start()

    def add_frame(self, name):
        tmp = ttk.Frame(self.window)
        tmp.pack()
        self.frames[name] = tmp

    def add_button(self, name, canvasname, width, text):
        tmp = ttk.Button(self.canvases[canvasname], width=width, text=text)
        self.buttons[name] = tmp

    def register_button(self, canvasname, x, y, buttonname):
        self.canvases[canvasname].create_window(x, y, anchor=tk.NW, window=self.buttons[buttonname])

    def register_function(self, name, function, functionname=False):
        if functionname:
            self.buttons[name].config(command=self.functions[functionname])
        else:
            self.buttons[name].config(command=function)

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
        tmp = ttk.Label(background=background, foreground=foreground, width=width)
        self.labels[name] = tmp

    def register_labels(self, canvasname, x, y, name):
        self.canvases[canvasname].create_window(x, y, anchor=tk.NW, window=self.labels[name])

    # Function Declarations
    def press_start(self):
        print("Button pressed!")
        repentry = self.entries["replayfolderpathentry"].get()
        txtentry = self.entries["textfolderpathentry"].get()
        replist, repcount = replay_file_parser(repentry)
        separate_replaypool(replist, txtentry, mainclass_copy.numberofprocesses)

    def select_replay_folder(self):
        replayfolderpath = filedialog.askdirectory(title="Select the root directory for ONIZ replays")
        self.entries["replayfolderpathentry"].delete(0, tk.END)
        self.entries["replayfolderpathentry"].insert(0, replayfolderpath)

    def select_text_output_folder(self):
        textfolderpath = filedialog.askdirectory(title="Select the output directory for text files")
        self.entries["textfolderpathentry"].delete(0, tk.END)
        self.entries["textfolderpathentry"].insert(0, textfolderpath)


# https://hhj6212.github.io/programming/python/2021/04/18/python-multi.html
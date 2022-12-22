import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
from PIL import Image, ImageTk

from tkinter import scrolledtext
from tkinter import messagebox


def select_replay_folder():
    global replayfolderpath
    replayfolderpath = filedialog.askdirectory(title="Select the root directory for ONIZ replays")
    replayfolderpathentry.delete(0, tk.END)
    replayfolderpathentry.insert(0, replayfolderpath)


def select_text_output_folder():
    global textfolderpath
    textfolderpath = filedialog.askdirectory(title="Select the output directory for text files")
    textfolderpathentry.delete(0, tk.END)
    textfolderpathentry.insert(0, textfolderpath)


imagepath = "C:/Users/USER/PycharmProjects/onizanalyzer/sc2 stock photos/557285.jpg"

window = tk.Tk(screenName="ONIZ Replay Analyzer   - by ProDem")
frame = ttk.Frame(window)
frame.pack()

pilimage = Image.open(imagepath)
image = ImageTk.PhotoImage(pilimage.resize((1440, 810)))

canvas = tk.Canvas(window, width=1440, height=810)
canvas.background = image
canvas.create_image(0, 0, anchor=tk.NW, image=image)
canvas.pack()

# Start Button
startbutton = ttk.Button(text="Start", width=8)
canvas.create_window(1260, 748, anchor=tk.NW, window=startbutton)

# Close button
closebutton = ttk.Button(text="Exit", width=8, command=window.destroy)
canvas.create_window(1340, 748, anchor=tk.NW, window=closebutton)

# Replay root folder entry
canvas.create_text(800, 30, text="ONIZ replay root folder path:", width=300, anchor=tk.NW, fill="white")
repentrybutton = ttk.Button(master=canvas, text="Designate Path", width=15, command=select_replay_folder)
canvas.create_window(1300, 48, anchor=tk.NW, window=repentrybutton)
replayfolderpathentry = ttk.Entry(master=canvas, width=70)
canvas.create_window(800, 50, anchor=tk.NW, window=replayfolderpathentry)

# Text file output folder entry
canvas.create_text(800, 80, text="ONIZ replay text file output folder path:", width=300, anchor=tk.NW, fill="white")
textentrybutton = ttk.Button(master=canvas, text="Designate Path", width=15, command=select_text_output_folder)
canvas.create_window(1300, 98, anchor=tk.NW, window=textentrybutton)
textfolderpathentry = ttk.Entry(master=canvas, width=70)
canvas.create_window(800, 100, anchor=tk.NW, window=textfolderpathentry)

# Replay analysis progress scrolloutput window
outputscroll = tk.scrolledtext.ScrolledText(master=window, height=40, width=100)
outputscroll.insert(index="1.0", chars="Hello\n")
canvas.create_window(30, 30, anchor=tk.NW, window=outputscroll)

# doneevent = tk.messagebox.showinfo(title="Analysis Complete", message="Replay Analysis has been completed!")

# Replay analysis progress bar (lower screen)
progressbar = ttk.Progressbar(orient="horizontal", length=1200, maximum=1200, mode="determinate")
# progressbar.start(interval=100) # miliseconds
# progressbar.step(amount=1)
# progressbar.stop()
canvas.create_window(30, 750, anchor=tk.NW, window=progressbar)

# Estimated time remaining
canvas.create_text(30, 725, anchor=tk.NW, text="Estimated time remaining: ", width=500, fill="white", font=8)
remainingtimelabel = ttk.Label(text="1320 seconds", background="black", foreground="white", width=60, font=8)
# remainingtimelabel.config(text="newtext")
canvas.create_window(230, 724, anchor=tk.NW, width=160, window=remainingtimelabel)

window.mainloop()


# https://docs.python.org/3/library/tkinter.html
# https://docs.python.org/3/library/tkinter.ttk.html

# https://realpython.com/python-gui-tkinter/

# Themes
    # https://github.com/rdbende/Azure-ttk-theme
# https://wiki.tcl-lang.org/page/List+of+ttk+Themes

# canvas tutorial
    # https://cosmosproject.tistory.com/619

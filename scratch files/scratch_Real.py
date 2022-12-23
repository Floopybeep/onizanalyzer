import tkinter as tk
import multiprocessing
import time

def loop(a, b, c, d):
     # Will just sleep for 3 seconds.. simulates whatever processing you do.
    time.sleep(3)
    return

def queue_loop():
    p = multiprocessing.Process(target = loop,
                                args = (1, 2),
                                kwargs = {"c": 3, "d": 4})
    # You can pass args and kwargs to the target function like that
    # Note that the process isn't started yet. You call p.start() to activate it.
    p.start()
    check_status(p) # This is the next function we'll define.
    return

def check_status(p):
    """ p is the multiprocessing.Process object """
    if p.is_alive(): # Then the process is still running
        label.config(text = "MP Running")
        mp_button.config(state = "disabled")
        not_mp_button.config(state = "disabled")
        root.after(200, lambda p=p: check_status(p)) # After 200 ms, it will check the status again.
    else:
        label.config(text = "MP Not Running")
        mp_button.config(state = "normal")
        not_mp_button.config(state = "normal")
    return


if __name__ == "__main__":
    root = tk.Tk()
    mp_button = tk.Button(master = root, text = "Using MP", command = queue_loop)
    mp_button.pack()
    label = tk.Label(master = root, text = "MP Not Running")
    label.pack()
    not_mp_button = tk.Button(master = root, text = "Not MP", command = lambda: loop(1,2,3,4))
    not_mp_button.pack()
    root.mainloop()
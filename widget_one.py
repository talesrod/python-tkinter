import tkinter as tk
from tkinter import ttk


class Application:
    def __init__(self, master=None):
        self.widget1 = ttk.Frame(master)
        self.widget1.pack()
        self.msg = ttk.Label(self.widget1,text="Primeiro Wiget")
        self.msg.pack()

root = tk.Tk()

Application(root)
root.mainloop()
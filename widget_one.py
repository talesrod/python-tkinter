import tkinter as tk
from tkinter import ttk


class Application:
    def __init__(self, master=None):
        self.widget1 = ttk.Frame(master)
        self.widget1.pack()
        self.msg = ttk.Label(self.widget1,text="Primeiro Wiget")
        self.msg["font"] = ("Verdana",10,"italic","bold")
        self.msg.pack()
        self.sair = ttk.Button(self.widget1, text="Sair", command=self.widget1.quit)
        style = ttk.Style()
        style.configure("TButton", font=("Calibri", 10))
        self.sair.pack()

root = tk.Tk()

Application(root)
root.mainloop()
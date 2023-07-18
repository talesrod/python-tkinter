import tkinter as tk
from tkinter import ttk


class Application:
    def __init__(self, master=None):
        self.widget1 = ttk.Frame(master)
        self.widget1.pack()
        self.msg = ttk.Label(self.widget1,text="Primeiro widget")
        self.msg["font"] = ("Verdana",10,"italic","bold")
        self.msg.pack()
        self.sair = ttk.Button(self.widget1,text="Clique aqui")
        style = ttk.Style()
        style.configure("TButton",font=("Calibri", 10),width=20)
        self.sair.bind("<Button-1>",self.mudarTexto)
        self.sair.pack(side="right")
    def mudarTexto(self,event):
        if self.msg["text"] == "Primeiro widget":
            self.msg["text"] = "O botão recebeu um clique"
           
        else:
            self.msg["text"] = "Primeiro Widget"

root = tk.Tk()

Application(root)
root.mainloop()
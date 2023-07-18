import tkinter as tk
from tkinter import ttk
#uso de dados mockados
class Application:
    def __init__(self,master=None):
        self.fontePadrao = ("Arial","10")
        self.primeiroContainer = ttk.Frame(master)
        self.primeiroContainer["padding"] =  10
        self.primeiroContainer.pack()

        self.segundoContainer = ttk.Frame(master)
        self.segundoContainer["padding"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = ttk.Frame(master)
        self.terceiroContainer["padding"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = ttk.Frame(master)
        self.quartoContainer["padding"] = 20
        self.quartoContainer.pack()
        
        self.titulo = ttk.Label(self.primeiroContainer,text="Dados do Usuário")
        self.titulo["font"] = ("Arial","10","bold")
        self.titulo.pack()

        self.nomeLabel = ttk.Label(self.segundoContainer,text="nome",font=self.fontePadrao)
        self.nomeLabel.pack(side="left")

        self.nome = ttk.Entry(self.segundoContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side="left")

        self.senhaLabel = ttk.Label(self.terceiroContainer,text="Senha",font=self.fontePadrao)
        self.senhaLabel.pack(side="left")

        self.senha = ttk.Entry(self.terceiroContainer)
        self.senha["width"] = 30
        self.senha["font"] = self.fontePadrao
        self.senha["show"] = "*"
        self.senha.pack(side="left")

        self.style = ttk.Style()
        self.style.configure("Custom.TButton", font=self.fontePadrao)
        self.autenticar = ttk.Button(self.quartoContainer, text="Autenticar", style="Custom.TButton", width=12, command=self.verificaSenha)
        self.autenticar.pack()

        self.mensagem = ttk.Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

    # método verificar senha
    def verificaSenha(self):
        usuario = self.nome.get()
        senha = self.senha.get()
        if usuario == "usuariodevmedia" and senha == "dev":
            self.mensagem["text"] = "Autenticado"
        else:
            self.mensagem["text"] = "Erro na autenticação"

root = tk.Tk()
Application(root)
root.mainloop()

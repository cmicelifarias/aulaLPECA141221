from tkinter import *

class Aplicacao:
    
    def __init__(self, master=None):
        self.fonte = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack() 

        self.titulo = Label(self.primeiroContainer, text="Dados dos usuários")
        self.titulo["font"] = ("Arial","10","bold")
        self.titulo.pack()

        self.nomeLabel = Label(self.segundoContainer,text="Nome",font=self.fonte)
        self.nomeLabel.pack(side=LEFT)

        self.nome= Entry(self.segundoContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fonte
        self.nome.pack(side=LEFT)

        self.senhaLabel = Label(self.terceiroContainer, text="Senha", font= self.fonte)
        self.senhaLabel.pack(side=LEFT)

        self.senha=Entry(self.terceiroContainer)
        self.senha["width"] = 30
        self.senha["font"] = self.fonte
        self.senha["show"] ="*"
        self.senha.pack(side=LEFT)

        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "Autenticar"
        self.autenticar["font"] = ("Verdana","8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.verificaSenha
        self.autenticar.pack()

        self.mensagem = Label(self.quartoContainer, text="", font=self.fonte)
        self.mensagem.pack()
    
    def verificaSenha(self):
        usuario = self.nome.get()
        senha = self.senha.get()

        if usuario == "Buda" and senha == "Buda":
            self.mensagem["text"] = "Acesso garantido"
        else:
            self.mensagem["text"] = "Acesso negado"


root = Tk()
Aplicacao(root)
root.mainloop()


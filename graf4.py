from tkinter import *

class Aplicacao:
    def __init__(self,master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.msg = Label(self.widget1, text="Ainda um label")
        self.msg["font"] = ("Verdana","12","italic")
        self.msg.pack()

        #cria botao
        self.sair = Button(self.widget1)
        self.sair["text"] = "Clica"
        self.sair["font"] = ("Times","10")
        self.sair["width"] = 10
        self.sair.bind("<Button-1>", self.mudarTexto)
        #self.sair["command"] = self.widget1.quit
        self.sair.pack()
    
    def mudarTexto(self, event):
        if self.msg["text"] == "Ainda um label":
            self.msg["text"] = "Alguém clicou"
        else:
            self.msg["text"] = "Ainda um label"

root = Tk()
Aplicacao(root)
root.mainloop()
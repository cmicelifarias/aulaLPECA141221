from tkinter import *

class Aplicacao:
    def __init__(self,master=None):
        self.widget1 = Frame(master)
        self.widget1.pack(side=RIGHT)
        self.msg = Label(self.widget1, text="Outro label")
        self.msg["font"] = ("Verdana","12","italic")
        self.msg.pack()
        self.sair = Button(self.widget1)
        self.sair["text"] = "Tchau"
        self.sair["font"] = ("Times","10")
        self.sair["width"] = 5
        self.sair["command"] = self.widget1.quit
        self.sair.pack(side=RIGHT)

root = Tk()
Aplicacao(root)
root.mainloop()
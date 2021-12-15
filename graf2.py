from tkinter import *

class Aplicacao:
    def __init__(self,master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.msg = Label(self.widget1, text="Meu primeiro widget")
        self.msg.pack()

root = Tk()
Aplicacao(root)
root.mainloop()
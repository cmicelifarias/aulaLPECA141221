from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
import subprocess

ide = Tk()
ide.title("Minha ide fulera")
file_path = ""

editor=Text()
editor.pack()
code_output = Text(height=10)
code_output.pack()

menu_bar = Menu(ide)


def set_file_path(path):
    global file_path
    file_path = path

def open_file():
    path = askopenfilename(filetypes=[("Arquivo Python","*.py")])
    with open(path,"r") as file:
        code = file.read()
        editor.delete("1.0", END)
        editor.insert("1.0",code)
        set_file_path(path)

def save_as():
    if file_path == "":
        path = asksaveasfilename(filetypes=[("Arquivo Python","*.py")])
    else:
        path = file_path
    with open(path, "w") as file:
        code = editor.get("1.0",END)
        file.write(code)
        set_file_path(path)

def run():
    if file_path == " ":
        save_prompt = Toplevel()
        text = Label(save_prompt, text="Salvar code")
        text.pack()
        return

    print("Entrei aqui")
    command = f'python3 {file_path}'
    process = subprocess.Popen(command, stdout=subprocess.PIPE,
                                        stderr= subprocess.PIPE,shell=True)
    output,error = process.communicate()
    print(output)
    code_output.insert("1.0", output)
    code_output.insert("1.0", error)


file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Abrir",command=open_file)
file_menu.add_command(label="Salvar",command=save_as)
file_menu.add_command(label="Salvar como",command=save_as())
file_menu.add_command(label="Sair",command=exit)
menu_bar.add_cascade(label="Arquivo", menu=file_menu)

run_bar = Menu(menu_bar,tearoff=0)
run_bar.add_command(label="Rodar",command=run)
menu_bar.add_cascade(label="Rodar",menu=run_bar)


ide.config(menu=menu_bar)

ide.mainloop()
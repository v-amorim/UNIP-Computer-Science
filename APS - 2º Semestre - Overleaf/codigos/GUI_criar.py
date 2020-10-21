from tkinter import *
import tkinter as tk
from functools import partial
from BD_criar import criar
import sqlite3


def validate_login(username, password):
    usuario = username.get()  # Pega o texto entrado na interface grafica e atribui à uma variável
    senha = password.get()  # Pega o texto entrado na interface grafica e atribui à uma variável

    if criar(usuario, senha) == 1:
        # Criação da Interface gráfica
        acesso_window = Tk()
        acesso_window.title("Sucesso")
        width = 180
        height = 40
        width_screen = acesso_window.winfo_screenwidth()
        height_screen = acesso_window.winfo_screenheight()
        x = (width_screen/2) - (width/2)
        y = (height_screen/2) - (height/2)-110
        acesso_window.geometry('%dx%d+%d+%d' % (width, height, x, y))
        # Texto da interface
        l1 = Label(acesso_window, text="Usuario criado com sucesso!")
        l1.grid(row=1, column=1)
        acesso_window.mainloop()

    elif criar(usuario, senha) == 2:
        # Criação da Interface gráfica
        acesso_window = Tk()
        acesso_window.title("Erro")
        width = 100
        height = 80
        width_screen = acesso_window.winfo_screenwidth()
        height_screen = acesso_window.winfo_screenheight()
        x = (width_screen/2) - (width/2)-5
        y = (height_screen/2) - (height/2)-140
        acesso_window.geometry('%dx%d+%d+%d' % (width, height, x, y))
        # Texto da interface
        l1 = Label(acesso_window, text="Usuário já existe\nou\nSenha em branco\n\nTente novamente!")
        l1.grid(row=1, column=1)
        acesso_window.mainloop()

    else:
        # Criação da Interface gráfica
        acesso_window = Tk()
        acesso_window.title("Erro")
        width = 100
        height = 40
        width_screen = acesso_window.winfo_screenwidth()
        height_screen = acesso_window.winfo_screenheight()
        x = (width_screen/2) - (width/2)-50
        y = (height_screen/2) - (height/2)-110
        acesso_window.geometry('%dx%d+%d+%d' % (width, height, x, y))
        # Texto da interface
        l1 = Label(acesso_window, text="Erro ao Criar!")
        l1.grid(row=1, column=1)
        acesso_window.mainloop()


# Criação da Interface grafica
login_window = Tk()
login_window.title("APS")
width = 200
height = 100
width_screen = login_window.winfo_screenwidth()
height_screen = login_window.winfo_screenheight()
x = (width_screen/2) - (width/2)
y = (height_screen/2) - (height/2)
login_window.geometry('%dx%d+%d+%d' % (width, height, x, y))
# 1a linha de texto
info_label = Label(login_window, text="APS 2º SEM - 3DES\nCriação de Usuario no BD")
info_label.grid(row=0, column=0, columnspan=2)
# 2a linha com o usuario e entrada de texto
username_label = Label(login_window, text="Usuario")
username_label.grid(row=1, column=0)
username = StringVar()
username_entry = Entry(login_window, textvariable=username)
username_entry.grid(row=1, column=1)
# 3a linha com a senha e entrada de texto
password_label = Label(login_window, text="Senha")
password_label.grid(row=2, column=0)
password = StringVar()
password_entry = Entry(login_window, textvariable=password, show='*')
password_entry.grid(row=2, column=1)
# 4a linha com o botão que acessa a função validate_login
validate_login = partial(validate_login, username, password)
login_button = Button(login_window, text="Login", width=20, command=validate_login)
login_button.grid(row=5, column=1)
login_window.mainloop()

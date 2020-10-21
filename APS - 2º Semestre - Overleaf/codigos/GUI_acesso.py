from tkinter import *
import tkinter as tk
from functools import partial
from BD_acesso import acessar
import sqlite3


def validate_login(username, password):
    username = username.get()
    password = password.get()

    def substancias():  # Função que cria a janela para selecionar as substancias e mostra-las usando o BD
        conn = sqlite3.connect('bancodedados.db')
        # Criação da Interface gráfica
        substancias_window = tk.Tk()
        substancias_window.title("Substancias")
        width = 200
        height = 200
        width_screen = substancias_window.winfo_screenwidth()
        height_screen = substancias_window.winfo_screenheight()
        x = (width_screen/2) - (width/2)+210
        y = (height_screen/2) - (height/2)+100
        substancias_window.geometry('%dx%d+%d+%d' % (width, height, x, y))
        # Cria cursor que acessa a tabela substancias no BD
        cursor = conn.execute('''SELECT * from substancias''')
        i = 0
        for substancia in cursor:
            for j in range(len(substancia)):
                e = Entry(substancias_window, width=10, fg='blue')
                e.grid(row=i, column=j)  # Cria uma matriz com a quantidade de linhas e colunas de substancias
                e.insert(END, substancia[j])  # Atribui o valor do elemento localizado em substancia[j] na matriz
            i = i+1
        substancias_window.mainloop()
        conn.close()  # Fecha conexão com BD

    def tripulacao():
        conn = sqlite3.connect('bancodedados.db')
        # Criação da Interface gráfica
        tripulacao_window = tk.Tk()
        tripulacao_window.title("Tripulantes")
        width = 400
        height = 200
        width_screen = tripulacao_window.winfo_screenwidth()
        height_screen = tripulacao_window.winfo_screenheight()
        x = (width_screen/2) - (width/2)-310
        y = (height_screen/2) - (height/2)+100
        tripulacao_window.geometry('%dx%d+%d+%d' % (width, height, x, y))
        # Cria cursor que acessa a tabela tripulacao no BD
        cursor = conn.execute('''SELECT * from tripulacao''')
        i = 0
        for tripulante in cursor:
            for j in range(len(tripulante)):
                e = Entry(tripulacao_window, width=25, fg='blue')
                e.grid(row=i, column=j)  # Cria uma matriz com a quantidade de linhas e colunas de tripulantes
                e.insert(END, tripulante[j])  # Atribui o valor do elemento localizado em tripulante[j] na matriz
            i = i+1
        tripulacao_window.mainloop()
        conn.close()  # Fecha conexão com BD

    if acessar(username, password) == 1:
        # Criação da Interface gráfica
        acesso_window = Tk()
        acesso_window.title("Banco de Dados")
        width = 150
        height = 100
        width_screen = acesso_window.winfo_screenwidth()
        height_screen = acesso_window.winfo_screenheight()
        x = (width_screen/2) - (width/2)
        y = (height_screen/2) - (height/2)+140
        acesso_window.geometry('%dx%d+%d+%d' % (width, height, x, y))
        # 1a linha de texto
        l1 = Label(acesso_window, text="Acesso Permitido\nEscolha uma opção")
        l1.grid(row=1, column=2, columnspan=2)
        # 2a linha com o botão que acessa a função subtancias
        b1 = Button(acesso_window, text="Substancias->", width=20, command=substancias)
        b1.grid(row=2, column=2)
        # 3a linha com o botão que acessa a função tripulancao
        b2 = Button(acesso_window, text="<-Tripulantes", width=20, command=tripulacao)
        b2.grid(row=3, column=2)
        acesso_window.mainloop()

    elif acessar(username, password) == 2:
        # Criação da Interface gráfica
        acesso_window = Tk()
        acesso_window.title("Erro senha")
        width = 20
        height = 40
        width_screen = acesso_window.winfo_screenwidth()
        height_screen = acesso_window.winfo_screenheight()
        x = (width_screen/2) - (width/2)-50
        y = (height_screen/2) - (height/2)-110
        acesso_window.geometry('%dx%d+%d+%d' % (width, height, x, y))
        # Texto da interface
        l1 = Label(acesso_window, text="Acesso Negado\nSenha invalida")
        l1.grid(row=1, column=1)
        acesso_window.mainloop()

    elif acessar(username, password) == 3:
        # Criação da Interface gráfica
        acesso_window = Tk()
        acesso_window.title("Erro Usuario")
        width = 180
        height = 40
        width_screen = acesso_window.winfo_screenwidth()
        height_screen = acesso_window.winfo_screenheight()
        x = (width_screen/2) - (width/2)
        y = (height_screen/2) - (height/2)-110
        acesso_window.geometry('%dx%d+%d+%d' % (width, height, x, y))
        # Texto da interface
        l1 = Label(acesso_window, text="Login inválido\nMantenha-se longe do navio.")
        l1.grid(row=1, column=1)
        acesso_window.mainloop()


# Interface grafica
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
info_label = Label(login_window, text="APS 2º SEM - 3DES\nAcesso ao BD ")
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

# -*- coding: utf-8 -*-
# IMPORTES ########################################################################################################################################################
import sqlite3
from bancos import bancoUsuarios, curUsuarios
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
import sys

# CORES ############################################################################################################################################################
corPreta = "#2e2d2b" 
corBranca = "#feffff" 
corVerde = "#8EB897"
corLetra = "#403d3d" 
corCinza = "#e9edf5" 
corBorda ="#82A0BC" 

# FUNÇÃO DE VERIFICAR LOGIN ########################################################################################################################################
def verifica_login():
    user = e_user.get()
    senha = e_senha.get()
    if user == "" or senha == "":
        messagebox.showinfo(title="Error", message="Preencha os campos corretamente.")
    elif senha.isdigit() == False:
        messagebox.showinfo(title="Error", message="A senha é exclusivamente numérica.")
        e_senha.delete(0, END)
    else:
        senha = int(e_senha.get())
        curUsuarios.execute("""SELECT * FROM tabelaUsuarios""")
        usuarios = curUsuarios.fetchall()
        admOk = False
        userOk = False
        for u in usuarios: 
            if user in u and senha in u and u[2] == "S":
                admOk = True
                break
            elif user in u and senha in u and u[2] == "N":
                userOk = True
                break
        if admOk == True:
            os.system('python menu_admin.py')
        elif userOk == True:
            os.system('python menu_tecnico.py')
        else:
            messagebox.showinfo(title="Error", message="Usuário ou senha inexistentes.")

# INTERFACE GRÁFICA ################################################################################################################################################
    # Criação Janela Principal
janLogin = Tk()
janLogin.configure(background=corCinza)
janLogin.resizable(width=FALSE, height=FALSE)
janLogin.geometry("800x400")
janLogin.title("Central de Ferramentaria")

    # Título Login
f_titulo = Frame(master=janLogin, width=800, height=60, bg=corBranca, relief=FLAT)
f_titulo.place(x=0, y=10)
l_title = Label(master=f_titulo, text="LOGIN", bg=corBranca, fg=corLetra, font=("Verdana 25 bold")) 
l_title.place(x=355, y=10)

    # Entrada Usuário
l_user = Label(master=janLogin, text="USUÁRIO", bg=corCinza, fg=corLetra, font=("Verdana 12 bold"))  
l_user.place(x=175, y= 140)
e_user = Entry(master=janLogin, bg=corBranca, fg=corLetra, justify="left", width= 40, font=("Verdana 12"), borderwidth=0, highlightbackground=corBorda)
e_user.place(x=260, y=140)

    # Entrada Senha
l_senha = Label(master=janLogin, text="SENHA", bg=corCinza, fg=corLetra, font=("Verdana 12 bold"))  
l_senha.place(x=181, y= 200)
e_senha= Entry(master=janLogin, bg=corBranca, fg=corLetra, justify="left", width= 40, font=("Verdana 12"), borderwidth=0, highlightbackground=corBorda)
e_senha.place(x=260, y=200) 

    # Botão Logar
btn_logar = Button(master=janLogin, command=lambda: verifica_login(), text="ENTRAR", font=("Verdana 11 bold"), highlightbackground=corVerde, fg=corLetra, height=2, width=16)
btn_logar.place(x=315, y=290)
 
# EXECUÇÃO DA JANELA ###############################################################################################################################################
janLogin.mainloop()


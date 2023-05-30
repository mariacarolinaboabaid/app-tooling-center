# -*- coding: utf-8 -*-
from tkinter import *
import os
import sys
from tkinter import ttk

# CORES ############################################################################################################################################################
corPreta = "#2e2d2b"
corBranca = "#feffff"
corVerde = "#8EB897"
corLetra = "#403d3d"
corCinza = "#e9edf5"
corBorda = "#82A0BC"

janelaMenuAdmin = Tk()

# Título da tela
janelaMenuAdmin.title('Central de Ferramentaria')

# Tamanho da tela
janelaMenuAdmin.geometry("300x300")
janelaMenuAdmin.resizable(width=FALSE, height=FALSE)

janelaMenuAdmin.configure(background=corCinza)
style = ttk.Style(janelaMenuAdmin)
style.theme_use("clam")


def botao_cadastrar_tecnico():
    os.system('python cadastroTecnico.py')


def botao_consultar_tecnico():
    os.system('python consultaTecnicoAdmin.py')


def botao_cadastrar_ferramenta():
    os.system('python cadastroFerramenta.py')


def botao_consultar_ferramenta():
    os.system('python consultaFerramentaAdmin.py')


# Botão Cadastrar Tecnico
botao_cadastrar_tecnico_menu_admin = Button(janelaMenuAdmin, text='Cadastrar Tecnico', font="Verdana 9 bold", highlightbackground="#FFE19C", fg=corLetra, height=2, width=15, command=botao_cadastrar_tecnico).place(x=50, y=20, width=200, height=40)

# Botão Consultar Tecnico
botao_consultar_tecnico_menu_admin = Button(janelaMenuAdmin, text='Consultar Tecnico', font="Verdana 9 bold", highlightbackground="#FFE19C", fg=corLetra, height=2, width=15, command=botao_consultar_tecnico).place(x=50, y=80, width=200, height=40)

# Botão Cadastrar Ferramenta
botao_cadastrar_ferramenta_menu_admin = Button(janelaMenuAdmin, text='Cadastrar Ferramenta', font="Verdana 9 bold", highlightbackground="#FFE19C", fg=corLetra, height=2, width=15, command=botao_cadastrar_ferramenta).place(x=50, y=180, width=200, height=40)

# Botão Consultar Ferramenta
botao_consultar_ferramenta_menu_admin = Button(janelaMenuAdmin, text='Consultar Ferramenta', font="Verdana 9 bold", highlightbackground="#FFE19C", fg=corLetra, height=2, width=15, command=botao_consultar_ferramenta).place(x=50, y=230, width=200, height=40)

# Impressão da tela
janelaMenuAdmin.mainloop()

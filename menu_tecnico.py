# -*- coding: utf-8 -*-
from tkinter import *
import os
import sys
from tkinter import ttk

from bancos import bancoTecnicos, curTecnicos
# CORES ############################################################################################################################################################
corPreta = "#2e2d2b"
corBranca = "#feffff"
corVerde = "#8EB897"
corLetra = "#403d3d"
corCinza = "#e9edf5"
corBorda = "#82A0BC"

janelaMenuTecnico = Tk()

# Título da tela
janelaMenuTecnico.title('Central de Ferramentaria')
janelaMenuTecnico.configure(background=corCinza)
# Tamanho da tela
janelaMenuTecnico.geometry("300x300")
janelaMenuTecnico.resizable(width=FALSE, height=FALSE)
style = ttk.Style(janelaMenuTecnico)
style.theme_use("clam")


def botao_consultar_ferramenta():
    os.system('python consultaFerramenta.py')


# Botão Consultar Ferramenta
button_consultar_ferramenta_menu_tecnico = Button(janelaMenuTecnico, text='CONSULTAR FERRAMENTA', font="Verdana 9 bold", highlightbackground="#FFE19C", fg=corLetra, height=2, width=15, command=botao_consultar_ferramenta).place(x=50, y=100, width=200, height=40)



# Impressão da tela
janelaMenuTecnico.mainloop()
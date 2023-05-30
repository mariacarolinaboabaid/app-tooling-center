# -*- coding: utf-8 -*-

# Importes
from tkinter import *
from tkinter import messagebox
from bancos import bancoFerramentas, curFerramentas
import os
import sys
# from tkinter.ttk import Combobox

# FUNÇÕES DE VALIDAÇÃO DO ENTRY ####################################################################################################################################
    # Limitação de 60 caracteres para o campo da descrição
def limitar_caractere_descricao(p):
    if len(p) > 60:
        return False
    return True

    #  Limitação de 25 caracteres para o campo do part number
def limitar_caractere_number(p):
    if len(p) > 25:
        return False
    return True

    # Limitação de 30 caracteres para o campo do fabricante
def limitar_caractere_fabricante(p):
    if len(p) > 30:
        return False
    return True

    # Limitação de 15 caracteres para o campo da voltagem
def limitar_caractere_voltagem(p):
    if len(p) > 15:
        return False
    return True

    # Limitação de 20 caracteres para o campo do tamanho
def limitar_caratere_tamanho(p):
    if len(p) > 20:
        return False
    return True

    # Limitação de 15 caracteres para o campo da medida
def limitar_caratere_medida(p):
    if len(p) > 15:
        return False
    return True

    # Limitação de 15 caracteres para o campo do tipo
def limitar_caratere_tipo(p):
    if len(p) > 15:
        return False
    return True

    # Limitação de 15 caracteres para o campo do material
def limitar_caratere_material(p):
    if len(p) > 15:
        return False
    return True

# FUNÇÕES BOTÕES ###################################################################################################################################################
def cadastrar():
    # Associando os entries à variáveis 
    descr = entry_descricao_cadastro_ferramenta.get()
    partNumber = entry_number_cadastro_ferramenta.get()
    fabricante = entry_fabricante_cadastro_ferramenta.get()
    voltagem = entry_voltagem_cadastro_ferramenta.get()
    tamanho = entry_tamanho_cadastro_ferramenta.get()
    medida = entry_medida_cadastro_ferramenta.get()
    tipo = entry_tipo_cadastro_ferramenta.get()
    material = entry_material_cadastro_ferramenta.get()
    # Caso haja um campo sem preenchimento
    if descr == "" or partNumber == "" or fabricante == "" or voltagem == "" or tamanho == "" or medida == "" or tipo == "" or material == "": 
        messagebox.showinfo(title="Error", message="Todos os campos são de preenchimento obrigatório.")
    # Caso a senha, telefone ou CPF não sejam numéricos:
    elif partNumber.isdigit() == False or tamanho.isdigit() == False:
        messagebox.showinfo(title="Error", message="Os campos tamanho e partNumber são exclusivamente numéricos.")
    # Comando SQL - 
    else:
        curFerramentas.execute("""INSERT INTO tabelaFerramentas
            (descr, fabricante, voltagem, partNumber, tamanho, unidadeMedida, tipo, material) 
            VALUES
            (?, ?, ?, ? , ?, ?, ? , ?)""", (descr, fabricante, voltagem, partNumber, tamanho, medida, tipo, material))
        bancoFerramentas.commit()
    # Informação de cadastro realizado com sucesso
        messagebox.showinfo(title="Sucesso", message="Ferramenta cadastrada com sucesso.")
        entry_descricao_cadastro_ferramenta.delete(0, END)
        entry_number_cadastro_ferramenta.delete(0, END)
        entry_fabricante_cadastro_ferramenta.delete(0, END)
        entry_voltagem_cadastro_ferramenta.delete(0, END)
        entry_tamanho_cadastro_ferramenta.delete(0, END)
        entry_medida_cadastro_ferramenta.delete(0, END)
        entry_tipo_cadastro_ferramenta.delete(0, END)
        entry_material_cadastro_ferramenta.delete(0, END)

def voltar():
    janelaCadastroFerramenta.destroy()

# CORES ############################################################################################################################################################
corPreta = "#2e2d2b" 
corBranca = "#feffff" 
corVerde = "#8EB897"
corLetra = "#403d3d" 
corCinza = "#e9edf5" 
corBorda ="#82A0BC" 

#  INTERFACE GRÁFICA ################################################################################################################################################
    # Criando a janela
janelaCadastroFerramenta = Tk()
janelaCadastroFerramenta.title('Central de Ferramentaria')
janelaCadastroFerramenta.configure(background=corCinza)
janelaCadastroFerramenta.resizable(width=FALSE, height=FALSE)
janelaCadastroFerramenta.geometry("1000x400")

    # Atribuindo a função a uma variável que servirá de parâmetro para o método de validação
vcmd_descricao = janelaCadastroFerramenta.register(func=limitar_caractere_descricao)
    # Atribuindo a função a uma variável que servirá de parâmetro para o método de validação
vcmd_number = janelaCadastroFerramenta.register(func=limitar_caractere_number)
    # Atribuindo a função a uma variável que servirá de parâmetro para o método de validação
vcmd_voltagem = janelaCadastroFerramenta.register(func=limitar_caractere_voltagem)
    # Atribuindo a função a uma variável que servirá de parâmetro para o método de validação
vcmd_fabricante = janelaCadastroFerramenta.register(func=limitar_caractere_fabricante)
    # Atribuindo a função a uma variável que servirá de parâmetro para o método de validação
vcmd_tamanho = janelaCadastroFerramenta.register(func=limitar_caratere_tamanho)
    # Atribuindo a função a uma variável que servirá de parâmetro para o método de validação
vcmd_medida = janelaCadastroFerramenta.register(func=limitar_caratere_medida)
    # Atribuindo a função a uma variável que servirá de parâmetro para o método de validação
vcmd_tipo = janelaCadastroFerramenta.register(func=limitar_caratere_tipo)
    # Atribuindo a função a uma variável que servirá de parâmetro para o método de validação
vcmd_material = janelaCadastroFerramenta.register(func=limitar_caratere_material)

    # Título Cadastro Ferramenta 
f_title = Frame(master=janelaCadastroFerramenta, width=1200, height=60, bg=corBranca, relief=FLAT)
f_title.place(x=0, y=20)
l_title = Label(master=f_title, text="CADASTRO DE FERRAMENTAS", bg=corBranca, fg=corLetra, font=("Verdana 18 bold")) 
l_title.place(x=360, y=15)

    # Campo da Descrição da janela
label_descricao_cadastro_ferramenta = Label(text='DESCRIÇÃO', bg=corCinza, fg=corLetra, font=("Verdana 12 bold"))
label_descricao_cadastro_ferramenta.place(x=18, y=100)
entry_descricao_cadastro_ferramenta = Entry(janelaCadastroFerramenta, validate='key', validatecommand=(vcmd_descricao, '%P'), font=("Verdana 9 bold"), bg=corBranca, highlightbackground=corBorda, fg=corLetra, justify="left", width= 40)
entry_descricao_cadastro_ferramenta.place(x=125, y=100)

   # Campo do Part Number da ferramenta
label_number_cadastro_ferramenta = Label(text='PART NUMBER', bg=corCinza, fg=corLetra, font=("Verdana 12 bold"))
label_number_cadastro_ferramenta.place(x=18, y=140)
entry_number_cadastro_ferramenta = Entry(janelaCadastroFerramenta, validate='key', validatecommand=(vcmd_number, '%P'), font=("Verdana 9 bold"), bg=corBranca, highlightbackground=corBorda, fg=corLetra, justify="left", width= 40)
entry_number_cadastro_ferramenta.place(x=125, y=140)

    # Campo do Fabricante da ferramenta
label_fabricante_cadastro_ferramenta = Label(text='FABRICANTE', bg=corCinza, fg=corLetra, font=("Verdana 12 bold"))
label_fabricante_cadastro_ferramenta.place(x=18, y=180)
entry_fabricante_cadastro_ferramenta = Entry(janelaCadastroFerramenta, validate='key', validatecommand=(vcmd_fabricante, '%P'), font=("Verdana 9 bold"), bg=corBranca, highlightbackground=corBorda, fg=corLetra, justify="left", width= 40)
entry_fabricante_cadastro_ferramenta.place(x=125, y=180)

    # Campo da Voltagem da ferramenta
label_voltagem_cadastro_ferramenta = Label(text='VOLTAGEM', bg=corCinza, fg=corLetra, font=("Verdana 12 bold"))
label_voltagem_cadastro_ferramenta.place(x=18, y=220)
entry_voltagem_cadastro_ferramenta = Entry(janelaCadastroFerramenta, validate='key', validatecommand=(vcmd_voltagem, '%P'), font=("Verdana 9 bold"), bg=corBranca, highlightbackground=corBorda, fg=corLetra, justify="left", width= 40)
entry_voltagem_cadastro_ferramenta.place(x=125, y=220)

    # Campo do Tamanho da ferramenta
label_tamanho_cadastro_ferramenta = Label(text='TAMANHO', bg=corCinza, fg=corLetra, font=("Verdana 12 bold"))
label_tamanho_cadastro_ferramenta.place(x=500, y=100)
entry_tamanho_cadastro_ferramenta = Entry(janelaCadastroFerramenta, validate='key', validatecommand=(vcmd_tamanho, '%P'), font=("Verdana 9 bold"), bg=corBranca, highlightbackground=corBorda, fg=corLetra, justify="left", width= 40)
entry_tamanho_cadastro_ferramenta.place(x=607, y=100)

    # Campo da Unidade de medida da ferramenta
label_medida_cadastro_ferramenta = Label(text='UNIDADE DE MEDIDA', bg=corCinza, fg=corLetra, font=("Verdana 12 bold"))
label_medida_cadastro_ferramenta.place(x=500, y=140)
entry_medida_cadastro_ferramenta = Entry(janelaCadastroFerramenta, validate='key', validatecommand=(vcmd_medida, '%P'), font=("Verdana 9 bold"), bg=corBranca, highlightbackground=corBorda, fg=corLetra, justify="left", width= 32)
entry_medida_cadastro_ferramenta.place(x=660, y=140)

    # Campo do Tipo da ferramenta
label_tipo_cadastro_ferramenta = Label(text='TIPO', bg=corCinza, fg=corLetra, font=("Verdana 12 bold"))
label_tipo_cadastro_ferramenta.place(x=500, y=180)
entry_tipo_cadastro_ferramenta = Entry(janelaCadastroFerramenta, validate='key', validatecommand=(vcmd_tipo, '%P'), font=("Verdana 9 bold"), bg=corBranca, highlightbackground=corBorda, fg=corLetra, justify="left", width= 40)
entry_tipo_cadastro_ferramenta.place(x=607, y=180)

    # Campo do Material da ferramenta
label_material_cadastro_ferramenta = Label(text='MATERIAL', bg=corCinza, fg=corLetra, font=("Verdana 12 bold"))
label_material_cadastro_ferramenta.place(x=500, y=220)
entry_material_cadastro_ferramenta = Entry(janelaCadastroFerramenta, validate='key', validatecommand=(vcmd_material, '%P'), font=("Verdana 9 bold"), bg=corBranca, highlightbackground=corBorda, fg=corLetra, justify="left", width= 40)
entry_material_cadastro_ferramenta.place(x=607, y=220)


# BOTÕES ###########################################################################################################################################################
    # Botão de voltar
botao_voltar_ferramenta = Button(text='VOLTAR', command=lambda: voltar(), font=("Verdana 9 bold"), highlightbackground=corBorda, fg=corLetra,  height=2, width=15)
botao_voltar_ferramenta.place(x=350, y=300)

    # Botão de confirmação
botao_cadastrar_ferramenta = Button(text='CADASTRAR', command=lambda: cadastrar(), font=("Verdana 9 bold"), highlightbackground=corVerde, fg=corLetra, height=2, width=15)
botao_cadastrar_ferramenta.place(x=530, y=300)


# EXECUÇÃO DA JANELA ##############################################################################################################################################
janelaCadastroFerramenta.mainloop()



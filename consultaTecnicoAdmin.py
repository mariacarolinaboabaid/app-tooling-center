# -*- coding: utf-8 -*-
#  IMPORTES ########################################################################################################################################################
import sqlite3
from bancos import bancoTecnicos, curTecnicos
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import ttk
from tkinter import messagebox

# CORES ############################################################################################################################################################
corPreta = "#2e2d2b"
corBranca = "#feffff"
corVerde = "#8EB897"
corLetra = "#403d3d"
corCinza = "#e9edf5"
corBorda = "#82A0BC"


# FUNÇÕES ##########################################################################################################################################################

#  Erro:
def erro(tree):
    curTecnicos.execute("""SELECT * FROM tabelaTecnicos""")
    resultado = curTecnicos.fetchall()
    for row in resultado:
        tree.insert("", "end", values=row)
    messagebox.showinfo(title="Error", message="Nenhum técnico encontrado.")


# Limpar Busca:
def limparBusca(tree):
    e_nome.delete(0, END)
    e_turno.delete(0, END)
    e_cpf.delete(0, END)
    curFerramentas = bancoTecnicos.cursor()
    curFerramentas.execute("""SELECT * FROM tabelaTecnicos""")
    resultado = curFerramentas.fetchall()
    # Removendo todos os itens da Treeview
    for i in tree.get_children():
        tree.delete(i)
    for row in resultado:
        tree.insert("", "end", values=row)
    return resultado


# Consultar Item
def consultar(tree):
    # Ligando as variáveis com as entradas
    nome = e_nome.get()
    turno = e_turno.get()
    cpf = e_cpf.get()
    # Verificando se as variáveis foram preenchidas
    nomeEntry = False
    turnoEntry = False
    cpfEntry = False
    if nome != "":
        nomeEntry = True
    if turno != "":
        turnoEntry = True
    if cpf != "":
        cpfEntry = True
    # Caso nenhum campo seja preenchido
    if nomeEntry == False and turnoEntry == False and cpfEntry == False:
        messagebox.showinfo(title="Error", message="Ao menos um campo deve ser preenchido.")
    elif cpfEntry == True and cpf.isdigit() == False:
        messagebox.showinfo(title="Error", message="O campo CPF aceita apenas números.")
        e_cpf.delete(0, END)
        # Retornando o resultado
    else:
        # Removendo os dados do Treeview
        for i in tree.get_children():
            tree.delete(i)
        # Caso o Usuário só tenha preenchido o campo NOME
        find = False
        if nomeEntry == True and turnoEntry == False and cpfEntry == False:
            curTecnicos.execute("""SELECT * FROM tabelaTecnicos WHERE nome=?""", [nome])
            resultado = curTecnicos.fetchall()
            for row in range(0, len(resultado)):
                if resultado[row][1] == nome:
                    tree.insert("", "end", values=resultado[row])
                    find = True
            if find == False:
                erro(tabela_dados)
        # Caso o Usuário só tenha preenchido o campo TURNO
        elif nomeEntry == False and turnoEntry == True and cpfEntry == False:
            curTecnicos.execute("""SELECT * FROM tabelaTecnicos WHERE turno=?""", [turno])
            resultado = curTecnicos.fetchall()
            for row in range(0, len(resultado)):
                if resultado[row][3] == turno:
                    tree.insert("", "end", values=resultado[row])
                    find = True
            if find == False:
                erro(tabela_dados)
        # Caso o Usuário só tenha preenchido o campo CPF
        elif nomeEntry == False and turnoEntry == False and cpfEntry == True:
            cpf = int(cpf)
            curTecnicos.execute("""SELECT * FROM tabelaTecnicos WHERE cpf=?""", [cpf])
            resultado = curTecnicos.fetchall()
            for row in range(0, len(resultado)):
                if resultado[row][0] == cpf:
                    tree.insert("", "end", values=resultado[row])
                    find = True
            if find == False:
                # Inserindo dados do banco no Treeview
                erro(tabela_dados)
        # Caso o Usuário tenha preenchido o campo TURNO e CPF
        elif nomeEntry == False and turnoEntry == True and cpfEntry == True:
            cpf = int(cpf)
            curTecnicos.execute("""SELECT * FROM tabelaTecnicos WHERE turno=? and cpf=?""", [turno, cpf])
            resultado = curTecnicos.fetchall()
            for row in range(0, len(resultado)):
                if resultado[row][3] == turno and resultado[row][0] == cpf:
                    tree.insert("", "end", values=resultado[row])
                    find = True
            if find == False:
                erro(tabela_dados)
        # Caso o Usuário tenha preenchido o campo TURNO e NOME
        elif nomeEntry == True and turnoEntry == True and cpfEntry == False:
            curTecnicos.execute("""SELECT * FROM tabelaTecnicos WHERE nome=? and turno=?""", [nome, turno])
            resultado = curTecnicos.fetchall()
            for row in range(0, len(resultado)):
                if resultado[row][1] == nome and resultado[row][3] == turno:
                    tree.insert("", "end", values=resultado[row])
                    find = True
            if find == False:
                erro(tabela_dados)
        # Caso o Usuário tenha preenchido o campo NOME e CPF
        elif nomeEntry == True and turnoEntry == False and cpfEntry == True:
            cpf = int(cpf)
            curTecnicos.execute("""SELECT * FROM tabelaTecnicos WHERE nome=? and cpf=?""", [nome, cpf])
            resultado = curTecnicos.fetchall()
            for row in range(0, len(resultado)):
                if resultado[row][1] == nome and resultado[row][0] == cpf:
                    tree.insert("", "end", values=resultado[row])
                    find = True
            if find == False:
                erro(tabela_dados)
        # Caso o Usuário tenha preenchido o campo NOME, TURNO e CPC
        elif nomeEntry == True and turnoEntry == True and cpfEntry == True:
            cpf = int(cpf)
            curTecnicos.execute("""SELECT * FROM tabelaTecnicos WHERE nome=? and turno=? and cpf=?""",
                                [nome, turno, cpf])
            resultado = curTecnicos.fetchall()
            for row in range(0, len(resultado)):
                if resultado[row][1] == nome and resultado[row][3] == turno and resultado[row][0] == cpf:
                    tree.insert("", "end", values=resultado[row])
                    find = True
            if find == False:
                erro(tabela_dados)


# Deletar
def deletar(tree):
    # Ligando as variáveis com as entradas
    cpf = e_cpf.get()
    # Verificando se as variáveis foram preenchidas
    cpf_entry = False
    if cpf == "":
        messagebox.showinfo(title="Error", message="Campo CPF não preenchido.")
    elif cpf.isdigit() == True:
        cpf = int(cpf)
        cpf_entry = True
    elif cpf.isdigit() == False:
        messagebox.showinfo(title="Error", message="O campo CPF aceita apenas números.")
        e_cpf.delete(0, END)
        # Retorando o resultado
    if cpf_entry == True:
        find = False
        curTecnicos.execute("""SELECT * FROM tabelaTecnicos""")
        resultado = curTecnicos.fetchall()
        for row in range(0, len(resultado)):
            if resultado[row][0] == cpf:
                curTecnicos.execute("""DELETE FROM tabelaTecnicos WHERE cpf=?""", [cpf])
                bancoTecnicos.commit()
                # Deletando as informações do campo
                # Limpeza dos campos
                e_nome.delete(0, END)
                e_turno.delete(0, END)
                e_cpf.delete(0, END)
                # Mensagem de sucesso
                messagebox.showinfo(title="Informação", message="Técnico deletado com sucesso!")
                # Removendo todos os itens da Treeview
                for i in tree.get_children():
                    tree.delete(i)
                # Atualizando itens da treeview conforme banco de dados
                curTecnicos.execute("""SELECT * FROM tabelaTecnicos""")
                resultado = curTecnicos.fetchall()
                for row in resultado:
                    tree.insert("", "end", values=row)
                find = True
                break
        if find == False:
            messagebox.showinfo(title="Error", message="Técnico não encontrado.")


# INTERFACE GRÁFICA  ###############################################################################################################################################
janConsultaTecnico = Tk()
janConsultaTecnico.configure(background=corCinza)
janConsultaTecnico.resizable(width=FALSE, height=FALSE)
janConsultaTecnico.geometry("900x500")
janConsultaTecnico.title("Central de Ferramentaria")
style = ttk.Style(janConsultaTecnico)
style.theme_use("clam")

# Título Consulta Ferramenta
f_title = Frame(master=janConsultaTecnico, width=900, height=60, bg=corBranca, relief=FLAT)
f_title.place(x=0, y=20)
l_title = Label(master=f_title, text="CONSULTA DE TÉCNICOS", bg=corBranca, fg=corLetra, font=("Verdana 18 bold"))
l_title.place(x=300, y=15)

# Campo ID
l_nome = Label(text='NOME', bg=corCinza, fg=corLetra, font=("Verdana 12 bold"))
l_nome.place(x=25, y=120)
e_nome = Entry(font=("Verdana 9 bold"), bg=corBranca, highlightbackground=corBorda, fg=corLetra, justify="left",
               width=40)
e_nome.place(x=90, y=120)

# Campo Tipo
l_turno = Label(text='TURNO', bg=corCinza, fg=corLetra, font=("Verdana 12 bold"))
l_turno.place(x=25, y=160)
e_turno = Entry(font=("Verdana 9 bold"), bg=corBranca, highlightbackground=corBorda, fg=corLetra, justify="left",
                width=40)
e_turno.place(x=90, y=160)

# Campo Fabricante
l_cpf = Label(text='CPF', bg=corCinza, fg=corLetra, font=("Verdana 12 bold"))
l_cpf.place(x=25, y=200)
e_cpf = Entry(font=("Verdana 9 bold"), bg=corBranca, highlightbackground=corBorda, fg=corLetra, justify="left",
              width=40)
e_cpf.place(x=90, y=200)

# TREEVIEW #########################################################################################################################################################
# Frame
f_tabela_dados = Frame(master=janConsultaTecnico, width=900, height=240, bg=corBranca, relief=FLAT)
f_tabela_dados.place(x=0, y=300)

# Adicionando vertical scrollbar na tabela de dados
vertical_scroll = ttk.Scrollbar(master=f_tabela_dados)
vertical_scroll.pack(side=RIGHT, fill=Y)

# Criando a tabela de dados
lista_itens = []
global tabela_dados
itens_head = ["cpf", "nome", "telefone", "turno", "equipe"]

tabela_dados = ttk.Treeview(master=f_tabela_dados,
                            columns=itens_head, show="headings", height=5, yscrollcommand=vertical_scroll.set,
                            selectmode="extended")
style.configure("Treeview", rowheight=31)

# Configurando o tamanho das colunas
tabela_dados.column("cpf", minwidth=1, width=190)
tabela_dados.column("nome", minwidth=1, width=190)
tabela_dados.column("telefone", minwidth=1, width=150)
tabela_dados.column("turno", minwidth=1, width=140)
tabela_dados.column("equipe", minwidth=1, width=135)

# Configurando o heading das colunas
tabela_dados.heading("cpf", text="CPF")
tabela_dados.heading("nome", text="Nome")
tabela_dados.heading("telefone", text="Telefone")
tabela_dados.heading("turno", text="Turno")
tabela_dados.heading("equipe", text="Equipe")

# Inserindo dados do banco no Treeview
curTecnicos.execute("""SELECT * FROM tabelaTecnicos""")
resultado = curTecnicos.fetchall()
for row in resultado:
    tabela_dados.insert("", "end", values=row)
tabela_dados.pack(padx=10)

# Configurando o vertical scrollbar
vertical_scroll.config(command=tabela_dados.yview)

# BOTÕES ###########################################################################################################################################################
# Botão Cancelar
btn_voltar = Button(master=janConsultaTecnico, text="VOLTAR", font=("Verdana 9 bold"), highlightbackground=corBorda,
                    fg=corLetra, height=2, width=15)
btn_voltar.place(x=450, y=127)

# Botão Limpar Busca
btn_limparBuscar = Button(master=janConsultaTecnico, command=lambda: limparBusca(tabela_dados), text="LIMPAR BUSCA",
                          font=("Verdana 9 bold"), highlightbackground="#FFE19C", fg=corLetra, height=2, width=15)
btn_limparBuscar.place(x=450, y=187)

# Botão Deletat
btn_deletar = Button(master=janConsultaTecnico, command=lambda: deletar(tabela_dados), text="DELETAR POR CPF",
                     font=("Verdana 9 bold"), highlightbackground="#FE5F55", fg=corLetra, height=2, width=15)
btn_deletar.place(x=650, y=127)

# Botão Consultar Item Específico
btn_consultar = Button(master=janConsultaTecnico, command=lambda: consultar(tabela_dados), text="CONSULTAR",
                       font=("Verdana 9 bold"), highlightbackground=corVerde, fg=corLetra, height=2, width=15)
btn_consultar.place(x=650, y=187)

# EXECUÇÃO DA JANELA PRINCIPAL #####################################################################################################################################
janConsultaTecnico.mainloop()


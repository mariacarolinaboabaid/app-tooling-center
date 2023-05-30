# -*- coding: utf-8 -*-
#  IMPORTES ########################################################################################################################################################
import sqlite3
from bancos import bancoFerramentas, curFerramentas
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
    curFerramentas.execute("""SELECT * FROM tabelaFerramentas""")
    resultado = curFerramentas.fetchall()
    for row in resultado:
        tree.insert("", "end", values=row)
    messagebox.showinfo(title="Error", message="Nenhuma ferramenta encontrada.")


# Limpar Busca:
def limparBusca(tree):
    e_ID.delete(0, END)
    e_fabricante.delete(0, END)
    e_tipo.delete(0, END)
    curFerramentas = bancoFerramentas.cursor()
    curFerramentas.execute("""SELECT * FROM tabelaFerramentas""")
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
    id = e_ID.get()
    fabricante = e_fabricante.get()
    tipo = e_tipo.get()
    # Verificando se as variáveis foram preenchidas
    idEntry = False
    fabricanteEntry = False
    tipoEntry = False
    if id != "" and id.isdigit() == True:
        id = int(id)
        idEntry = True
    if fabricante != "":
        fabricanteEntry = True
    if tipo != "":
        tipoEntry = True
    # Caso nenhum campo seja preenchido
    if idEntry == False and fabricanteEntry == False and tipoEntry == False:
        messagebox.showinfo(title="Error", message="Ao menos um campo deve ser preenchido.")
    # Retornando o resultado
    else:
        # Removendo os dados do Treeview
        for i in tree.get_children():
            tree.delete(i)
        # Caso o Usuário tenha preenchido o campo ID
        find = False
        if idEntry == True:
            curFerramentas.execute("""SELECT * FROM tabelaFerramentas WHERE id=?""", [id])
            resultado = curFerramentas.fetchall()
            for row in range(0, len(resultado)):
                if resultado[row][0] == int(id):
                    tree.insert("", "end", values=resultado[row])
                    find = True
            if find == False:
                erro(tabela_dados)
        # Caso o Usuário só tenha preenchido o campo FABRICANTE
        elif idEntry == False and fabricanteEntry == True and tipoEntry == False:
            curFerramentas.execute("""SELECT * FROM tabelaFerramentas WHERE fabricante=?""", [fabricante])
            resultado = curFerramentas.fetchall()
            for row in range(0, len(resultado)):
                if resultado[row][2] == fabricante:
                    tree.insert("", "end", values=resultado[row])
                    find = True
            if find == False:
                erro(tabela_dados)
        # Caso o Usuário só tenha preenchido o campo TIPO
        elif idEntry == False and fabricanteEntry == False and tipoEntry == True:
            curFerramentas.execute("""SELECT * FROM tabelaFerramentas WHERE tipo=?""", [tipo])
            resultado = curFerramentas.fetchall()
            for row in range(0, len(resultado)):
                if resultado[row][7] == tipo:
                    tree.insert("", "end", values=resultado[row])
                    find = True
            if find == False:
                # Inserindo dados do banco no Treeview
                erro(tabela_dados)
        # Caso o Usuário tenha preenchido o campo TIPO e FABRICANTE
        elif idEntry == False and fabricanteEntry == True and tipoEntry == True:
            curFerramentas.execute("""SELECT * FROM tabelaFerramentas WHERE tipo=? and fabricante=?""",
                                   [tipo, fabricante])
            resultado = curFerramentas.fetchall()
            for row in range(0, len(resultado)):
                if resultado[row][7] == tipo and resultado[row][2] == fabricante:
                    tree.insert("", "end", values=resultado[row])
                    find = True
            if find == False:
                erro(tabela_dados)


# Deletar
def deletar(tree):
    # Ligando as variáveis com as entradas
    id = e_ID.get()
    # Verificando se as variáveis foram preenchidas
    idEntry = False
    if id == "":
        messagebox.showinfo(title="Error", message="Campo ID não preenchido.")
    elif id.isdigit() == True:
        id = int(id)
        idEntry = True
    elif id.isdigit() == False:
        messagebox.showinfo(title="Error", message="O campo ID aceita apenas números.")
        e_ID.delete(0, END)
        # Retorando o resultado
    if idEntry == True:
        find = False
        curFerramentas.execute("""SELECT * FROM tabelaFerramentas""")
        resultado = curFerramentas.fetchall()
        for row in range(0, len(resultado)):
            if resultado[row][0] == id:
                curFerramentas.execute("""DELETE FROM tabelaFerramentas WHERE id=?""", [id])
                bancoFerramentas.commit()
                # Deletando as informações do campo
                e_ID.delete(0, END)
                e_fabricante.delete(0, END)
                e_tipo.delete(0, END)
                # Mensagem de sucesso
                messagebox.showinfo(title="Informação", message="Ferramenta deletada com sucesso!")
                # Removendo todos os itens da Treeview
                for i in tree.get_children():
                    tree.delete(i)
                # Atualizando itens da treeview conforme banco de dados
                curFerramentas.execute("""SELECT * FROM tabelaFerramentas""")
                resultado = curFerramentas.fetchall()
                for row in resultado:
                    tree.insert("", "end", values=row)
                find = True
                break
        if find == False:
            messagebox.showinfo(title="Error", message="Ferramenta não encontrada.")


# INTERFACE GRÁFICA  ###############################################################################################################################################
janConsultaFerramenta = Tk()
janConsultaFerramenta.configure(background=corCinza)
janConsultaFerramenta.title("Central de Ferramentaria")
janConsultaFerramenta.resizable(width=FALSE, height=FALSE)
janConsultaFerramenta.geometry("1200x500")
style = ttk.Style(janConsultaFerramenta)
style.theme_use("clam")

# Título Consulta Ferramenta
f_title = Frame(master=janConsultaFerramenta, width=1200, height=60, bg=corBranca, relief=FLAT)
f_title.place(x=0, y=20)
l_title = Label(master=f_title, text="CONSULTA DE FERRAMENTAS", bg=corBranca, fg=corLetra, font=("Verdana 18 bold"))
l_title.place(x=450, y=15)

# Campo ID
l_ID = Label(text='ID', bg=corCinza, fg=corLetra, font=("Verdana 12 bold"))
l_ID.place(x=25, y=120)
e_ID = Entry(font=("Verdana 9 bold"), bg=corBranca, highlightbackground=corBorda, fg=corLetra, justify="left", width=44)
e_ID.place(x=55, y=120)

# Campo Tipo
l_tipo = Label(text='TIPO', bg=corCinza, fg=corLetra, font=("Verdana 12 bold"))
l_tipo.place(x=25, y=160)
e_tipo = Entry(font=("Verdana 9 bold"), bg=corBranca, highlightbackground=corBorda, fg=corLetra, justify="left",
               width=41)
e_tipo.place(x=75, y=160)

# Campo Fabricante
l_fabricante = Label(text='FABRICANTE', bg=corCinza, fg=corLetra, font=("Verdana 12 bold"))
l_fabricante.place(x=25, y=200)
e_fabricante = Entry(font=("Verdana 9 bold"), bg=corBranca, highlightbackground=corBorda, fg=corLetra, justify="left",
                     width=35)
e_fabricante.place(x=120, y=200)

# TREEVIEW #########################################################################################################################################################
# Frame
f_tabela_dados = Frame(master=janConsultaFerramenta, width=900, height=240, bg=corBranca, relief=FLAT)
f_tabela_dados.place(x=0, y=300)

# Adicionando vertical scrollbar na tabela de dados
vertical_scroll = ttk.Scrollbar(master=f_tabela_dados)
vertical_scroll.pack(side=RIGHT, fill=Y)

# Criando a tabela de dados
lista_itens = []
global tabela_dados
itens_head = ["id", "descr", "fabricante", "voltagem", "partNumber", "tamanho", "unidadeMedida", "tipo", "material"]

tabela_dados = ttk.Treeview(master=f_tabela_dados,
                            columns=itens_head, show="headings", height=5, yscrollcommand=vertical_scroll.set,
                            selectmode="extended")
style.configure("Treeview", rowheight=31)

# Configurando o tamanho das colunas
tabela_dados.column("id", minwidth=1, width=50)
tabela_dados.column("descr", minwidth=1, width=190)
tabela_dados.column("fabricante", minwidth=1, width=150)
tabela_dados.column("voltagem", minwidth=1, width=140)
tabela_dados.column("partNumber", minwidth=1, width=135)
tabela_dados.column("tamanho", minwidth=1, width=120)
tabela_dados.column("unidadeMedida", minwidth=1, width=120)
tabela_dados.column("tipo", minwidth=1, width=120)
tabela_dados.column("material", minwidth=1, width=120)
tabela_dados.column("material", minwidth=1, width=120)

# Configurando o heading das colunas
tabela_dados.heading("id", text="ID")
tabela_dados.heading("descr", text="Descrição")
tabela_dados.heading("fabricante", text="Fabricante")
tabela_dados.heading("voltagem", text="Voltagem")
tabela_dados.heading("partNumber", text="Part Number")
tabela_dados.heading("tamanho", text="Tamanho")
tabela_dados.heading("unidadeMedida", text="Unid. Medida")
tabela_dados.heading("tipo", text="Tipo")
tabela_dados.heading("material", text="Material")

# Inserindo dados do banco no Treeview
curFerramentas.execute("""SELECT * FROM tabelaFerramentas""")
resultado = curFerramentas.fetchall()
for row in resultado:
    tabela_dados.insert("", "end", values=row)
tabela_dados.pack(padx=10)

# Configurando o vertical scrollbar
vertical_scroll.config(command=tabela_dados.yview)

# BOTÕES ###########################################################################################################################################################
# Botão Cancelar
btn_voltar = Button(master=janConsultaFerramenta, text="VOLTAR", font=("Verdana 9 bold"), highlightbackground=corBorda,
                    fg=corLetra, height=2, width=15)
btn_voltar.place(x=600, y=130)

# Botão Limpar Busca
btn_limparBuscar = Button(master=janConsultaFerramenta, command=lambda: limparBusca(tabela_dados), text="LIMPAR BUSCA",
                          font=("Verdana 9 bold"), highlightbackground="#FFE19C", fg=corLetra, height=2, width=15)
btn_limparBuscar.place(x=600, y=190)

# Botão Consultar Item Específico
btn_consultar = Button(master=janConsultaFerramenta, command=lambda: consultar(tabela_dados), text="CONSULTAR",
                       font=("Verdana 9 bold"), highlightbackground=corVerde, fg=corLetra, height=2, width=15)
btn_consultar.place(x=780, y=130)

# Botão Deletar
btn_deletar = Button(master=janConsultaFerramenta, command=lambda: deletar(tabela_dados), text="DELETAR POR ID",
                     font=("Verdana 9 bold"), highlightbackground="#FE5F55", fg=corLetra, height=2, width=15)
btn_deletar.place(x=780, y=190)

# EXECUÇÃO DA JANELA PRINCIPAL #####################################################################################################################################
janConsultaFerramenta.mainloop()
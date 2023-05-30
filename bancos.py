# -*- coding: utf-8 -*-
#  IMPORTES #################################################################################################################################
import sqlite3

# BANCO DE DADOS DOS USUÁRIOS ###############################################################################################################
    # Nome do banco
bancoUsuarios = sqlite3.connect("usuariosDados.db")
curUsuarios = bancoUsuarios.cursor()
    # Tabela
curUsuarios.execute("""CREATE TABLE IF NOT EXISTS tabelaUsuarios
(usuario TEXT, 
senha INTEGER, 
administrador TEXT) """)



# BANCO DE DADOS DOS TÉCNICOS #############################################################################################################################################
    # Nome do banco
bancoTecnicos = sqlite3.connect("tecnicosDados.db")
curTecnicos = bancoTecnicos.cursor()
    # Tabela
curTecnicos.execute("""CREATE TABLE IF NOT EXISTS tabelaTecnicos
(cpf INTEGER, 
nome TEXT, 
telefone INTEGER, 
turno TEXT, 
equipe TEXT) """)


# BANCO DE DADOS DAS FERRAMENTAS ###########################################################################################################
    # Nome do banco
bancoFerramentas = sqlite3.connect("ferramentasDados.db")
curFerramentas = bancoFerramentas.cursor()
    # Tabela
curFerramentas.execute("""CREATE TABLE IF NOT EXISTS tabelaFerramentas
(id INTEGER PRIMARY KEY AUTOINCREMENT,
descr TEXT,
fabricante TEXT,
voltagem TEXT,
partNumber INTEGER,
tamanho INTEGER,
unidadeMedida TEXT,
tipo TEXT,
material TEXT) """)


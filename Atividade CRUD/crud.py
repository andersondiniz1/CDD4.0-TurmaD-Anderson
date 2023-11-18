# ///////////////////////////////////////////////////////////////////////////
# //         PROJETO - CADASTRO ACADEMIA | crud.py - Biblioteca            //
# ///////////////////////////////////////////////////////////////////////////
# // Registro de Alterações:                                               //
# // 18/11/2023 | Criação inicial do script.                               //
# // 00/00/0000 |                                                          //
# // 00/00/0000 |                                                          //
# // 00/00/0000 |                                                          //
# ///////////////////////////////////////////////////////////////////////////
# // Desenvolvedores:  Anderson Celso Menzes Diniz Ribeiro                 //
# //                   Kelvyn Luiz Peixoto de Freitas                      //
# //                                                                       //
# //                                                                       //
# ///////////////////////////////////////////////////////////////////////////

import sqlite3

# |\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\|
# | 19 - INICIO | 139 - FIM | Criação tabelas e inserção de dados.  |
# |\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\|

def criar_e_inserir_aluno():
    banco = sqlite3.connect('banco_alunos.db')

    criar_tabela_alunos = '''
        CREATE TABLE IF NOT EXISTS alunos (
            matricula INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cpf TEXT NOT NULL,
            telefone TEXT,
            email TEXT,
            endereco TEXT NOT NULL
        );
    '''
    banco.execute(criar_tabela_alunos)

    nome = input("Digite o nome do aluno: ")
    cpf = input("Digite o CPF do aluno: ")
    telefone = input("Digite o telefone do aluno: ")
    email = input("Digite o email do aluno: ")
    endereco = input("Digite o endereço do aluno: ")

    inserir_dados_alunos = f'''
        INSERT INTO alunos (nome, cpf, telefone, email, endereco) VALUES
        ('{nome}', '{cpf}', '{telefone}', '{email}', '{endereco}');
    '''
    banco.execute(inserir_dados_alunos)

    banco.commit()
    banco.close()
    print("Dados inseridos com sucesso!")


def criar_e_inserir_modalidade():
    banco = sqlite3.connect('banco_alunos.db')

    criar_tabela_modalidades = '''
        CREATE TABLE IF NOT EXISTS modalidades (
            id_mod INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT
        );
    '''
    banco.execute(criar_tabela_modalidades)

    nome_modalidade = input("Digite o nome da modalidade: ")

    inserir_dados_modalidades = f'''
        INSERT INTO modalidades (nome) VALUES
        ('{nome_modalidade}');
    '''
    banco.execute(inserir_dados_modalidades)

    banco.commit()
    banco.close()
    print("Dados inseridos com sucesso!")

def criar_e_inserir_personal():
    banco = sqlite3.connect('banco_alunos.db')

    criar_tabela_personal = '''
        CREATE TABLE IF NOT EXISTS personal (
            cpf TEXT NOT NULL,
            cref INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            nome TEXT NOT NULL,
            telefone TEXT NOT NULL,
            email TEXT NOT NULL
        );
    '''
    banco.execute(criar_tabela_personal)

    cpf_personal = input("Digite o CPF do personal: ")
    nome_personal = input("Digite o nome do personal: ")
    telefone_personal = input("Digite o telefone do personal: ")
    email_personal = input("Digite o email do personal: ")

    inserir_dados_personal = f'''
        INSERT INTO personal (cpf, nome, telefone, email) VALUES
        ('{cpf_personal}', '{nome_personal}', '{telefone_personal}', '{email_personal}');
    '''
    banco.execute(inserir_dados_personal)

    banco.commit()
    banco.close()
    print("Dados inseridos com sucesso!")

def criar_e_inserir_funcionario():
    banco = sqlite3.connect('banco_alunos.db')

    criar_tabela_funcionario = '''
        CREATE TABLE IF NOT EXISTS funcionario (
            id_funcionario INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cpf TEXT NOT NULL,
            departamento INTEGER NOT NULL,
            cpf_supervisor TEXT NOT NULL,
            salario DECIMAL(8,2)
        );
    '''
    banco.execute(criar_tabela_funcionario)

    nome_funcionario = input("Digite o nome do funcionário: ")
    cpf_funcionario = input("Digite o CPF do funcionário: ")
    departamento = int(input("Digite o departamento do funcionário: "))
    cpf_supervisor = input("Digite o CPF do supervisor: ")
    salario = float(input("Digite o salário do funcionário: "))

    inserir_dados_funcionario = f'''
        INSERT INTO funcionario (nome, cpf, departamento, cpf_supervisor, salario) VALUES
        ('{nome_funcionario}', '{cpf_funcionario}', {departamento}, '{cpf_supervisor}', {salario});
    '''
    banco.execute(inserir_dados_funcionario)

    banco.commit()
    banco.close()
    print("Dados inseridos com sucesso!")

# |\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\|
# | 19 - INICIO | 139 - FIM | Criação tabelas e inserção de dados.  |
# |\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\|


# |\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\|
# | 142 - INICIO | 171 - FIM | Acessar contas existentes.           |
# |\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\|

def acessar_conta():

    # Conectar ao banco de dados
    banco = sqlite3.connect('banco_alunos.db')

    # Commit para salvar as alterações
    # banco.commit()

    # Consultar dados (Read)
    meucursor = banco.cursor()
    pesquisa = "SELECT matricula, nome, CPF, telefone FROM alunos;"
    meucursor.execute(pesquisa)
    resultado = meucursor.fetchall()

    # Exibir resultados
    for linha in resultado:
        print("======================")
        print("Matrícula:", linha[0])
        print("Nome:", linha[1])
        print("CPF:", linha[2])
        print("Telefone:", linha[3])
        print("======================\n")

# |\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\|
# | 142 - INICIO | 171 - FIM | Acessar contas existentes.           |
# |\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\|

# |\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\|
# | 173 - INICIO | 186 - FIM | Fechar conexão com o banco de dados. |
# |\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\|

def sair_banco():
    # Conectar ao banco de dados
    banco = sqlite3.connect('banco_alunos.db')

    # Fechar a conexão com o banco de dados
    banco.close()

# |\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\|
# | 173 - INICIO | 186 - FIM | Fechar conexão com o banco de dados. |
# |\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\|

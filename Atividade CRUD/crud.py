import sqlite3

# Função para inserir dados
def inserir_aluno():

    # Conectar ao banco de dados (ou criar se não existir)
    banco = sqlite3.connect('banco_alunos.db')

    # Criar tabela se não existir
    criar_tabela = '''
        CREATE TABLE IF NOT EXISTS alunos (
            matricula INTEGER PRIMARY KEY,
            nome TEXT,
            CPF TEXT,
            telefone TEXT
        );
    '''
    banco.execute(criar_tabela)

    matricula = int(input("Digite a matrícula do aluno: "))
    nome = input("Digite o nome do aluno: ")
    cpf = input("Digite o CPF do aluno: ")
    telefone = input("Digite o telefone do aluno: ")

    # Inserir dados (Create)
    inserir_dados = f'''
        INSERT INTO alunos (matricula, nome, CPF, telefone) VALUES
        ({matricula}, '{nome}', '{cpf}', '{telefone}');
    '''
    banco.execute(inserir_dados)
    banco.commit()
    print("Dados inseridos com sucesso!")


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

def sair_banco():
    # Conectar ao banco de dados
    banco = sqlite3.connect('banco_alunos.db')

    # Fechar a conexão com o banco de dados
    banco.close()

import sqlite3

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

# Inserir dados (Create)
inserir_dados = '''
    INSERT INTO alunos (matricula, nome, CPF, telefone) VALUES
    (1, 'Fulano', '123.456.789-01', '(11) 1234-5678'),
    (2, 'Ciclano', '987.654.321-09', '(22) 9876-5432');
'''
banco.execute(inserir_dados)

# Commit para salvar as alterações
banco.commit()

# Consultar dados (Read)
meucursor = banco.cursor()
pesquisa = "SELECT matricula, nome, CPF, telefone FROM alunos;"
meucursor.execute(pesquisa)
resultado = meucursor.fetchall()

# Exibir resultados
for linha in resultado:
    print("Matrícula:", linha[0])
    print("Nome:", linha[1])
    print("CPF:", linha[2])
    print("Telefone:", linha[3])
    print()

# Fechar a conexão com o banco de dados
banco.close()

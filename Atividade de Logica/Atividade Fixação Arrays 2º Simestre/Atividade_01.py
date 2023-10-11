# Perguntar ao usuário quantos alunos tem na sala e criar um array, unidimensional (Vetor) com o nome de todos os alunos da sala:
# python "/workspaces/CDD4.0-TurmaD-Anderson/Atividade de Logica/Atividade Fixação Arrays 2º Simestre/Atividade_01.py"

from Biblioteca import cadastro_alunos

print("========================\n"
      "1. Cadastro de alunos\n"
      "2. Outra opção (caso exista)\n"
      "0. Sair\n"
      "========================\n")

ops = input("\nEscolha uma opção: ")

while ops not in ["1", "2", "0"]:
    ops = input("\nErro - Escolha uma opção (entre 1, 2 ou 0): ")

if ops == "1":
    cadastro_alunos()

#elif ops == 2:


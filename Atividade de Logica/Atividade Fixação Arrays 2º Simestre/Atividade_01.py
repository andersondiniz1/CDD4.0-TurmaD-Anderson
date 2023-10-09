# Perguntar ao usuário quantos alunos tem na sala e criar um array, unidimensional (Vetor) com o nome de todos os alunos da sala:

ArrayAlunos = []
alunos = int(input("Quantidade de alunos? "))

for i in range(alunos):
    nome = input(f"Digite o nome do {i+1}º aluno: ")
    ArrayAlunos.append(nome)

print("Nomes dos alunos na sala:")
for nome in ArrayAlunos:
    print(nome)

# ========================================================================================================== #
# INICIO - Perguntar ao usuário quantos alunos tem na sala e criar um array, unidimensional (Vetor) com o nome de todos os alunos da sala
def cadastro_alunos():

    verificador = "s"
    while verificador == "s" or verificador == "S":
        print("========================\n"
              "1. Cadastrar alunos\n"
              "2. Imprimir nomes dos alunos\n"
              "0. Sair\n"
              "========================\n")
        
        ops = int(input("\nEscolha uma opção: "))
        while ops != 1 and ops != 2 and ops != 0:
            ops = int(input("\nErro - Escolha uma opção (entre 1, 2, 3 ou 0): "))
        print("")

        if ops == 1:

            alunos = int(input("Qual a quantidade de alunos? "))

            ArrayAlunos = []

            for i in range(alunos):
                nome = input(f"Digite o nome do {i+1}º aluno: ") 
                ArrayAlunos.append(nome)

        if ops == 2:

            print("Nomes dos alunos na sala:")
            for i, nome in range(alunos):
                print(f"{i}º. {nome}")

            enterruptor = ("Digite qualquer letra para contunuar... ")
        
        if ops == 0:  
            break
print("Encerrando o programa...")

# FIM - Perguntar ao usuário quantos alunos tem na sala e criar um array, unidimensional (Vetor) com o nome de todos os alunos da sala
# ========================================================================================================== #

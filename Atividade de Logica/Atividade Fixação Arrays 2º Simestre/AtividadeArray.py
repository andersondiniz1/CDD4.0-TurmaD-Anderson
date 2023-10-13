from Biblioteca import *

verificador = "s"
while verificador in "sS":

    # Atividades de Array: 1º á 13º
    print("\n\n========================================================\n"
    "1  - Cadastro de Alunos               (1º, 2º e 3º questão)\n"
    "2  - Calcular a Média                 (4º questão)\n"
    "3  - Multiplicação de Vetor           (5º questão)\n"
    "4  - Nuemros ao Inverso               (6º e 7ºquestão)\n"
    "5  - Cadastro e Logim de Usuarios     (8º e 9º questão)\n"
    "6  - Somar Numeros em Vetor           (10º questão)\n"
    "7  - Contar Numeros em Vetor          (11º questão)\n"
    "8  - Nomes em Reverso                 (12º questão)\n"
    "9  -   (13º questão)\n"
    "========================================================\n"
    "0 - Encerrar Programa\n"
    "========================================================\n")
    ops = input("\nEscolha uma opção: ")
    while ops not in "1234567890":
        ops = input("Opção invalida, tente novamente...\n"
                    "Escolha uma opção acima: ")

    if ops == "1":
        cadastro_alunos()

    elif ops == "2":
        calcular_media()

    elif ops == "3":
        calcular_AXM()

    elif ops == "4":
        inverso()

    elif ops == "5":
        cadastro_usuarios()
    
    elif ops == "6":
        soma_vetor()

    elif ops == "7":
        contagem()

    elif ops == "8":
        reverso()

    elif ops == "9":
        verificador30numeros()

    elif ops == "0":
        verificador == "n"
        print("Finalizando o programa...")

    else:
        print("\nOpção invalida, tente novamente...\n")
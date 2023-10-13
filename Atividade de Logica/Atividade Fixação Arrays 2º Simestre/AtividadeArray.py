from Biblioteca import *

verificador = "s"
while verificador in "sS":

    print("\n\n========================================================\n"
    "1  - Cadastro de Alunos               (1º, 2º e 3º questão)\n"
    "2  - Calcular a Média                 (4º questão)\n"
    "3  - Multiplicação de Vetor           (5º questão)\n"
    "4  - Nuemros ao Inverso               (6º e 7ºquestão)\n"
    "5  - Cadastro e Logim de Usuarios     (8º e 9º questão)\n"
    "6  - Soma de Vetores                  (10º questão)\n"
    "7  -  (11º questão)\n"
    "8  -   (12º questão)\n"
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

    if ops == "2":
        calcular_media()

    if ops == "3":
        calcular_AXM()

    if ops == "4":
        inverso()

    if ops == "5":
        cadastro_usuarios()
    
    if ops == "6":
        soma_vetor()
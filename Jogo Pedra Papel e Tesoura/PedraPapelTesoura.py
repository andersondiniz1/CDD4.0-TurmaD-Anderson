
jogador1 = input("Digite o nome do 1º jogador: ")
jogador2 = input("Digite o nome do 2º jogador: ")

verificador = "s"
while verificador == "s" or verificador == "S": 

    print("==========================\n"
         f" {jogador1} X {jogador2}  \n"
          "==========================\n"
          "= 1 - Jogar              =\n"
          "= 2 - Trocar nomes       =\n"
          "==========================\n"
          "= 0 - Encerrar Programa  =\n"
          "==========================\n")
    ops = int(input("\nEscolha uma opção: "))
    while ops != 1 and ops != 2 and ops != 0:
        ops = int(input("\nEscolha uma opção: "))
    print("")

    if ops == 2:
        print("=========================\n"
              "1 - Trocar nome do jogador 1 \n"
              "2 - Trocar nome do jogador 2 \n"
              "=========================\n"
              "0 - Voltar 2 \n"
              "=========================\n")
        ops2 = int(input("\nEscolha uma opção: "))
        while ops2 != 1 and ops2 != 2 and ops2 != 0:
            ops2 = int(input("\nEscolha uma opção: "))

        if ops2 == 1:
            jogador1 = input("Digite o nome do 1º jogador: ")
        else:
            jogador2 = input("Digite o nome do 2º jogador: ")
    
    elif ops == 1:
        primeiro = int(input("Quem sera o primeiro jogador? (1 ou 2) \n"))
        while primeiro != 1 and primeiro != 2:
            primeiro = int(input("Erro - Escolha 1 para o primeiro jogador ou 2 para o segundo jogador: (1 ou 2) \n"))

        opc1 = "a"
        opc2 = "b"

        if primeiro == 1:
            opc1 = input(f"Jogador {jogador1} escolha entre: pedra, papel ou tesoura: ")
            while opc1 != "pedra" and opc1 != "papel" and opc1 != "tesoura":
                opc1 = input(f"Erro - Jogador {jogador1} escolha somente entre: pedra, papel ou tesoura: ")

            opc2 = input(f"Jogador {jogador2} escolha entre: pedra, papel ou tesoura: ")
            while opc2 != "pedra" and opc2 != "papel" and opc2 != "tesoura":
                opc2 = input(f"Erro - Jogador {jogador2} escolha somente entre: pedra, papel ou tesoura: ")

        else:
            opc2 = input(f"Jogador {jogador2} escolha entre: pedra, papel ou tesoura: ")
            while opc2 != "pedra" and opc2 != "papel" and opc2 != "tesoura":
                opc2 = input(f"Erro - Jogador {jogador2} escolha somente entre: pedra, papel ou tesoura: ")

            opc1 = input(f"Jogador {jogador1} escolha entre: pedra, papel ou tesoura: ")
            while opc1 != "pedra" and opc1 != "papel" and opc1 != "tesoura":
                opc1 = input(f"Erro - Jogador {jogador1} escolha somente entre: pedra, papel ou tesoura: ")


        if opc1 == opc2:
            print(f"Empate, jogador {jogador1} escolheu {opc1} e jogador {jogador2} escolheu {opc2}.")
        elif (opc1 == "pedra" and opc2 == "tesoura") or (opc1 == "papel" and opc2 == "pedra") or (opc1 == "tesoura" and opc2 == "papel"):
            print(f"Jogador {jogador1} venceu, {opc1} ganha de {opc2}.")
        else:
            print(f"Jogador {jogador2} venceu, {opc2} ganha de {opc1}.")

        saveJogador1 = jogador1
        saveJogador2 = jogador2

        verificador = input("\nDeseja jogar novamente? (s/n)\n")
        while verificador != "n" and verificador != "N" and verificador != "s" and verificador != "S":
            verificador = input("Opção inválida, tente novamente...\n"
         
                                "Deseja jogar novamente? (s/n)")
    else:
        print("\n Encerrando o jogo...")
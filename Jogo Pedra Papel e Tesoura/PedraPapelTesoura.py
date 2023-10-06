# Variaveis de jogadores e placar
jogador1 = input("Digite o nome do 1º jogador: ")
jogador2 = input("Digite o nome do 2º jogador: ")
placar1 = 0
placar2 = 0

# Quantidade de partidas
quantidade = int(input("Melhor de quantas? (Escolha um numero impar): "))
while quantidade % 2 == 0:
    quantidade = int(input("Erro - Quantidade de partidas dever ser um numero impar. (Escolha um numero impar): "))

# verificador se deseja jogar novamente
verificador = "s"
while verificador == "s" or verificador == "S": 

    print("==========================\n"
         f" {jogador1} X {jogador2}  \n"
         f" {placar1} placar {placar2}  \n"
         f" Melhor de {quantidade}  \n"
          "==========================\n"
          "= 1 - Jogar              =\n"
          "= 2 - Trocar nomes       =\n"
          "= 3 - Melhor de quantas  =\n"
          "==========================\n"
          "= 0 - Encerrar Programa  =\n"
          "==========================\n")
    ops = int(input("\nEscolha uma opção: "))
    while ops != 1 and ops != 2 and ops != 3 and ops != 0:
        ops = int(input("\nErro - Escolha uma opção (entre 1, 2, 3 ou 0): "))
    print("")

    if ops == 3:
        # Quantidade de partidas
        quantidade = int(input("Melhor de quantas? (Escolha um numero impar): "))
        while quantidade % 2 == 0:
            quantidade = int(input("Erro - Quantidade de partidas dever ser um numero impar. (Escolha um numero impar): "))

    # Trocar nomes
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
    
    # Jogar
    elif ops == 1:
        # Escolher quem sera o primeiro jogador
        primeiro = int(input("Quem sera o primeiro jogador? (1 ou 2) \n"))
        while primeiro != 1 and primeiro != 2:
            primeiro = int(input("Erro - Escolha 1 para o primeiro jogador ou 2 para o segundo jogador: (1 ou 2) \n"))

        # Variavel ed seleção das opções dos jogadores, quantidade de jogos e placar
        opc1 = "varivel de opção do jogador 1"
        opc2 = "varivel de opção do jogador 2"
        quantidade1 = quantidade # Para não alterar a quantidade de jogos original
        placar1 = 0
        placar2 = 0

        while quantidade1 != 0:
            # Primeiro jogador selecionado anteriormente escolhe entre pedra, papel ou tesoura
            if primeiro == 1:
                opc1 = input(f"\nJogador {jogador1} escolha entre: pedra, papel ou tesoura: ")
                while opc1 != "pedra" and opc1 != "papel" and opc1 != "tesoura":
                    opc1 = input(f"\nErro - Jogador {jogador1} escolha somente entre: pedra, papel ou tesoura: ")

                opc2 = input(f"\nJogador {jogador2} escolha entre: pedra, papel ou tesoura: ")
                while opc2 != "pedra" and opc2 != "papel" and opc2 != "tesoura":
                    opc2 = input(f"\nErro - Jogador {jogador2} escolha somente entre: pedra, papel ou tesoura: ")

            # Segundo jogador escolhe entre pedra, papel ou tesoura
            else:
                opc2 = input(f"\nJogador {jogador2} escolha entre: pedra, papel ou tesoura: ")
                while opc2 != "pedra" and opc2 != "papel" and opc2 != "tesoura":
                    opc2 = input(f"\nErro - Jogador {jogador2} escolha somente entre: pedra, papel ou tesoura: ")

                opc1 = input(f"\nJogador {jogador1} escolha entre: pedra, papel ou tesoura: ")
                while opc1 != "pedra" and opc1 != "papel" and opc1 != "tesoura":
                    opc1 = input(f"\nErro - Jogador {jogador1} escolha somente entre: pedra, papel ou tesoura: ")

            # Condição de vitoria, empate e derrota
            if opc1 == opc2:
                print(f"\nEmpate, jogador {jogador1} escolheu {opc1} e jogador {jogador2} escolheu {opc2}.")
                quantidade1 -= quantidade1
            elif (opc1 == "pedra" and opc2 == "tesoura") or (opc1 == "papel" and opc2 == "pedra") or (opc1 == "tesoura" and opc2 == "papel"):
                quantidade1 -= 1
                print(f"\nJogador {jogador1} venceu, {opc1} ganha de {opc2}.\n"
                      f"Jogos restantes: {quantidade1}")
                placar1 += 1
                
            else:
                quantidade1 -= 1
                print(f"\nJogador {jogador2} venceu, {opc2} ganha de {opc1} \n."
                      f"Jogos restantes: {quantidade1}")
                placar2 += 1           

            print("\n==========================\n"
                 f" {jogador1} X {jogador2}  \n"
                 f" {placar1} placar {placar2}\n"
                 f" Melhor de {quantidade}  \n"
                 f"Jogos restantes: {quantidade1}\n"
                 "==========================\n")
            
            if placar1 > placar2:
                print(f"O jogador {jogador1} ganhou de {placar1} a {placar2}")
            elif placar2 > placar1:
                print(f"O jogador {jogador2} ganhou de {placar2} a {placar1}")
            else:
                print(f"Empate entre o jogador {jogador1} e {jogador2} com placar de {placar1} a {placar2}")


        # verificador se deseja jogar novamente
        verificador = input("\nDeseja jogar novamente? (s/n)\n")
        while verificador != "n" and verificador != "N" and verificador != "s" and verificador != "S":
            verificador = input("Opção inválida, tente novamente...\n"
                                "Deseja jogar novamente? (s/n)")
        if verificador == "n" and verificador == "N":
            print("\n Encerrando o jogo...")

    # Encerrar programa        
    else:
        print("\n Encerrando o jogo...")
        verificador = "n"
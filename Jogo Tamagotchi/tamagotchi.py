from Biblioteca import Tamagotchi

def main():
    # Digitar o nome do bicho
    nome = input("Nome do seu Tamagotchi: ")
    bichinho = Tamagotchi(nome)

    # Se o bicho estiver vivo, o jogador pode escrever a proxima ação
    while bichinho.esta_vivo():
        print(bichinho.status())
        acao = input("==================\n"
                     "Escolha uma ação:\n"
                     "==================\n"
                     "- Alimentar\n"
                     "- Brincar\n"
                     "- Curar\n"
                     "- Sair\n"
                     "==================\n").lower()

        # Repetição se o jogador escrever errado
        while acao not in ["alimentar", "brincar", "curar", "sair"]:
            print("Ação inválida. Escolha entre alimentar, brincar, curar ou sair.")
            acao = input("==================\n"
                         "Escolha uma ação:\n"
                         "==================\n"
                         "- Alimentar\n"
                         "- Brincar\n"
                         "- Curar\n"
                         "- Sair\n"
                         "==================\n").lower()
            
        # Ecolha do jogador
        if acao == "alimentar":
            bichinho.alimentar()
        elif acao == "brincar":
            bichinho.brincar()
        elif acao == "curar":
            bichinho.curar()
        elif acao == "sair":
            print("========================\n"
                  "Desligando Tamagotchi...\n"
                  "========================\n")
            break

        # A cada rodada acontece isso com o status do bicho
        bichinho.fome += 5
        bichinho.felicidade -= 5
        bichinho.saude -= 5

    # Se o loop "while bichinho.esta_vivo():" ficar false, fica se algum status do bicho passar do limite
    if not bichinho.esta_vivo():
        print("========================\n"
            f"{bichinho.nome} morreu. O jogo acabou, voltando para o menu...\n"
            "========================\n")

# repetição do menu lá embaixo
menu = True

while menu:
    # Menu do jogo
    jogo = input("==================\n"
                "TAMAGOTCHI CDD4.0\n"
                "==================\n"
                "- Jogar\n"
                "- Sair\n"
                "==================\n").lower()
    # Se digitar opção errada
    while jogo not in ["jogar", "sair", "wellington"]:
        jogo = input("==================\n"
                    "TAMAGOTCHI CDD4.0\n"
                    "==================\n"
                    "- Jogar\n"
                    "- Sair\n"
                    "==================\n").lower()
        
    # Condição escolhida pelo jogador
    if jogo == "jogar":
        menu = False
        main()
    elif jogo == "sair":
        print("\nEncerrando o jogo...")
        menu = False
    elif jogo == "wellington":
        print("\n Wellington melhor professor!!! S2")
    else:
        print("Alternativa incorreta...")


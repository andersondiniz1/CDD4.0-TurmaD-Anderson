# 16. Escreva um algoritmo para ler a hora de início e a hora de fim de um jogo de Xadrez (considere apenas horas inteiras, sem os minutos) e calcule a duração do jogo em horas, sabendo-se que o tempo máximo de duração do jogo é de 24 horas e que o jogo pode iniciar em um dia e terminar no dia seguinte

verificador = "s"
while verificador == "s" or verificador == "S": 

    hora_inicio = int(input("Digite a hora de início do jogo: "))
    while hora_inicio <= 0 or hora_inicio > 24:
        hora_inicio = int(input("Digite a hora de início do jogo entre 1 e 24 horas: "))

    hora_fim = int(input("Digite a hora de fim do jogo: "))
    while hora_fim <= 0 or hora_fim > 24:
        hora_fim = int(input("Digite a hora de fim do jogo entre 1 e 24 horas: "))

    duracao = 0
    if hora_inicio == hora_fim:
        duracao = 24 
    elif hora_inicio <= hora_fim:
        duracao = hora_fim - hora_inicio
    else:
        duracao = (24 - hora_inicio) + hora_fim

    print(f"A duração do jogo de xadrez foi de {duracao} horas.")

    verificador = input("\nDeseja fazer um novo calculo? (s/n)\n")
    while verificador != "n" and verificador != "N" and verificador != "s" and verificador != "S":
        verificador = input("Oplção invalida, tente novamente...\n"
                            "Deseja fazer um novo calculo? (s/n)")
print("Encerrando programa...")


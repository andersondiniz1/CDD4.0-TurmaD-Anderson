# 11. Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade dessa pessoa expressa apenas em dias. Considerar ano com 365 dias e mês com 30 dias.

verificador = "s"
while verificador == "s" or verificador == "S":

    idade = int(input("Digite sua idade: "))
    while idade <= 0 or idade > 120:
        idade = int(input("Digite a sua idade entre 1 e 120: "))

    mes_nascimento = int(input("Digite o mês de nascimento: "))
    while mes_nascimento <= 0 or mes_nascimento >= 13:
        mes_nascimento = int(input("Digite o mês de nascimento entre 1 e 12: "))

    dia_nascimento = int(input("Digite o dia de nascimento: "))
    while dia_nascimento <= 0 or dia_nascimento >= 32:
        dia_nascimento = int(input("Digite o dia de nascimento entre 1 e 31: "))

    idade_em_dias = (idade * 365) + (mes_nascimento * 30) + dia_nascimento

    print(f"\nVocê tem: {idade_em_dias} dias de vida.")

    verificador = input("\nDeseja fazer um novo calculo? (s/n)\n")
    while verificador != "n" and verificador != "N" and verificador != "s" and verificador != "S":
        verificador = input("Opção invalida, tente novamente...\n"
                            "Deseja fazer um novo calculo? (s/n)")
            
print("Encerrando programa...")

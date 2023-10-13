# 07. Faça um código que receba o valor da base e da altura de um triângulo e calcule sua área. usando a fórmula A = (base x Altura ) /2
# 13. Escreva um algoritmo para ler as dimensões de um retângulo (base e altura), calcular e escrever a área do retângulo. 

verificador = "s"
while verificador == "s" or verificador == "S":

    print("\n\n============================\n"
        "T - Area do triângulo\n"
        "R - Area do retângulo\n"
        "N - Sair do programa\n"
        "============================\n")
    ops = input("\nEscolha uma opção: \n") 

    if ops == "t" or ops == "T": 

        base = float(input("Digite o valor da base do triangulo: "))
        while base == 0:
            base = float(input("Digite o valor da base do triangulo diferente de 0: "))

        altura = float(input("Digite o valor da altura do triangulo: "))
        while base == 0:
            altura = float(input("Digite o valor da altura do triangulo diferente de 0: "))

        area = (base * altura) / 2
        print(f"A area do triangulo é: {area}.")
        ops = "n"
        verificador = input("\nDeseja fazer um novo calculo? (s/n)\n")
        while verificador != "n" and verificador != "N" and verificador != "s" and verificador != "S":
            verificador = input("Opção invalida, tente novamente...\n"
                                "Deseja fazer um novo calculo? (s/n)")


    elif ops == "r" or ops == "R": 

        base = float(input("Digite o valor da base do retângulo: "))
        while base == 0:
            base = float(input("Digite o valor da base do retângulo diferente de 0: "))

        altura = float(input("Digite o valor da altura do retângulo: "))
        while base == 0:
            altura = float(input("Digite o valor da altura do retângulo diferente de 0: "))

        area = base * altura
        print(f"A area do retângulo é: {area}.")
        ops = "n"
        verificador = input("\nDeseja fazer um novo calculo? (s/n)\n")
        while verificador != "n" and verificador != "N" and verificador != "s" and verificador != "S":
            verificador = input("Opção invalida, tente novamente...\n"
                                "Deseja fazer um novo calculo? (s/n)")
    
    elif ops == "n" or ops == "N": 
        verificador = "n"
    
    else:
        print("\n Opção invalida, tente novamente...")

print("Encerrando programa...")
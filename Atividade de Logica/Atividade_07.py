# Faça um código que receba o valor da base e da altura de um triângulo e calcule sua área. usando a fórmula A = (base x Altura ) /2

verificador = "s"
while verificador == "s" or verificador == "S": 

    base = float(input("Digite o valor da base do triangulo: "))
    while base == 0:
        base = float(input("Digite o valor da base do triangulo diferente de 0: "))

    altura = float(input("Digite o valor da altura do triangulo: "))
    while base == 0:
        altura = float(input("Digite o valor da altura do triangulo diferente de 0: "))

    area = (base * altura) / 2
    print(f"A area do triangulo é: {area}.")

    verificador = input("Deseja fazer uma nova verificação? (s/n)")
print("Encerrando programa...")
# 14. Escreva um algoritmo para ler uma temperatura em graus Fahrenheit, calcular e escrever o valor correspondente em graus Celsius (baseado na fórmula abaixo): C = ((F - 32)/9)*5 Observação: Para testar se a sua resposta está correta saiba que 100 ⍛C = 212 F

verificador = "s"
while verificador == "s" or verificador == "S": 

    fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))

    celsius = ((fahrenheit - 32) / 9) * 5

    print(f"A temperatura em graus Celsius é: {celsius:.2f} °C")

    verificador = input("Deseja fazer um novo calculo? (s/n)")
    while verificador != "n" and verificador != "N" and verificador != "s" and verificador != "S":
        verificador = input("Oplção invalida, tente novamente...\n"
                            "Deseja fazer um novo calculo? (s/n)")
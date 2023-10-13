# 15. Escreva um algoritmo para ler dois valores (considere que não serão lidos valores iguais) e escrevê-los em ordem crescente

verificador = "s"
while verificador == "s" or verificador == "S": 

    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))
    while valor1 == valor2:
        valor2 = float(input("Digite o segundo valor diferente do primeiro: "))

    if valor1 > valor2:
        print(f"Ordem crescente: {valor2}, {valor1}")
    else:
        print(f"Ordem crescente: {valor1}, {valor2}")

    verificador = input("\nDeseja fazer um novo calculo? (s/n)\n")
    while verificador != "n" and verificador != "N" and verificador != "s" and verificador != "S":
        verificador = input("Opção invalida, tente novamente...\n"
                            "Deseja fazer um novo calculo? (s/n)")
print("Encerrando programa...")
# 04. Crie um algoritmo que receba 3 números e informe qual o maior entre eles.

verificador = "s"
while verificador == "s" or verificador == "S": 

    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    numero3 = float(input("Digite o terceiro número: "))

    if numero1 > numero2 and numero1 > numero3:
        print(f"O maior número entre {numero1}, {numero2} e {numero3} é {numero1}.")
    elif numero2 > numero1 and numero2 > numero3:
        print(f"O maior número entre {numero1}, {numero2} e {numero3} é {numero2}.")
    else:
        print(f"O maior número entre {numero1}, {numero2} e {numero3} é {numero3}.")
        
    verificador = input("\nDeseja fazer um novo calculo? (s/n)\n")
    while verificador != "n" and verificador != "N" and verificador != "s" and verificador != "S":
        verificador = input("Opção invalida, tente novamente...\n"
                            "Deseja fazer um novo calculo? (s/n)")
        
print("Encerrando programa...")
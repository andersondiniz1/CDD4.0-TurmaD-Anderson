# 09. Faça um código que receba um número inteiro e mostre o seu antecessor.
# 10. Faça um Algoritmo que receba um número inteiro e mostre o seu sucessor.

verificador = "s"
while verificador == "s" or verificador == "S":

    numero = int(input("\nDigite o numero para verificar seu antecessor ou sucessor: "))

    verificador2 = "s"
    while verificador2 == "s" or verificador2 == "S":
        print("\n\n============================\n"
            "1 - Digitar o número novamente\n"
            "2 - Sucessor do número\n"
            "3 - Antecessor do número\n"
            "0 - Sair do programa\n"
            "============================\n")
        ops = int(input("\nEscolha uma opção: \n"))
        
        if ops == 1:
            numero = int(input("\nDigite o numero para verificar seu antecessor: "))
            verificador = "s"
        elif ops == 2:
            sucessor = numero + 1
            print(f"\nO sucessor do numero {numero} é: {sucessor}\n")
            verificador2 = "n"
            verificador = input("\nDeseja fazer um novo calculo? (s/n)\n")
            while verificador != "n" and verificador != "N" and verificador != "s" and verificador != "S":
                verificador = input("Opção invalida, tente novamente...\n"
                                    "Deseja fazer um novo calculo? (s/n)")
        elif ops == 3:
            antecessor = numero - 1
            print(f"\nO antecessor do numero {numero} é: {antecessor}\n")
            verificador2 = "n"
            verificador = input("\nDeseja fazer um novo calculo? (s/n)\n")
            while verificador != "n" and verificador != "N" and verificador != "s" and verificador != "S":
                verificador = input("Opção invalida, tente novamente...\n"
                                    "Deseja fazer um novo calculo? (s/n)")
        elif ops == 0:
            print("")
            verificador = "n"
            verificador2 = "n"
        else:
            print("\n Opção errada, voltando parao menu... \n")
            
print("Encerrando programa...")
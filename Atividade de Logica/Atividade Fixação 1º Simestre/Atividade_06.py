# 06. Ler um valor e escrever a mensagem É MAIOR QUE 10! se o valor lido for maior que 10, caso contrário escrever NÃO É MAIOR QUE 10!

verificador = "s"
while verificador == "s" or verificador == "S": 

    numero = float(input("Digite o número: "))

    if numero > 10:
        print(f"O número {numero} é maior que 10.")
    elif numero < 10:
        print(f"O número {numero} é menor que 10.")    
    else:
        print(f"O número {numero} é igual a 10.")    

    verificador = input("\nDeseja fazer um novo calculo? (s/n)\n")
    while verificador != "n" and verificador != "N" and verificador != "s" and verificador != "S":
        verificador = input("Oplção invalida, tente novamente...\n"
                            "Deseja fazer um novo calculo? (s/n)")
        
print("Encerrando programa...")
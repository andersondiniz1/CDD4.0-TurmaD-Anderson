# Crie um código que leia um número diferente de zero e diga se este número é positivo ou negativo:

verificador = "s"
while verificador == "s" or verificador == "S":    

    numero = int(input("Digite o número: "))
    while numero == 0:
        numero = int(input("Deve ser maior ou menor que 0, digite o número novamente: "))
    if numero < 0:
        print(f"O número {numero} é negativo...")
    else:
        print(f"O número {numero} é positivo...")

    verificador = input("Deseja fazer uma nova verificação? (s/n)")
print("Encerrando programa...")
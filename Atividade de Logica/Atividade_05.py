# 05. Crie um algoritmo que leia um número e diga se ele é par ou ímpar

verificador = "s"
while verificador == "s" or verificador == "S": 

    numero = float(input("Digite o número: "))
    while numero == 0:
        numero = int(input("Deve ser maior ou menor que 0, digite o número novamente: "))

    if numero % 2 == 0:
        print(f"O número {numero} é par.")
    else:
        print(f"O número {numero} é ímpar.")

    verificador = input("Deseja fazer uma nova verificação? (s/n)")
print("Encerrando programa...")
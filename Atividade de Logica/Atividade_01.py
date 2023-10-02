# Faça um algoritmo que receba 2 notas e calcule a média aritmética:

verificador = "s"
while verificador == "s" or verificador == "S":    

    quantidade = int(input("Quantas notas você quer inserir? "))
    while quantidade <= 1:
        quantidade = int(input("Deve ser maior que 1, Digite novamente quantas notas você quer inserir? "))

    soma = 0

    for x in range(1, quantidade + 1):
        nota = float(input(f"Digite a {x}ª nota: "))
        while nota < 0 or nota > 10:
            nota = float(input(f"Deve ser entre 0 e 10, digite a {x}ª nota novamente: "))
        soma += nota

    media = soma / quantidade
    print(f"Sua média é: {media:.2f}")
    
    verificador = input("Deseja fazer uma nova média? (s/n)")
print("Encerrando programa...")
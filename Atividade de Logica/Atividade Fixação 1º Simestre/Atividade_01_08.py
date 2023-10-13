# 01. Faça um algoritmo que receba 2 notas e calcule a média aritmética:
# 02. Faça um código que receba 4 números e realize a soma1 deles e a média entre eles. e mostre os resultados.


verificador1 = "s"
while verificador1 == "s" or verificador1 == "S":    

    quantidade1 = int(input("Quantas notas você quer inserir? "))
    while quantidade1 <= 1:
        quantidade1 = int(input("Deve ser maior que 1, Digite novamente quantas notas você quer inserir? "))

    soma1 = 0

    for x in range(1, quantidade1 + 1):
        nota1 = float(input(f"Digite a {x}ª nota: "))
        while nota1 < 0 or nota1 > 10:
            nota1 = float(input(f"Deve ser entre 0 e 10, digite a {x}ª nota novamente: "))
        soma1 += nota1

    media = soma1 / quantidade1
    print(f"Sua média é: {media:.2f}")
    
    verificador = input("\nDeseja fazer um novo calculo? (s/n)\n")
    while verificador != "n" and verificador != "N" and verificador != "s" and verificador != "S":
        verificador = input("Opção invalida, tente novamente...\n"
                            "Deseja fazer um novo calculo? (s/n)")
        
print("Encerrando programa...")
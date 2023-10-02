# 17.As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule eescreva o custo total da compra.

verificador = "s"
while verificador == "s" or verificador == "S": 

    unitario = 1.30  
    duzia = 1.00   

    maca = int(input("Digite o número de maçãs compradas: "))
    while maca <= 0:
        maca = int(input("Digite o número de maçãs compradas diferente de 0: "))

    if maca < 12:
        total = maca * unitario
    else:
        total = maca * duzia

    print(f"O custo total da compra de {maca} maçã(s) é de R$ {total:.2f}.")

    verificador = input("\nDeseja fazer um novo calculo? (s/n)\n")
    while verificador != "n" and verificador != "N" and verificador != "s" and verificador != "S":
        verificador = input("Oplção invalida, tente novamente...\n"
                            "Deseja fazer um novo calculo? (s/n)")
print("Encerrando programa...")


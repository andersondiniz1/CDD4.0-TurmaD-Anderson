# 03. Crie um código que leia a idade de uma pessoa e diga em qual ano ela nasceu:

verificador = "s"
while verificador == "s" or verificador == "S":  
    
    idade = int(input("Digite a sua idade: "))
    while idade <= 0 or idade > 120:
        idade = int(input("Digite a sua idade entre 1 e 120: "))

    mes_atual = int(input("Digite o mês atual: "))
    while mes_atual < 1 or mes_atual > 12:
        mes_atual = int(input("Digite o mês atual entre 1 e 12: "))

    ano_atual = int(input("Digite o ano atual: "))
    while ano_atual <= 0:
        ano_atual = int(input("Digite o ano atual diferente de 0: "))


    ano_nascimento = ano_atual - idade
    if mes_atual < 10:
        ano_nascimento -= 1

    print(f"Ano que você nasceu: {ano_nascimento}")

    verificador = input("\nDeseja fazer um novo calculo? (s/n)\n")
    while verificador != "n" and verificador != "N" and verificador != "s" and verificador != "S":
        verificador = input("Opção invalida, tente novamente...\n"
                            "Deseja fazer um novo calculo? (s/n)")
        
print("Encerrando programa...")

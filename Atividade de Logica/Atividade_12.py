# 12. Escreva um algoritmo para ler o número total de eleitores de um município, o número de votos brancos, nulos e válidos. Calcular e escrever o percentual que cada um representa em relação ao total de eleitores.

verificador = "s"
while verificador == "s" or verificador == "S":

    eleitores = int(input("\nDigite o número total de eleitores: "))
    while eleitores <= 0:
        eleitores = int(input("\nDigite o número total de eleitores maior que 0: "))

    branco = int(input("\nDigite o número de votos brancos: "))
    while branco < 0 or branco > eleitores:
        branco = int(input("\nDigite o número de votos brancos igual ou maior que 0: "))

    nulo = int(input("\nDigite o número de votos nulos: "))
    while nulo < 0 or nulo > eleitores:
        nulo = int(input("\nDigite o número de votos nulos igual ou maior que 0: "))

    valido = int(input("\nDigite o número de votos válidos: \n"))
    while valido < 0 or valido > eleitores:
        valido = int(input("\nDigite o número de votos válidos igual ou maior que 0: \n"))

    percentual_branco = (branco / eleitores) * 100
    percentual_nulo = (nulo / eleitores) * 100
    percentual_valido = (valido / eleitores) * 100

    print("========================================================")
    print(f"Percentual de votos brancos: {percentual_branco:.2f}%")
    print(f"Percentual de votos nulos: {percentual_nulo:.2f}%")
    print(f"Percentual de votos válidos: {percentual_valido:.2f}%")
    print("========================================================")
    
    verificador = input("\nDeseja fazer uma nova verificação? (s/n)\n")
            
print("Encerrando programa...")
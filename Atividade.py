verificador = "s"
while verificador == "s" or verificador == "S":

    print("\n\n========================================================\n"
    "1  - Média aritmética               (1º e 8º questão)\n"
    "2  - Positivo ou negativo           (2º questão)\n"
    "3  - Ano que nasceu                 (3º questão)\n"
    "4  - Maior numero                   (4º questão)\n"
    "5  - Par ou ímpar                   (5º questão)\n"
    "6  - Maior que 10                   (6º questão)\n"
    "7  - Área do triângulo ou retângulo (7º e 13º questão)\n"
    "8  - Antecessor e Sucessor          (9º e 10º questão)\n"
    "9  - Dias de vida                   (11º questão)\n"
    "10 - Percentual de eleição          (12º questão)\n"
    "11 - Fahrenheit para Celsius        (14º questão)\n"
    "12 - Ordem crescente                (15º questão)\n"
    "13 - Tempo jogo Xadrez              (16º questão)\n"
    "14 - Preço das Maças                (17º questão)\n"
    "========================================================\n"
    "0 - Encerrar Programa\n"
    "========================================================\n")
    ops = int(input("\nEscolha uma opção: "))
    print("")

    if ops == 1:
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
            
            verificador1 = input("Deseja fazer uma nova média? (s/n)")
            while verificador1 != "n" and verificador1 != "N" and verificador1 != "s" and verificador1 != "S":
                verificador1 = input("Oplção invalida, tente novamente...\n"
                                     "Deseja fazer um novo calculo? (s/n)")
            
    elif ops == 2:
        verificador1 = "s"
        while verificador1 == "s" or verificador1 == "S":    

            numero = int(input("Digite o número: "))
            while numero == 0:
                numero = int(input("Deve ser maior ou menor que 0, digite o número novamente: "))
            if numero < 0:
                print(f"O número {numero} é negativo...")
            else:
                print(f"O número {numero} é positivo...")

            verificador1 = input("Deseja fazer uma nova verificação? (s/n)")
            while verificador1 != "n" and verificador1 != "N" and verificador1 != "s" and verificador1 != "S":
                verificador1 = input("Oplção invalida, tente novamente...\n"
                                     "Deseja fazer um novo calculo? (s/n)")

    elif ops == 3:
        verificador1 = "s"
        while verificador1 == "s" or verificador1 == "S":  
            
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

            verificador1 = input("Deseja fazer uma nova verificação? (s/n)")
            while verificador1 != "n" and verificador1 != "N" and verificador1 != "s" and verificador1 != "S":
                verificador1 = input("Oplção invalida, tente novamente...\n"
                                     "Deseja fazer um novo calculo? (s/n)")

    elif ops == 4:
        verificador1 = "s"
        while verificador1 == "s" or verificador1 == "S": 

            numero1 = float(input("Digite o primeiro número: "))
            numero2 = float(input("Digite o segundo número: "))
            numero3 = float(input("Digite o terceiro número: "))

            if numero1 > numero2 and numero1 > numero3:
                print(f"O maior número é {numero1}.")
            elif numero2 > numero1 and numero2 > numero3:
                print(f"O maior número é {numero2}.")
            else:
                print(f"O maior número é {numero3}.")
                
            verificador1 = input("Deseja fazer uma nova verificação? (s/n)")
            while verificador1 != "n" and verificador1 != "N" and verificador1 != "s" and verificador1 != "S":
                verificador1 = input("Oplção invalida, tente novamente...\n"
                                     "Deseja fazer um novo calculo? (s/n)")

    elif ops == 5:
        verificador1 = "s"
        while verificador1 == "s" or verificador1 == "S": 

            numero = float(input("Digite o número: "))
            while numero == 0:
                numero = int(input("Deve ser maior ou menor que 0, digite o número novamente: "))

            if numero % 2 == 0:
                print(f"O número {numero} é par.")
            else:
                print(f"O número {numero} é ímpar.")

            verificador1 = input("Deseja fazer uma nova verificação? (s/n)")
            while verificador1 != "n" and verificador1 != "N" and verificador1 != "s" and verificador1 != "S":
                verificador1 = input("Oplção invalida, tente novamente...\n"
                                     "Deseja fazer um novo calculo? (s/n)")
    
    elif ops == 6:
        verificador1 = "s"
        while verificador1 == "s" or verificador1 == "S": 

            numero = float(input("Digite o número: "))

            if numero > 10:
                print(f"O número {numero} é maior que 10.")
            elif numero < 10:
                print(f"O número {numero} é menor que 10.")    
            else:
                print(f"O número {numero} é igual a 10.")    

            verificador1 = input("Deseja fazer uma nova verificação? (s/n)")     
            while verificador1 != "n" and verificador1 != "N" and verificador1 != "s" and verificador1 != "S":
                verificador1 = input("Oplção invalida, tente novamente...\n"
                                     "Deseja fazer um novo calculo? (s/n)")

    elif ops == 7:
        verificador1 = "s"
        while verificador1 == "s" or verificador1 == "S":

            print("\n\n============================\n"
                "T - Area do triângulo\n"
                "R - Area do retângulo\n"
                "N - Sair do programa\n"
                "============================\n")
            ops = input("\nEscolha uma opção: \n") 

            if ops == "t" or ops == "T": 

                base = float(input("Digite o valor da base do triangulo: "))
                while base == 0:
                    base = float(input("Digite o valor da base do triangulo diferente de 0: "))

                altura = float(input("Digite o valor da altura do triangulo: "))
                while base == 0:
                    altura = float(input("Digite o valor da altura do triangulo diferente de 0: "))

                area = (base * altura) / 2
                print(f"A area do triangulo é: {area}.")
                ops = "n"
                verificador1 = input("Deseja fazer uma nova verificação? (s/n)")
                while verificador1 != "n" and verificador1 != "N" and verificador1 != "s" and verificador1 != "S":
                    verificador1 = input("Oplção invalida, tente novamente...\n"
                                         "Deseja fazer um novo calculo? (s/n)")

            elif ops == "r" or ops == "R": 

                base = float(input("Digite o valor da base do retângulo: "))
                while base == 0:
                    base = float(input("Digite o valor da base do retângulo diferente de 0: "))

                altura = float(input("Digite o valor da altura do retângulo: "))
                while base == 0:
                    altura = float(input("Digite o valor da altura do retângulo diferente de 0: "))

                area = base * altura
                print(f"A area do retângulo é: {area}.")
                ops = "n"
                verificador1 = input("Deseja fazer uma nova verificação? (s/n)")
                while verificador1 != "n" and verificador1 != "N" and verificador1 != "s" and verificador1 != "S":
                    verificador1 = input("Oplção invalida, tente novamente...\n"
                                         "Deseja fazer um novo calculo? (s/n)")
            
            elif ops == "n" or ops == "N": 
                verificador1 = "n"
            
            else:
                print("\n Opção invalida, tente novamente...")

    elif ops == 8:
        verificador1 = "s"
        while verificador1 == "s" or verificador1 == "S":

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
                    verificador1 = "s"
                elif ops == 2:
                    sucessor = numero + 1
                    print(f"\nO sucessor do numero {numero} é: {sucessor}\n")
                    verificador2 = "n"
                    verificador1 = input("\nDeseja fazer uma nova verificação? (s/n) \n")
                    while verificador1 != "n" and verificador1 != "N" and verificador1 != "s" and verificador1 != "S":
                        verificador1 = input("Oplção invalida, tente novamente...\n"
                                             "Deseja fazer um novo calculo? (s/n)")
                elif ops == 3:
                    antecessor = numero - 1
                    print(f"\nO antecessor do numero {numero} é: {antecessor}\n")
                    verificador2 = "n"
                    verificador1 = input("\nDeseja fazer uma nova verificação? (s/n) \n")
                    while verificador1 != "n" and verificador1 != "N" and verificador1 != "s" and verificador1 != "S":
                        verificador1 = input("Oplção invalida, tente novamente...\n"
                                             "Deseja fazer um novo calculo? (s/n)")
                elif ops == 0:
                    print("")
                    verificador1 = "n"
                    verificador2 = "n"
                else:
                    print("\n Opção errada, voltando parao menu... \n")

    elif ops == 9:
        verificador1 = "s"
        while verificador1 == "s" or verificador1 == "S":

            idade = int(input("Digite sua idade: "))
            while idade <= 0 or idade > 120:
                idade = int(input("Digite a sua idade entre 1 e 120: "))

            mes_nascimento = int(input("Digite o mês de nascimento: "))
            while mes_nascimento <= 0 or mes_nascimento >= 13:
                mes_nascimento = int(input("Digite o mês de nascimento entre 1 e 12: "))

            dia_nascimento = int(input("Digite o dia de nascimento: "))
            while dia_nascimento <= 0 or dia_nascimento >= 32:
                dia_nascimento = int(input("Digite o dia de nascimento entre 1 e 31: "))

            idade_em_dias = (idade * 365) + (mes_nascimento * 30) + dia_nascimento

            print(f"\nVocê tem: {idade_em_dias} dias de vida.")

            verificador1 = input("\nDeseja fazer uma nova verificação? (s/n) \n")
            while verificador1 != "n" and verificador1 != "N" and verificador1 != "s" and verificador1 != "S":
                verificador1 = input("Oplção invalida, tente novamente...\n"
                                     "Deseja fazer um novo calculo? (s/n)")

    elif ops == 10:
        verificador1 = "s"
        while verificador1 == "s" or verificador1 == "S":

            eleitores = int(input("\nDigite o número total de eleitores: "))
            while eleitores <= 0:
                eleitores = int(input("\nDigite o número total de eleitores maior que 0: "))

            branco = int(input("\nDigite o número de votos brancos: "))
            while branco < 0 or branco > eleitores:
                branco = int(input("\nDigite o número de votos brancos igual ou maior que 0 e entre a quantidade de eleitores: "))

            nulo = int(input("\nDigite o número de votos nulos: "))
            while nulo < 0 or nulo > eleitores:
                nulo = int(input("\nDigite o número de votos nulos igual ou maior que 0 e entre a quantidade de eleitores: "))

            valido = int(input("\nDigite o número de votos válidos: \n"))
            while valido < 0 or valido > eleitores:
                valido = int(input("\nDigite o número de votos válidos igual ou maior que 0 e entre a quantidade de eleitores: \n"))

            percentual_branco = (branco / eleitores) * 100
            percentual_nulo = (nulo / eleitores) * 100
            percentual_valido = (valido / eleitores) * 100

            print("========================================================")
            print(f"Percentual de votos brancos: {percentual_branco:.2f}%")
            print(f"Percentual de votos nulos: {percentual_nulo:.2f}%")
            print(f"Percentual de votos válidos: {percentual_valido:.2f}%")
            print("========================================================")
            
            verificador1 = input("\nDeseja fazer uma nova verificação? (s/n) \n")

    elif ops == 11:
        verificador1 = "s"
        while verificador1 == "s" or verificador1 == "S": 

            fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))

            celsius = ((fahrenheit - 32) / 9) * 5

            print(f"A temperatura em graus Celsius é: {celsius:.2f} °C")

            verificador1 = input("Deseja fazer um novo calculo? (s/n)")
            while verificador1 != "n" and verificador1 != "N" and verificador1 != "s" and verificador1 != "S":
                verificador1 = input("Oplção invalida, tente novamente...\n"
                                    "Deseja fazer um novo calculo? (s/n)")
    elif ops == 12:
        verificador1 = "s"
        while verificador1 == "s" or verificador1 == "S": 

            valor1 = float(input("Digite o primeiro valor: "))
            valor2 = float(input("Digite o segundo valor: "))
            while valor1 == valor2:
                valor2 = float(input("Digite o segundo valor diferente do primeiro: "))

            if valor1 > valor2:
                print(f"Ordem crescente: {valor2}, {valor1}")
            else:
                print(f"Ordem crescente: {valor1}, {valor2}")

            verificador1 = input("Deseja fazer um novo calculo? (s/n)")
            while verificador1 != "n" and verificador1 != "N" and verificador1 != "s" and verificador1 != "S":
                verificador1 = input("Oplção invalida, tente novamente...\n"
                                    "Deseja fazer um novo calculo? (s/n)")
            
    elif ops == 13:
        verificador1 = "s"
        while verificador1 == "s" or verificador1 == "S": 

            hora_inicio = int(input("Digite a hora de início do jogo: "))
            while hora_inicio <= 0 or hora_inicio > 24:
                hora_inicio = int(input("Digite a hora de início do jogo entre 1 e 24 horas: "))

            hora_fim = int(input("Digite a hora de fim do jogo: "))
            while hora_fim <= 0 or hora_fim > 24 or hora_fim > hora_inicio:
                hora_fim = int(input("Digite a hora de fim do jogo entre 1 e 24 horas e menor que a hora de inicio inicio: "))

            duracao = 0
            if hora_inicio == hora_fim:
                duracao = 24 
            elif hora_inicio <= hora_fim:
                duracao = hora_fim - hora_inicio
            else:
                duracao = (24 - hora_inicio) + hora_fim

            print(f"A duração do jogo de xadrez foi de {duracao} horas.")

            verificador1 = input("Deseja fazer um novo calculo? (s/n)")
            while verificador1 != "n" and verificador1 != "N" and verificador1 != "s" and verificador1 != "S":
                verificador1 = input("Oplção invalida, tente novamente...\n"
                                    "Deseja fazer um novo calculo? (s/n)")
                
    elif ops == 14:
        verificador1 = "s"
        while verificador1 == "s" or verificador1 == "S": 

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

            verificador1 = input("Deseja fazer um novo calculo? (s/n)")
            while verificador1 != "n" and verificador1 != "N" and verificador1 != "s" and verificador1 != "S":
                verificador1 = input("Oplção invalida, tente novamente...\n"
                                    "Deseja fazer um novo calculo? (s/n)")
                
    elif ops == 0:
        print("")
        verificador = "n"
    else: 
        print("Opção invalida, tente novamente...")

print("Encerrando programa...")      
# ========================================================================================================== #
# INICIO - Perguntar ao usuário quantos alunos tem na sala e criar um array, unidimensional (Vetor) com o nome de todos os alunos da sala

def cadastro_alunos():

    quantidade = int(input("Quantos alunos há na sala? "))
    alunos = []

    for i in range(quantidade):
        nome = input(f"Digite o nome do {i + 1}º aluno: ")
        alunos.append(nome)
    print("Alunos cadastrados com sucesso...")


    # Variavel de repetição do codigo/aplicativo
    verificador = "s"
    while verificador in "sS":
        # Menu e variavel de opções de seleção
        print("\n\n============================\n"
            "1 - Criar turma novamente\n"
            "2 - Lista de alunos\n"
            "3 - Buscar alunos\n"
            "0 - Sair do programa\n"
            "============================\n")
        ops = input("\nEscolha uma opção: ")
        while ops not in "1230":
            ops = input("\nOpção invalida, tente novamente...\n"
                        "Escolha uma opção acima: ")

        # Quantidade de alunos e Cadastrar alunos
        if ops == "1":
            
            quantidade = int(input("Quantos alunos há na sala? "))
            alunos = []

            for i in range(quantidade):
                nome = input(f"Digite o nome do {i + 1}º aluno: ")
                alunos.append(nome)
            print("Alunos cadastrados com sucesso...")

        # Listar Alunos
        elif ops == "2":

            print("============================\n"
                "Lista dos Alunos:\n"
                "============================\n")
            for i, nome in enumerate(alunos):
                print(f"Posição {i + 1}: {nome}")
            print("============================\n")
            verificador2 = input("Digite qualquer letra para continuar... ")

        # Procurar alunos
        elif ops == "3":

            verificador1 = "s"
            while verificador1 in "sS":
                nome_procurado = input("Digite o nome que você deseja procurar: ")

                if nome_procurado in alunos:
                    posicao = alunos.index(nome_procurado)
                    print(f"\n-   {nome_procurado} está na {posicao + 1}º posição da lista.")
                    verificador1 = input("Deseja fazer uma nova pesquisa de alunos? (s/n)")
                    while verificador1 not in "sSnN":
                        verificador1 = input("Opção invalida, tente novamente...\n"
                                             "Deseja fazer uma nova pesquisa de alunos? (s/n)")
                else:
                    print(f"{nome_procurado} não foi encontrado na lista.\n")
                    verificador1 = input("Deseja fazer uma nova pesquisa de alunos? (s/n)")
                    while verificador1 not in "sSnN":
                        verificador1 = input("Opção invalida, tente novamente...\n"
                                             "Deseja fazer uma nova pesquisa de alunos? (s/n)")
        # Finalizar programa
        elif ops == "0":
            print("Finalizando o aplicativo Cadastro de aluno...")
            verificador == "n"

        else:
            print("\nOpção invalida, tente novamente...\n")


# FIM - Perguntar ao usuário quantos alunos tem na sala e criar um array, unidimensional (Vetor) com o nome de todos os alunos da sala
# ========================================================================================================== #
# INICIO - Escreva um código que permita a leitura das notas de uma turma de 5 alunos e guarde num vetor, Calcular a média da turma e contar quantos alunos obtiveram nota acima desta média calculada Escrever a média da turma e o resultado da contagem

def calcular_media():

    # Variavel de repetição do codigo/aplicativo
    verificador = "s"
    while verificador in "sS":
        
        notas = []
        # Coletar notas dos alunos
        for i in range(5):
            nota = float(input(f"Digite a nota do {i + 1}º aluno: "))
            notas.append(nota)

        # SUM = Soma todas os numeros do Array | len pega a quantidad de indices que estão preenchidos na Array
        media = sum(notas) / len(notas)

        # Contados para alunos acima da média
        acima_media = 0

        # Verificador quais alunos estão acima da média
        for nota in notas:
            if nota > media:
                acima_media += 1


        print("============================\n"
            f"Média da turma: {media:.2f}\n"
            f"Alunos com notas acima da média: {acima_media}\n"
            "============================\n")
        
        verificador = input("Deseja fazer uma nova pesquisa verificação de média? (s/n)")
        while verificador not in "sSnN":
            verificador = input("Opção invalida, tente novamente...\n"
                                "Deseja fazer uma nova verificação de média? (s/n)")



# FIM - Escreva um código que permita a leitura das notas de uma turma de 5 alunos e guarde num vetor, Calcular a média da turma e contar quantos alunos obtiveram nota acima desta média calculada Escrever a média da turma e o resultado da contagem
# ========================================================================================================== #
# INICIO - Ler um vetor A de 10 números. logo em seguida, ler mais um número e guardar em uma variável X.Armazenar em um vetor M o resultado de cada elemento de A multiplicado pelo valor X. Logo após, imprimir o vetor M.

def calcular_AXM():
    
    # Variavel de repetição do codigo/aplicativo
    verificador = "s"
    while verificador in "sS":
        
        vetor = []

        qtd_numero = int(input("Digite a quantidade de nuemros para multiplicar: "))
        for i in range(qtd_numero):
            numero = float(input(f"Digite o {i+1}º número: "))
            vetor.append(numero)

        multiplicador = float(input("Digite um número para multiplicar pelos numeros armazenados: "))

        # multiplica cada número na lista pelo número inserido como multiplicador e armazena os resultados em uma nova lista chamada resultado.
        resultado = [numero * multiplicador for numero in vetor]

        print("Resultado da multiplicação:")
        for i, valor in enumerate(resultado):
            print(f"Elemento {i + 1}: {valor}")

        verificador = input("Deseja fazer uma nova multiplicação? (s/n)")
        while verificador not in "sSnN":
            verificador = input("Opção invalida, tente novamente...\n"
                                "Deseja fazer uma nova multiplicação? (s/n)")

# FIM - Ler um vetor A de 10 números. logo em seguida, ler mais um número e guardar em uma variável X.Armazenar em um vetor M o resultado de cada elemento de A multiplicado pelo valor X. Logo após, imprimir o vetor M.
# ========================================================================================================== #
# INICIO - Faça um código para ler 5 números e armazenar em um vetor. Após a leitura total dos 5 números, o código deve escrever esses 5 números lidos na ordem inversa.

def inverso():

    # Variavel de repetição do codigo/aplicativo
    verificador = "s"
    while verificador in "sS":

        vetor = []

        qtd_numero = int(input("Digite a quantidade de nuemros: "))
        for i in range(qtd_numero):
            numero = float(input(f"Digite o {i+1}º número: "))
            vetor.append(numero)

        print("Números na ordem inversa:")
        for i in range(4, -1, -1):
            print(vetor[i])

        verificador = input("Deseja fazer uma nova inversão? (s/n)")
        while verificador not in "sSnN":
            verificador = input("Opção invalida, tente novamente...\n"
                                "Deseja fazer uma nova inversão? (s/n)")

# FIM - Faça um código para ler 5 números e armazenar em um vetor. Após a leitura total dos 5 números, o código deve escrever esses 5 números lidos na ordem inversa.
# ========================================================================================================== #
# INICIO - Faça um código para ler 5 nomes de usuários e suas respectivas senhas, e armazenar cada lista em um array diferente, após completar a digitação, imprimir , nome, senha e posição dos dados no array.

def cadastro_usuarios():

    # Função para criar contas
    def criar_contas(qtd_usuarios):
        usuarios = {}
        print("=========== CADASTRO ===========")
        for i in range(qtd_usuarios):
            nome = input(f"Digite o nome do {i + 1}º usuário: ")
            senha = input(f"Digite a senha para o usuário {nome}: ")
            print("================================\n")
            usuarios[nome] = senha
        return usuarios

    # Função para tentativas de login
    def tentativa_login(usuarios, tentativas):
        while tentativas > 0:
            print("=========== LOGIN ===========")
            nome_usuario = input("Digite seu nome de usuário: ")
            senha_digitada = input("Digite sua senha: ")
            print("================================\n")

            if nome_usuario in usuarios and usuarios[nome_usuario] == senha_digitada:
                print(f"Login efetuado com sucesso. Bem-vindo, {nome_usuario}!\n\n")
                return True
            else:
                print("Nome de usuário ou senha incorretos. Tente novamente.\n")
                tentativas -= 1

        print("Você excedeu o número máximo de tentativas de login.")
        return False

    # Variável de repetição do código/aplicativo
    verificador = "s"
    while verificador in "sS":

        print("=========== CADASTRO ===========")
        qtd_usuarios = int(input("Digite a quantidade de usuários: "))
        print("================================\n")
        dados_usuarios = criar_contas(qtd_usuarios)
        

        tentativas = 3
        login_sucesso = tentativa_login(dados_usuarios, tentativas)

        verificador = input("Deseja fazer um novo cadastro de usuário? (s/n)")
        while verificador not in "sSnN":
            verificador = input("Opção inválida, tente novamente...\n"
                                "Deseja fazer um novo cadastro de usuário? (s/n)")

# FIM - Faça um código para ler 5 nomes de usuários e suas respectivas senhas, e armazenar cada lista em um array diferente, após completar a digitação, imprimir , nome, senha e posição dos dados no array.
# ========================================================================================================== #
# INICIO - Faça um código para ler um valor N qualquer (que será o tamanho dos vetores). Após, ler dois vetores A e B (de tamanho N cada um) e depois armazenar em um terceiro vetor Soma a soma dos elementos do vetor A com os do vetor B (respeitando as mesmas posições) e escrever o vetor Soma.

def soma_vetor():

    # Variavel de repetição do codigo/aplicativo
    verificador = "s"
    while verificador in "sS":

        N = int(input("N - Digite o tamano dos vetores A e B: "))
        A = [0] * N
        B = [0] * N

        print("================================\n"
            "Digite os elementos do vetor A")
        for i in range(N):
            A[i] = int(input(f"{i + 1}º valor: "))
        print("================================\n"
            "Digite os elementos do vetor B:")
        for i in range(N):
            B[i] = int(input(f"{i + 1}º valor: "))
        print("================================\n")
            
        Soma = [0] * N

        for i in range(N):
            Soma[i] = A[i] + B[i]

        print(f"Soma total: {Soma}")

        verificador = input("Deseja fazer um novo calculo/soma? (s/n)")
        while verificador not in "sSnN":
            verificador = input("Opção inválida, tente novamente...\n"
                                "Deseja fazer um novo calculo/soma? (s/n)")


# FIM - Faça um código para ler um valor N qualquer (que será o tamanho dos vetores). Após, ler dois vetores A e B (de tamanho N cada um) e depois armazenar em um terceiro vetor Soma a soma dos elementos do vetor A com os do vetor B (respeitando as mesmas posições) e escrever o vetor Soma.
# ========================================================================================================== #
# INICIO - Faça um código para ler um vetor de 30 números. Após isto, ler mais um número qualquer, calcular e escrever quantas vezes esse número aparece no vetor.

def contagem():

    # Variavel de repetição do codigo/aplicativo
    verificador = "s"
    while verificador in "sS":

        vetor = [0] * 30

        for i in range(30):
            vetor[i] = int(input(f"Digite o {i + 1}º número: "))

        contado = int(input("Digite o número a ser contado: "))

        contagem = 0

        for numero in vetor:
            if numero == contado:
                contagem += 1

        print(f"O número {contado} aparece {contagem} vezes no vetor.")

        verificador = input("Deseja fazer uma nova verificação? (s/n)")
        while verificador not in "sSnN":
            verificador = input("Opção inválida, tente novamente...\n"
                                "Deseja fazer uma nova verificação? (s/n)")
            
# FIM - Faça um código para ler um vetor de 30 números. Após isto, ler mais um número qualquer, calcular e escrever quantas vezes esse número aparece no vetor.
# ========================================================================================================== #
# INICIO - Escreva um algoritmo que solicite ao usuário a entrada de 5 nomes, e que exiba a lista desses nomes na tela.Após exibir essa lista, o programa deve mostrar também os nomes na ordem inversa em que o usuário os digitou, um por linha.

def reverso():

    # Variavel de repetição do codigo/aplicativo
    verificador = "s"
    while verificador in "sS":

        nomes = []

        for i in range(5):
            nome = input(f"Digite o {i + 1}º nome: ")
            nomes.append(nome)

        print("================================\n"
            "Nomes digitados\n"
            "================================\n")
        for nome in nomes:
            print(nome)
        print("================================\n")

        print("================================\n"
            "Nomes na ordem inversa\n"
            "================================\n")
        for i in range(len(nomes) - 1, -1, -1):
            print(nomes[i])
        print("================================\n")

        verificador = input("Deseja fazer um novo reverso? (s/n)")
        while verificador not in "sSnN":
            verificador = input("Opção inválida, tente novamente...\n"
                                "Deseja fazer umanovo reverso? (s/n)")

# FIM - Escreva um algoritmo que solicite ao usuário a entrada de 5 nomes, e que exiba a lista desses nomes na tela.Após exibir essa lista, o programa deve mostrar também os nomes na ordem inversa em que o usuário os digitou, um por linha.
# ========================================================================================================== #
# INICIO - Faça um algoritmo que leia 30 valores do tipo inteiro e armazene-os em um vetor. A seguir, o algoritmo deverá informar (1) todos os números pares que existem no vetor; (2) o menor e o maior valor existente no vetor; (3) quantos dos valores do vetor são maiores que a média desses valores:

def verificador30numeros():

    vetor = [0] * 30

    for i in range(30):
        vetor[i] = int(input(f"Digite o {i + 1}º número: "))

    verificador = "s"
    while verificador in "sS":
        # Menu e variavel de opções de seleção
        print("\n\n============================\n"
            "1 - Digitar os 30 numeros novamente\n"
            "2 - Números pares\n"
            "3 - Menor e o Maior Número\n"
            "4 - Média dos Valres\n"
            "0 - Sair do programa\n"
            "============================\n")
        ops = input("\nEscolha uma opção: ")
        while ops not in "12340":
            ops = input("\nOpção invalida, tente novamente...\n"
                        "Escolha uma opção acima: ")

    if ops == "1":
        vetor = [0] * 30

        for i in range(30):
            vetor[i] = int(input(f"Digite o {i + 1}º número: "))

    # (1) Todos os números pares que existem no vetor.
    elif ops == "2":
        pares = []

        for numero in vetor:
            if numero % 2 == 0:
                pares.append(numero)
        print(f"Números pares no vetor: {pares}")

    # (2) o menor e o maior valor existente no vetor.
    elif ops == "3":
        menor_valor = vetor[0]
        maior_valor = vetor[0]

        for numero in vetor:
            if numero < menor_valor:
                menor_valor = numero
            if numero > maior_valor:
                maior_valor = numero

        print(f"Menor valor: {menor_valor}")
        print(f"Maior valor: {maior_valor}")

    # (3) quantos dos valores do vetor são maiores que a média desses valores.
    elif ops == "4":
        
        soma = 0
        for numero in vetor:
            soma += numero
        media = soma / len(vetor)

        # Conta quantos valores no vetor são maiores que a média
        contador = 0
        for numero in vetor:
            if numero > media:
                contador += 1

        print(f"Valores maiores que a média: {contador}")

    elif ops == "0":
        verificador == "n"
        print("Finalizando o programa...")

    else:
        print("\nOpção invalida, tente novamente...\n")
        
# FIM - Faça um algoritmo que leia 30 valores do tipo inteiro e armazene-os em um vetor. A seguir, o algoritmo deverá informar (1) todos os números pares que existem no vetor; (2) o menor e o maior valor existente no vetor; (3) quantos dos valores do vetor são maiores que a média desses valores:
# ========================================================================================================== #

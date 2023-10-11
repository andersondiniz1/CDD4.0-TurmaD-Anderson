# ========================================================================================================== #
# INICIO - Perguntar ao usuário quantos alunos tem na sala e criar um array, unidimensional (Vetor) com o nome de todos os alunos da sala
#def cadastro_alunos():


# FIM - Perguntar ao usuário quantos alunos tem na sala e criar um array, unidimensional (Vetor) com o nome de todos os alunos da sala
# ========================================================================================================== #
# INICIO - Escreva um código que permita a leitura das notas de uma turma de 5 alunos e guarde num vetor, Calcular a média da turma e contar quantos alunos obtiveram nota acima desta média calculada Escrever a média da turma e o resultado da contagem

#def calcular_media():

# FIM - Escreva um código que permita a leitura das notas de uma turma de 5 alunos e guarde num vetor, Calcular a média da turma e contar quantos alunos obtiveram nota acima desta média calculada Escrever a média da turma e o resultado da contagem
# ========================================================================================================== #
# INICIO - Ler um vetor A de 10 números. logo em seguida, ler mais um número e guardar em uma variável X.Armazenar em um vetor M o resultado de cada elemento de A multiplicado pelo valor X. Logo após, imprimir o vetor M.

def calculas_AXM():

    vetor = []

    qtd_numero = int(input("Digite a quantidade de nuemros: "))
    for i in range(qtd_numero):
        numero = float(input(f"Digite o {i+1}º número: "))
        vetor.append(numero)

    numero_variavel = float(input("Digite um número para multiplicar pelo vetor: "))

    resultado = [numero * numero_variavel for numero in vetor]

    print("Resultado da multiplicação:")
    for i, valor in enumerate(resultado):
        print(f"Elemento {i + 1}: {valor}")

# FIM - Ler um vetor A de 10 números. logo em seguida, ler mais um número e guardar em uma variável X.Armazenar em um vetor M o resultado de cada elemento de A multiplicado pelo valor X. Logo após, imprimir o vetor M.
# ========================================================================================================== #
# INICIO - Faça um código para ler 5 números e armazenar em um vetor. Após a leitura total dos 5 números, o código deve escrever esses 5 números lidos na ordem inversa.

def inverso():

    vetor = []

    qtd_numero = int(input("Digite a quantidade de nuemros: "))
    for i in range(qtd_numero):
        numero = float(input(f"Digite o {i+1}º número: "))
        vetor.append(numero)

    print("Números na ordem inversa:")
    for i in range(4, -1, -1):
        print(vetor[i])

# FIM - Faça um código para ler 5 números e armazenar em um vetor. Após a leitura total dos 5 números, o código deve escrever esses 5 números lidos na ordem inversa.
# ========================================================================================================== #
# INICIO - Faça um código para ler 5 nomes de usuários e suas respectivas senhas, e armazenar cada lista em um array diferente, após completar a digitação, imprimir , nome, senha e posição dos dados no array.

def cadastro_usuarios():

    usuarios = []
    senhas = []

    qtd_usuarios = int(input("Digite a quantidade de usuarios: "))
    for i in range(qtd_usuarios):
        nome = input(f"Digite o nome de usuário {i+1}: ")
        senha = input(f"Digite a senha para o usuário {nome}: ")
        
        usuarios.append(nome)
        senhas.append(senha)

    print("Dados armazenados:")
    for i in range(qtd_usuarios):
        nome = usuarios[i]
        senha = senhas[i]
        print(f"Posição {i+1} - Nome de usuário: {nome}, Senha: {senha}")


# FIM - Faça um código para ler 5 nomes de usuários e suas respectivas senhas, e armazenar cada lista em um array diferente, após completar a digitação, imprimir , nome, senha e posição dos dados no array.
# ========================================================================================================== #
# INICIO - Altere o sistema anterior e faça um sistema de login, pedindo a senha do usuário e mostrando seu nome e a mensagem, login efetuado com sucesso.

def login():

    dados_usuarios = {}

    for i in range(5):
        nome = input(f"Digite o nome de usuário {i+1}: ")
        senha = input(f"Digite a senha para o usuário {nome}: ")
        
        dados_usuarios[nome] = senha

    tentativas = 3

    while tentativas > 0:
        nome_usuario = input("Digite seu nome de usuário: ")
        senha_digitada = input("Digite sua senha: ")
        
        if nome_usuario in dados_usuarios and dados_usuarios[nome_usuario] == senha_digitada:
            print(f"Login efetuado com sucesso. Bem-vindo, {nome_usuario}!")
            break
        else:
            print("Nome de usuário ou senha incorretos. Tente novamente.")
            tentativas -= 1

    if tentativas == 0:
        print("Você excedeu o número máximo de tentativas de login.\n"
              "Encerrando o programa...")


# FIM - Altere o sistema anterior e faça um sistema de login, pedindo a senha do usuário e mostrando seu nome e a mensagem, login efetuado com sucesso.
# ========================================================================================================== #
# INICIO - Faça um código para ler um valor N qualquer (que será o tamanho dos vetores). Após, ler dois vetores A e B (de tamanho N cada um) e depois armazenar em um terceiro vetor Soma a soma dos elementos do vetor A com os do vetor B (respeitando as mesmas posições) e escrever o vetor Soma.




# FIM - Faça um código para ler um valor N qualquer (que será o tamanho dos vetores). Após, ler dois vetores A e B (de tamanho N cada um) e depois armazenar em um terceiro vetor Soma a soma dos elementos do vetor A com os do vetor B (respeitando as mesmas posições) e escrever o vetor Soma.
# ========================================================================================================== #

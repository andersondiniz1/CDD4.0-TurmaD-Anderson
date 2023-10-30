from Biblioteca import ContaBancaria

def criar_conta():

    print("=============================")
    numero = int(input("Número da conta: "))
    nome = input("Nome do titular da conta: ")
    tipo = input("Tipo da conta: ")
    limite = float(input("Limite de crédito da conta: "))
    saldo_inicial = float(input("Saldo inicial da conta: "))
    print("=============================")  

    conta = ContaBancaria(numero, saldo_inicial, nome, tipo, limite)
    conta.ativar_conta()
    return conta

def main():

    # Lista para armazenar as contas
    contas = []  

    while True:
        print("=============================\n"
              "Escolha uma ação:\n"
              "=============================\n"
              "1. Criar conta\n"
              "2. Acessar conta existente\n"
              "0. Sair\n"
              "=============================\n")
        
        escolha = input("Opção: ")
        while escolha not in ["1", "2", "0"]:
            escolha = input("\nOpção invalida, tente novamente: ")

        if escolha == "1":
            nova_conta = criar_conta()
            contas.append(nova_conta)
            print("\nConta criada com sucesso!")

        elif escolha == "2":
            numero_conta = int(input("Digite o número da conta: "))
            conta = next((c for c in contas if c.numero == numero_conta), None)

            if conta:
                print(f"Conta encontrada: {conta.nome}")

                while True:
                    print("=============================\n"
                          "Escolha uma ação:\n"
                          "=============================\n"
                          "1. Depositar\n"
                          "2. Sacar\n"
                          "3. Verificar saldo\n"
                          "4. Desativar conta\n"
                          "0. Sair\n"
                          "=============================\n")
                    
                    escolha = input("Opção: ")
                    while escolha not in ["1", "2", "3", "4", "0"]:
                        escolha = input("\nOpção invalida, tente novamente: ")

                    if escolha == "1":
                        valor = float(input("\nDigite o valor do depósito: "))
                        print(conta.depositar(valor))

                    elif escolha == "2":
                        valor = float(input("\nDigite o valor do saque: "))
                        print(conta.sacar(valor))

                    elif escolha == "3":
                        print(conta.verificar_saldo())

                    elif escolha == "4":
                        conta.desativar_conta()
                        print("\nConta desativada.")
                        break

                    elif escolha == "0":
                        print("\nEncerrando a conta.")
                        break

                    else:
                        print("\nOpção inválida. Tente novamente.")

            else:
                print("\nConta não encontrada...")

        elif escolha == "0":
            print("\nEncerrando o programa...")
            break

        else:
            print("\nOpção inválida, tente novamente.")

main()

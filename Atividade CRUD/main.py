from crud import inserir_aluno, acessar_conta, sair_banco

while True:
        print("=============================\n"
              "Bem vindo a academia CDD:\n"
              "=============================\n"
              "1. Criar conta\n"
              "2. Acessar contas existentes\n"
              "0. Sair\n"
              "=============================\n")
        
        # repetição se escolher opção errado
        escolha = input("Opção: ")
        while escolha not in ["1", "2", "0"]:
            escolha = input("\nOpção invalida, tente novamente: ")

        # criar conta na academia
        if escolha == "1":
            inserir_aluno()
            print("\nConta criada com sucesso!")

        # verificar contas existentes
        elif escolha == "2":
            acessar_conta()

        # Sair do programa
        elif escolha == "0":
            sair_banco()
            print("\nEncerrando o programa...")
            break

        else:
            print("\nOpção inválida, tente novamente: ")
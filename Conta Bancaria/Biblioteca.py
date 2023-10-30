# conta_bancaria.py

class ContaBancaria:
    def __init__(self, numero, saldo, nome, tipo, limite):
        self.numero = numero
        self.saldo = saldo
        self.nome = nome
        self.tipo = tipo
        self.status = "inativa"
        self.limite = limite

    def ativar_conta(self):
        self.status = "ativa"

    def desativar_conta(self):
        self.status = "inativa"

    def depositar(self, valor):
        if self.status == "ativa" and valor > 0:
            self.saldo += valor
            return f"Depósito de R${valor} realizado. Novo saldo: R${self.saldo}"
        else:
            return "Não é possível realizar o depósito."

    def sacar(self, valor):
        if self.status == "ativa" and 0 < valor <= (self.saldo + self.limite):
            self.saldo -= valor
            return f"Saque de R${valor} realizado. Novo saldo: R${self.saldo}"
        else:
            return "Não é possível realizar o saque."

    def verificar_saldo(self):
        if self.status == "ativa":
            return f"Saldo disponível: R${self.saldo}"
        else:
            return "Conta inativa. Não é possível verificar o saldo."

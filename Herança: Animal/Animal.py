class Animal(): #Super Classe

    def __init__(self, nome , cor):
        self.nome = nome
        self.cor = cor

    def comer(self):
        print( f' O {self.nome} foi comer...')

class Gato(Animal): # Sub Classe

    def __init__(self, nome, cor):
        super().__init__(nome, cor) # Chamar o metodo construtor da Super classe

    def miar(self):
        print( f' O {self.nome} foi miando...')

# Criar uma instância da classe Animal
animal = Animal("Leão", "marrom")
print(f"Um {animal.nome} de cor {animal.cor} apareceu.")
animal.comer()

# Criar uma instância da classe Gato
gato = Gato("Whiskers", "cinza")
print(f"Um gato chamado {gato.nome} de cor {gato.cor} apareceu.")
gato.comer()  # O gato herda o método comer da classe Animal
gato.miar()  # Método específico da classe Gato

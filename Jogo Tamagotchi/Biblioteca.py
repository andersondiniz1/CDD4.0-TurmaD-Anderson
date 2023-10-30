class Tamagotchi:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 0
        self.felicidade = 100
        self.saude = 100

    def alimentar(self):
        self.fome -= 10
        if self.fome < 0:
            self.fome = 0

    def brincar(self):
        self.felicidade += 10
        if self.felicidade > 100:
            self.felicidade = 100

    def curar(self):
        self.saude += 10
        if self.saude > 100:
            self.saude = 100

    def esta_vivo(self):
        return self.fome < 100 and self.felicidade > 0 and self.saude > 0

    def status(self):
        return f"\n | {self.nome} \n | Fome: {self.fome} \n | Felicidade: {self.felicidade} \n | Saúde: {self.saude} \n" 

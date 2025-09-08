class Carro:
    def __init__(self, cor, modelo):
        self.cor = cor
        self.modelo = modelo

    def descrever(self):
        return f"Este carro é {self.cor} e é um {self.modelo}."

carro1 = Carro("preto", "Fusca")
carro2 = Carro("branco", "Civic")

print(carro1.descrever())
print(carro2.descrever())
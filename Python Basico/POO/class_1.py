class Casa:
    def __init__(self, cor, tamanho):
        self.cor = cor
        self.tamanho = tamanho

    def descrever(self):
        return f"Esta casa é {self.cor} e tem {self.tamanho} metros quadrados."

casa1 = Casa("azul", 100)
casa2 = Casa("vermelha", 150)

print(casa1.descrever())
print(casa2.descrever())
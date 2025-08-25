# Polymorfismo

class Personagens():
    def atacar(self):
        print("Eu sou um personagem.")

class Guerreiro():
    def atacar(self):
        print("O guerreiro ataca com sua espada!")

class Mago():
    def atacar(self):
        print("O mago lança um feitiço!")

class Arqueiro(Personagens):
    def atacar(self):
        print("O arqueiro atira uma flecha!")

# Criar os Objetos

personagens = [Guerreiro(), Mago(), Arqueiro()]

for p in personagens:
    p.atacar()
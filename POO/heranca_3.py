# Herança Multipla

class Predador():
  def cacando(self):
    print("O predador está caçando.")

class Presa():
  def fugindo(self):
    print("A presa está fugindo.")

# Classes Filho
class Leão(Predador):
  pass

class Gazela(Presa):
  pass

class Hiena(Predador, Presa):
  pass

gazela1 = Gazela()
leao1 = Leão()
hiena1 = Hiena()

gazela1.fugindo()
hiena1.cacando()
hiena1.fugindo()

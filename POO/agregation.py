class Motor:
  def __init__(self, marca, potencia):
    self.marca = marca
    self.potencia = potencia

class Carro:
  def __init__(self):
    self.motores = []

  def adicionar_motor(self, motor):
    self.motores.append(motor)

  def listar_motores(self):
    for motor in self.motores:
      print(f"Marca: {motor.marca}, Potência: {motor.potencia} HP")

# Criando os Motores (Objetos)
motor_v6 = Motor("Ford", 300)

# Criar o carro e adicionar o motor
carro = Carro()
carro.adicionar_motor(motor_v6)

# Listar Motores do Carro
carro.listar_motores()

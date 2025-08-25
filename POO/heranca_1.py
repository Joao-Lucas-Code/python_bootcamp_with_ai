class Animal:
  def __init__(self, nome, cor, especie):
    self.nome = nome
    self.cor = cor
    self.especie = especie

  def fazer_som(self):
    print(f'O {self.especie} chamado {self.nome} está fazendo um som.')


class Gato(Animal):
  def __init__(self, nome, cor, especie, raca):
    super().__init__(nome, cor, especie)
    self.raca = raca

  def fazer_som(self):
    print(f'O gato {self.nome} está miando.')

gato1 = Gato('Whiskers', 'preto', 'felino', 'Siamês')

animal1 = Animal('Generic Animal', 'marrom', 'mamífero')

gato1.fazer_som()
animal1.fazer_som()
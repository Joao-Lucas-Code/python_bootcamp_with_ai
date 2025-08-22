class Pessoa:
  def __init__(self, nome, sobrenome, idade, cargo):
    self.nome = nome
    self.sobrenome = sobrenome
    self.idade = idade
    self.cargo = cargo

  def apresentar(self):
    return f"Olá, meu nome é {self.nome} {self.sobrenome} e eu tenho {self.idade} anos."

  def informacoes(self):
    print(f'Nome: {self.nome} {self.sobrenome}\nIdade: {self.idade}\nCargo: {self.cargo}')

  def promover(self, novo_cargo):
    self.cargo = novo_cargo
    print(f'{self.nome} foi promovido a {self.cargo}')


pessoa1 = Pessoa("João Lucas", "Gomes", 19, "Dev Junior")
pessoa2 = Pessoa("Cauã Mendes", "Pinto", 17, "Dev Pleno")

pessoa1.informacoes()
print()
pessoa2.informacoes()

pessoa2.promover("Dev Senior")
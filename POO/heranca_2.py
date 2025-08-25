class Pessoa:
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade

  def apresentar(self):
    print(f'Olá, meu nome é {self.nome} e eu tenho {self.idade} anos.')

class Funcionario(Pessoa):
  def __init__(self, nome, idade, cargo):
    super().__init__(nome, idade)
    self.cargo = cargo

  def trabalhar(self):
    print(f'{self.nome} está trabalhando como {self.cargo}.')

class Cliente(Pessoa):
  def __init__(self, nome, idade, cpf):
    super().__init__(nome, idade)
    self.cpf = cpf

  def comprar(self):
    print(f'{self.nome} está comprando com o CPF {self.cpf}.')

f1 = Funcionario('Aghata', 28, 'Engenheira')
f1.apresentar()
f1.trabalhar()

c1 = Cliente('João', 30, '123.456.789-00')
c1.apresentar()
c1.comprar()
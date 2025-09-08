class Funcionarios:
  def __init__(self, nome, sobrenome, idade):
      self.nome = nome
      self.sobrenome = sobrenome
      self.idade = idade
  
  def nome_completo(self):
      return f'{self.nome} {self.sobrenome}'

# criar o objeto
usuario1 = Funcionarios('João', 'Silva', 30)
usuario2 = Funcionarios('Maria', 'Souza', 25)

# print
print(usuario1.nome_completo())
print(usuario2.nome_completo())
class Funcionarios:
  def __init__(self, nome, sobrenome, idade):
      self.nome = nome
      self.sobrenome = sobrenome
      self.idade = idade
  
  def nome_completo(self):
      return f'{self.nome} {self.sobrenome}'
  
  def ano_nascimento(self, ano_atual=2024):
      return ano_atual - self.idade

# criar o objeto
usuario1 = Funcionarios('João', 'Silva', 2005)
usuario2 = Funcionarios('Maria', 'Souza', 1998)

# print
print(usuario1.nome_completo())
print(usuario2.nome_completo())

# ano de nascimento
print(usuario1.ano_nascimento())
print(usuario2.ano_nascimento())
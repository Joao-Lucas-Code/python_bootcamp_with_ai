class Funcionarios:
  def __init__(self, nome, sobrenome, idade):
      self.nome = nome
      self.sobrenome = sobrenome
      self.idade = idade

# criar o objeto
usuario1 = Funcionarios('João', 'Silva', 30)
usuario2 = Funcionarios('Maria', 'Souza', 25)

# print
print(usuario1.nome)      # Saída: João
print(usuario2.nome)    # Saída: Maria
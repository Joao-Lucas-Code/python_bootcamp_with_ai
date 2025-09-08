# Functions (Funções)
  # DRY (Don't Repeat Yourself)

def cliente1(nome):
    print(f"Ola {nome}, seja bem-vindo(a)!")

def cliente2(nome):
    return f"Ola {nome}, seja bem-vindo(a)!"

x = cliente1('Maria')
y = cliente2('João')

print(x)
print(y)
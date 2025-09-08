# Functions (Funções)
  # DRY (Don't Repeat Yourself)

def boas_vindas(nome, quantidade):
    print(f"Seja bem-vindo(a), {nome}!")
    print(f'Temos {str(quantidade)} laptops em estoque')

boas_vindas("Alice", 5)
boas_vindas("Bob", 10)
boas_vindas("Charlie", 3)
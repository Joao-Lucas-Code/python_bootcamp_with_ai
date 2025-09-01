# Functions (Funções)
  # DRY (Don't Repeat Yourself)

def boas_vindas(nome, quantidade=5):
    print(f"Seja bem-vindo(a), {nome}!")
    print(f'Temos {str(quantidade)} laptops em estoque')

boas_vindas("Alice")

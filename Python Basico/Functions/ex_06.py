# Functions (Funções)
  # DRY (Don't Repeat Yourself)
  # Varios Argumentos (xargs)

# Criar uma função que soma vários números.

def soma(*numeros):
  resultado = 0
  for num in numeros:
    resultado += num
  return resultado

x = soma(2,3,4,5,9)

print(x)
quadrado = lambda x: x * x

lista = [1, 2, 3, 4, 5]
resultado = list(map(quadrado, lista))
print(f"Os quadrados dos números {lista} são {resultado}.")
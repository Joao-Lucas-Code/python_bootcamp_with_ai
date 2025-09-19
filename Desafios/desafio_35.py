hipotenusa = lambda a, b: (a**2 + b**2)**0.5

cateto1 = float(input("Digite o comprimento do primeiro cateto: "))
cateto2 = float(input("Digite o comprimento do segundo cateto: "))

print(f"A hipotenusa do triângulo retângulo com catetos {cateto1} e {cateto2} é {hipotenusa(cateto1, cateto2)}.")
par_impar = lambda x: "Par" if x % 2 == 0 else "Ímpar"

num = int(input("Digite um número inteiro: "))
print(f"O número {num} é {par_impar(num)}.")
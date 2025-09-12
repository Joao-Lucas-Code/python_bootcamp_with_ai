frutas = ["maçã", "banana", "laranja", "uva", "manga", "maçã", "maçã"]

cont = 0
for fruta in frutas:
    if fruta == "maçã":
        cont += 1

print(f"A palavra 'maçã' aparece {cont} vezes na lista.")
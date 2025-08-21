preco = float(input("Digite o preço: "))

desconto = preco * 0.10
preco_final = preco - desconto

print(f"Preço original: {preco}")
print(f"Desconto: {desconto:.2f}")
print(f"Preço final: {preco_final}")
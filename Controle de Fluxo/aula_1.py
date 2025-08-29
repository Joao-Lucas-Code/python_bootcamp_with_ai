velocidade = 100

if velocidade > 80:
    print("Você está acima da velocidade permitida!")

    multa = (velocidade - 80) * 5
    print(f"Você foi multado em R$ {multa:.2f}")
    print("Tenha um bom dia!")
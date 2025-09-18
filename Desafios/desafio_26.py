def potencia(base, expoente = 2):
    if expoente < 0:
        return 1 / (base ** abs(expoente))
    else:
        return base ** expoente
    
print(potencia(3))        # Saída: 9
print(potencia(2, 3))     # Saída: 8
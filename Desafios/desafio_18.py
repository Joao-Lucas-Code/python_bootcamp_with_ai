estoque_carros = ['BMWX6', 'BMWI5', 'BMWX1', 'BMWX3', 'BMWX5', 'BMWI8']

carro_usuario = input('Digite o modelo do carro que você deseja: ').strip().upper()
if carro_usuario in estoque_carros:
    print(f'Parabéns! O carro {carro_usuario} está disponível no nosso estoque.')
else:
    print(f'Sinto muito, o carro {carro_usuario} não está disponível no nosso estoque.')
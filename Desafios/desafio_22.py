capitais_pais = {
    'Brasil': 'Brasília',
    'Argentina': 'Buenos Aires',
    'Colômbia': 'Bogotá',
    'Peru': 'Lima',
    'Venezuela': 'Caracas'
    }

pais = str(input('Digite o nome de um país: ')).title() # Usando title() para padronizar a entrada do usuário
if pais in capitais_pais:
    print(f'A capital de {pais} é {capitais_pais[pais]}.')
else:
    print('País não encontrado no dicionário.')
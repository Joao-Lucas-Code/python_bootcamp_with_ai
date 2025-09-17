cidades = ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Salvador', 'Fortaleza']

if str(input('Digite o nome de uma cidade: ')).title() in cidades: # Usando title() para padronizar a entrada do usuário
    print('A cidade está na lista.')
else:
    print('A cidade não está na lista.')
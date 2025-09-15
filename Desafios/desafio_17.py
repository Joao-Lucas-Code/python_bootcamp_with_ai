idade = int(input('Digite sua idade: '))

if idade < 13:
  print('Criança')
elif 13 <= idade <= 19:
  print('Adolescente')
else:
  print('Adulto')
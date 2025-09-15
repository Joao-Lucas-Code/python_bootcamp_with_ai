while True:
  fruta = 'ABACATE'
  usuario_chute = str(input('Qual fruta estou pensando? ')).strip().upper()
  if usuario_chute == fruta:
      print('Parabéns! Você acertou a fruta.')
      break
  else:
      print('Tente novamente.')
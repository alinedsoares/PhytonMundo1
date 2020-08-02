distancia = float(input('Qual a distância da sua viagem em km? '))
if distancia <= 200:
    print('O valor da sua viagem será R${:.2f}'.format(distancia * 0.50))
else:
    print('O valor da sua viagem será R${:.2f}'.format(distancia * 0.45))

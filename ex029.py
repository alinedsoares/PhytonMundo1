vel = float(input('Informe qual é a velocidade do carro: '))
if vel > 80:
    print('Você foi multado e terá que pagar R${:.2f} de multa!'.format((vel-80) * 7))
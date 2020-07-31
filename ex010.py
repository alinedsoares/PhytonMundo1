r = float(input('Quanto dinheiro você tem na carteira? R$ '))
c = float(input('Qual a taxa de conversão do Dollar? '))
print('Com R${:.2f} você pode comprar US${:.2f}'.format(r, (r / c)))

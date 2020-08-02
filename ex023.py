## ereeeeiiii... só funciona com números de 4 dígitos
##n = int(input('Digite um número: '))
##num09999 = str(n)
##print('Unidade: {}'.format(num09999[3]))
##print('Dezena: {}'.format(num09999[2]))
##print('Centena: {}'.format(num09999[1]))
##print('Milhar: {}'.format(num09999[0]))

n = int(input('Digite um número: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))

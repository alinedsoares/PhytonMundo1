from math import hypot

co = float(input("Digite o comprimneto do cateto oposto: "))
ca = float(input('Digite o comprimento do cateto adjacente: '))
print('Considerando cateto oposto {} e cateto adjacente {}, a hipotenusa vai medir {:.2f}'.format(co, ca, hypot(co, ca)))

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))

if a < b and a < c:
    menor = a
if b < c and b < a:
    menor =b
if c < b and c < a:
    menor = c
print('O menor número é {}'.format(menor))

if a > b and a > c:
    maior = a
if b > c and b > a:
    maior = b
if c > a and c > b:
    maior = c
print ('O maior número é {}'.format(maior))

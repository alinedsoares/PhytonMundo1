import random
print('Estou pensando em um número de 0 a 5...')
palpite = str(input('Em qual número de 0 a 5 você acha que eu estou pensando? '))
numeros = ["0", "1", "2", "3", "4", "5"]
computador = random.choice(numeros)
if computador == palpite:
    print('Parabéns, você VENCEU e descobriu que pensei no número {}!!!'.format(palpite))
else:
    print('Você errou e PERDEU, não pensei no número {} e sim no número {} !!!'.format(palpite, computador))

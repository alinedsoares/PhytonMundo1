from math import radians
from math import sin
from math import cos
from math import tan

angulo = float(input('Digite um ângulo qualquer: '))
print('Para um ângulo de {:.0f} o seno é {:.2f}, o cosseno {:.2f} e a tangente é {:.2f}!!'.format(angulo, sin(radians(angulo)), cos(radians(angulo)), tan(radians(angulo))))
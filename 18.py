import math
from math import radians, sin, cos, tan
print('FAÇA UM PROGRAMA QUE LEIA UM ÂNGULO QUALQUER E MOSTRE NA TELA O VALOR DO SENO, COSSENO E TANGENTE DESSE ÂNGULO.')
ang = float(input('Digite um ângulo! - '))
sen = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print('Para o ângulo de {:.2f}\n'
      'O seu seno é {:.2f} \n'
      'O seu cosseno é {:.2f}\n'
      'E a sua tangente é {:.2f} !'.format(ang, sen, cos, tan))

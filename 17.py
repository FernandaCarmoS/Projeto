# Essa primeira forma eu vou deixar como comentário, pois ela não precisa de importar biblioteca e é a forma mais difícil.
print('FAÇA UM PROGRAMA QUE LEIA O COMPRIMENTO DO CATETO OPOSTO E DO CATETO ADJACENTE DE UM TRIÂNGULO E RETÂNGULO, CALCULE E MOSTRE O COMPRIMENTO DA HIPOTENUSA.')
# op = float(input('Digite o cateto oposto - '))
# ad = float(input('Digite o cateto adjacente - '))
# hip = (op ** 2 + ad ** 2) ** (1/2)
# print('A hipotenusa vai medir {:.2f}'.format(hip))
# Agora vamos fazer da forma mais fácil importando a biblioteca do math.
from math import hypot
op = float(input('Digite o cateto oposto - '))
ad = float(input('Digite o cateto adjacente - '))
hip = hypot(op,ad)
print('A hipotenusa vai medir {:.2f}'.format(hip))


import math
print('CRIE UM ALGORITMO QUE LEIA UM NÚMERO E MOSTRE O SEU DOBRO, TRIPLO E A RAIZ QUADRADA.')
print('Resolução: ')
num = int(input('Digite um número qualquer! -  '))
dobro = num * 2
triplo = num * 3
raiz = math.sqrt(num)
print('Analisando o número {} , vimos que o dobro dele é {}\n'
      'O triplo é {}\n'
      'E a sua raiz é {:.2f}'.format(num, dobro, triplo, raiz))
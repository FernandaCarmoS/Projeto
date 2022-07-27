print('Programa para verificcar se dois números são pares ou ímpares!')
a = int(input('Digite o primeiro número! '))
b = int(input('Digite o segundo número! '))
restoa = a % 2
restob = b % 2
if restoa == 0 and restob == 0:
    print('O número {} e o número {} são pares!'.format(a,b))
elif restoa ==0 and restob != 0:
    print('O número {} é par e o número {} é impar'.format(a, b))
elif restoa != 0 and restob == 0:
    print('O número {} é impar e o número {} é par'.format(a, b))
elif restoa != 0 and restob != 0:
    print('O número {} e o número {} são ímpares'.format(a, b))
    print('Fim do Programa!')
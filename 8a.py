print('Programa para descobrir se o número é par ou impar!')
a = int(input('Digite um número qualquer! '))
resto = a % 2
if resto == 0:
    print('O número {} é par'.format(a))
elif resto != 0:
    print('O número {} é impar'.format(a))
    print('Fim do programa')
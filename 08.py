print('Digite 3 números para descobrirmos qual é o maior! ')
a = int(input('Vamos começar com o primeiro, pode digitar! '))
b = int(input('Digite o segundo nùmero '))
c = int(input('Digite o terceiro número '))

if a > b and a > c:
    print('O número {} é o maior de todos!'.format(a))
elif b > a and b > c:
    print('O número {} é o maior de todos!'.format(b))
elif c > a and c > b:
    print('O número {} é o maior de todos!'.format(c))

elif a == b and a > c:
    print('O número {} é igual ao segundo número, e esses dois números são os maiores!'.format(a))
elif a == b and a < c:
    print('O número {} é igual ao segundo número, mas o número {} ainda é o maior de todos!'.format(a, c))
elif a == c and a and c > b:
    print('O número {} e {} são iguais e são maiores do que {}'.format(a, c, b))
elif b == c and b and c > a:
    print('O número {} é igual ao terceiro número digitado e ambos são os maiores números!'.format(b))
elif b == c and b and c < a:
    print('O número {} é igual ao terceiro número digitado, porém o número {} é o maior de todos!'.format(b, c, a))
elif a == b and b == c:
    print('Os três números são iguais, portanto não existe um número maior!')
    print('Fim do Programa!')
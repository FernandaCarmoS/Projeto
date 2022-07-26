from math import trunc
# From importa da biblioteca math somente a função que iremos usar(trunc).
# O código 'trunc' elimina todos os números após a vírgula.
print('CRIE UM PROGRAMA QUE LEIA UM NÚMERO REAL QUALQUER PELO TECLADO E MOSTRE NA TELA A SUA PORÇÃO INTEIRA. EX: DIGITE UM NÙMERO:6.127 – O NÙMERO 6.127 TEM A PORTA INTEIRA 6.')
num = float(input('Digite um número real(Com pontos flutuantes)! - '))
print('O número {} tem a porta inteira de {} !'.format(num,trunc(num)))
# Como importamos através do código from o trunc, nós não precisamos usar o math novamente no format.
# E podemos também criar esse código sem importar nenhuma biblioteca math como demonstrado abaixo.
# num = float(input('Digite um número real(Com pontos flutuantes)! - '))
# print('O número {} tem a porta inteira de {} !'.format(num, int(num)))
# O código int(inteiro) deixará o número inteiro.

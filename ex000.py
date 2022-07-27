n1 = int(input('Digite um valor - '))
n2 = int(input('Digite outro valor - '))
soma = n1 + n2
M = n1 * n2
d = n1 / n2
di = n1 // n2
p = n1**n2
print('A soma entre {} e {} é {} e a \n Multiplicação entre {} e {} é {} .'.format(n1, n2, soma, n1, n2, M,))
print('E  temos tambèm a divisão inteira de \n {} por {} é {} e também temos {} elevado a {} que vale {}.'.format(n1, n2, di,n1, n2, p) , end=' ')
print('Já a divisão real entre {} e {} é {:.3f} .'.format(n1, n2, d))

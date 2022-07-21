print('008- ESCREVA UM PROGRAMA QUE LEIA UM VALOR EM METROS E O EXIBA CONVERTIDO EM CENTIMETROS  E MILIMETROS.')
valor = float(input('Digite quantos metros você deseja converter! '))
cent = valor * 100
mm = valor * 1000
print('O valor {} equivale a {} centímetros e {} milímetros'.format(valor, cent, mm))
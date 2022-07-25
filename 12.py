print('FAÇA UM ALGORITMO QUE LEIA O PREÇO DE UM PRODUTO E MOSTRE SEU NOVO PREÇO, COM 5% DE DESCONTO.')
prec = float(input('Digite o valor atual do produto! - R$ '))
desconto = prec * 5/100
valor = prec - desconto
print('O seu produto com o valor de {:.2f} reais, com o desconto de 5% vai para R$ - {:.2f} reais'.format(prec,valor))

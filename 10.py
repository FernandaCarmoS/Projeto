
print('CRIE UM PROGRAMA QUE LEIA QUANTO DINHEIRO UMA PESSOA TEM NA CARTEIRA E MOSTRE QUANTOS DÓLARES ELA PODE COMPRAR.'
      '\n OBS: CONSIDERE US$ 1,00 = R$ 3,27 E INCLUA O EURO COM O VALOR DE E 0,18.')
valor = float(input('Digite qual o valor em reais você possui! - R$ '))
dolar = valor / 3.27
euro = valor * 0.18
print('Com R$ {:.2f} você pode comprar US$ {:.2f} dólar!'.format(valor, dolar))
print('E com R$ {:.2f} reais você pode comprar E {:.2f} euro!'.format(valor,euro))
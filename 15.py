print('ESCREVA UM PROGRAMA QU PERGUNTE A QUANTIDADE DE KM PERCORRIDOS POR UM CARRO ALUGADO E A QUANTIDADE DE DIAS PELOS QUAIS ELE FOI ALUGADO. CALCULE O PREÇO A PAGAR , SABENDO QUE O CARRO CUSTA R$60 POR DIA E R$0,15 POR KM RODADO.')
km = float(input('Informe quantos KM o carro percorreu! - '))
dias = int(input('Informe quantos dias você alugou! - '))
pkm = km * 0.15
pdias = dias * 60
total = pkm + pdias
# Este calculo é baseado no km que equivale a R$ 0,15 e por dia alugado que equivale a R$ 0,15 e no final soma-se os dois valores.
print('Analisando que você percorreu {:.2f} KM e alugou por {} dias o valor total a pagar é de R$ {:.2f} reais!'.format(km, dias, total))
print('ESCREVA UM PROGRAMA QUE CONVERTA UMA TEMPERATURA DIGITADA EM CELSIUS E CONVERTA PARA FAHRENHEIT.')
cel = float(input('Informe qual a temperatura em celsius! - '))
convert = (cel * 1.8)+32
#Fórmula de conversão de celsius para fahrenheit, outra fòrmula seria = 9 * cel / 5 + 32
print('A temperatura de {:.2f} graus celsius convertida será de {:.2f} graus fahrenheit!'.format(cel,convert))
fah = float(input('Agora informe a temperatura em fahrenheit para converter para celsius! - '))
convert2 = (fah-32)/1.8
#Fórmula de conversão de fahrenheit para celsius.
print('A temperatura de {:.2f} graus fahrenheit convertida será de {:.2f} graus celsius!'.format(fah,convert2))
#O código{:.2f} possibilita que o numeral seja formado por duas casas decimais.
print('FAÇA UM ALGORITMO E MOSTRE O SEU NOVO SALÁRIO COM 15% DE AUMENTO.')
salario = float(input('Informe o seu salário atual! - R$ '))
aumento = salario + (salario * 15/100)
print('O seu salário de R$ {:.2f} reais com um aumento de 15% irá para R$ {:.2f} reais! '.format(salario,aumento))
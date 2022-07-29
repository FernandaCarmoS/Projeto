print('CRIE UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA E MOSTRE:\n'
'O NOME COM TODAS AS LETRAS MAIÙSCULAS:\n'
'O NOME COM TODAS MINÙSCULAS.\n'
'QUANTAS LETRAS AO TODO(SEM CONSIDERAR ESPAÇOS.)\n'
 'QUANTAS LETRAS TEM O PRIMEIRO NOME.')
algo = str(input('Digite o seu nome completo! - ')).strip()
print('Analisando o seu nome...')
print('O nome {} com todas as letras maiúsculas é: {}'.format(algo, algo.upper()))
print('Já com todas as letras minúsculas é: {}'.format(algo.lower()))
print('E o seu nome possui {} letras.'.format(len(algo)- algo.count(' ')))
#print('E por fim o seu primeiro nome tem {} letras.'.format(algo.find(' ')))
# Esta é uma forma de fazer, mas abaixo vamos exemplificar.
separa = algo.split()
print('O seu primeiro nome é {} e tem {} letras.'.format(separa[0], len(separa)))


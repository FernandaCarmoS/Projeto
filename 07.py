print(' DESENVOLVA UM PROGRAMA QUE LEIA AS DUAS NOTAS DE UM ALUNO, CALCULE E MOSTRE A SUA MÈDIA.')
print('Resolução: ')
n1 = int(input('Digite a sua primeira nota! - '))
n2 = int(input('Digite a sua segunda nota ! - '))
media  = (n1 + n2) / 2
if media >= 5:
    print('A sua média nesta matéria é {} e você está APROVADO! '.format(media))
elif media < 5:
    print('A sua média nesta matéria é {} e você está REPROVADO! '.format(media))
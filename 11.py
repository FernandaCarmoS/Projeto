print('FAÇA UM PROGRAMA QUE LEIA A LARGURA DE UMA PAREDE EM METROS, CALCULE A SUA ÁREA E A QUANTIDADE DE TINTA NECESSÁRIA PARA PINTÁ-LA, SABENDO QUE CADA LITRO DE TINTA, PINTA UMA ÁREA DE 2 M2.')
met = float(input('Digite a largura da parede! - '))
alt = float(input('Digite a altura da parede! - '))
area = met * alt
tinta = area / 2
print('A sua parede tem a  dimensão de {} x {} , portanto a sua área mede {} m²! '.format(met,alt,area))
print('E para pintar essa parede você vai precisar de {} litros de tinta! '.format(tinta))


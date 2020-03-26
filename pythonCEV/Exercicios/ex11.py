'''
calcular area de uma parede em metros e depois calcular a quantidade de baldes de tintas necessario para pinta-las
sabendo que cada balde ocupa 2m²
'''

alt = float(input("Digite a altura da parede: "))
larg = float(input('Digite a largura da parede: '))
area = alt * larg
nbaldes = area/2
print('A parede tem {:.2f}m²'.format(area))
print('Sera necessario {} litros de tinta para pintar a parede'.format(nbaldes))
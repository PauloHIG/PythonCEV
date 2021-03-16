"""
calcular área de uma parede em metros e depois calcular a quantidade de baldes de tintas necessários para pinta-las
sabendo que cada balde pinta 2m² de parede
"""

alt = float(input("Digite a altura da parede: "))
larg = float(input("Digite a largura da parede: "))
area = alt * larg
nbaldes = area / 2
print("A parede tem {:.3f}m²".format(area))
print("Será necessario {} litros de tinta para pintar a parede".format(nbaldes))

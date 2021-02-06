'''Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, 
sabendo que o vencedor tirou o maior número no dado.
'''
from random import randint
from operator import itemgetter
from time import sleep
jogos={
	'Jogador1':randint(1,6),
	'Jogador2':randint(1,6),
	'Jogador3':randint(1,6),
	'Jogador4':randint(1,6)}

for jogador,res in jogos.items():
	print(f'{jogador} tirou {res} no dado')
	sleep(0.5)

ordem = sorted(jogos.items(), key = itemgetter(1), reverse = True)#assim funciona o ittemgetter (1) significa valor e(0) a chave

print('Ranking: ')
sleep(0.5)
for posição, dicionário in enumerate(ordem):#o enumerate me possibilita o uso dessa varoável posição
	print(f'{posição+1}º : {dicionário[0]} pontuação: {dicionário[1]}')#como pode ver, o ittemgetter colocou os nomes em uma tupla e juntou todos eles em uma lista
	sleep(0.5)
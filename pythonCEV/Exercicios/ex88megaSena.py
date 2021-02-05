'''Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta.'''

from time import sleep
from random import sample
jogos = int(input('Quantos jogos serão gerados? '))
lista = []
for i in range(jogos):
	lista.append(sample(range(60),6)) #essa função sample basicamente já faz o que eu preciso
i=1
for jogo in lista:
	print(f'jogo {i}: {jogo}')
	sleep(0.20)
	i+=1
'''
a = sample(range(100),100)
print(a)
print(sorted(a))#pra provar que o sample não repete números
use esse codigo aqui pra entender o uso do sample
'''
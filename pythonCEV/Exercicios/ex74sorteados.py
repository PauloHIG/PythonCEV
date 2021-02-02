'''Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
'''
from random import randint

n =(randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))#unica maneira de colocar 5 itens aleatorios em uma tupla
print('Os numeros sorteados foram:',end=' ')
for num in n:
	print(num,end=' ')
print(f'\nO maior é {max(n)}')
print(f'O menor é {min(n)}')
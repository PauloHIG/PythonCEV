#sortear nomes em ordem
from random import choice,shuffle
def solução1():
	nomes = ['Primeiro','Segundo','Terceiro','Quarto']

	print('Ordem original')
	print(nomes)

	nomer = nomes#lista de reserva
	for nome in nomes:
		nomeA = choice(nomer)
		nomer.remove(nomeA)
		nomes.append(nomeA)

	print('Nova ordem')
	print(nomes)

def soluçãocerta():
	nomes = ['Ana','José','Paula','Pedro']
	print('Nomes dos alunos:\n{}'.format(nomes))
	shuffle(nomes)
	print('A ordem de apresentação será:\n{}'.format(nomes))

soluçãocerta()
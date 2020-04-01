#Escolher um aluno aleatoriamente
def função():
	import random
	lista_de_nome = []
	i=1
	while i<5:
		lista_de_nome.append(input('Digite o nome do {}º aluno: '.format(i)))
		i+=1
	print('\n O aluno sorteado foi:{}'.format(random.choice(lista_de_nome)))

função()
#apenas para testar, criei uma função com acentos brasileiros e descobri que posso importar dentro de uma função
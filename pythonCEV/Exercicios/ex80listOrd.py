'''Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.'''
#reciclei de outro exercício
def RecNum():
	while True:
		try:
			n = int(input('Digite um valor: '))
		except:
			print('ocorreu um erro, tente novamente')
			continue
		break
	return n
lista = []

for i in range(5):
	n = RecNum()
	lista.append(n)

	#tentativa de quicksort
	pivo = 0
	pivo2 = len(lista)-1
	t=0
	for i in range(len(lista)):
		while pivo<pivo2:
			if lista[pivo]>lista[pivo2]:
				t = lista[pivo]
				lista[pivo] = lista[pivo2]
				lista[pivo2] = t
			pivo2-=1
		pivo = i
		pivo2 = len(lista)-1
	#não sei se dá pra chamar de quicksort, mas funcionou
	if n == max(lista):
		print(f'O {n} foi inserido na última posição')
	elif lista.index(n) == 0:
		print(f'O {n} foi inserido na primeira posição')
	else:
		print(f'O {n} foi inserido na posição{lista.index(n)}')
print(f'lista ordenada: {lista}')
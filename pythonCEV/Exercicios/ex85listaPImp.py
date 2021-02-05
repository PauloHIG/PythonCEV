'''Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista 
única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.'''
def Recint():
	while True:
		try:
			n = int(input(f'Digite o {i+1} número: '))
		except:
			print('Ocorreu um erro, tente novamente')
			continue
		break
	return n

lista = [[],[]]
for i in range(7):
	n = Recint()
	if n %2==0:
		lista[0].append(n)
	else:
		lista[1].append(n)
print(f'Números pares {sorted(lista[0])}')
print(f'Números impares{sorted(lista[1])}')
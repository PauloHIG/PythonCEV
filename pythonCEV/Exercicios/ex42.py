'''Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes'''
A=int(input('Digite o primeiro lado do triângulo: '))
B=int(input('Digite o segundo lado do triângulo: '))
C=int(input('Digite o terçeiro lado do triângulo: '))

if ((A + B) > C) and ((A + C) > B) and ((C + B) > A):
	if (A == B == C):
		tipo = 'EQUILÁTERO'
	elif (A == B != C) or (A == C != B) or (C == B != A):#e não é que funciona?
		tipo = 'ISÓSCELES'
	elif A!= B!= C:
		tipo = 'ESCALENO'
	print('As três retas podem formar um triângulo do tipo {}'.format(tipo))
else:
	print('As três retas não podem formar um triângulo')


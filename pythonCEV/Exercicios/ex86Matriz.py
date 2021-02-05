'''Exercício Python 086: Crie um programa que declare uma 
matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
 No final, mostre a matriz na tela, com a formatação correta.'''
matriz=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(1,4):
	for j in range(1,4):
		matriz[i-1][j-1]= int(input(f'Digite um valor para a posição {i}-{j} da matriz: '))
for linha in matriz:
	for coluna in linha:
		print(f'{coluna:4}',end='')
	print('')

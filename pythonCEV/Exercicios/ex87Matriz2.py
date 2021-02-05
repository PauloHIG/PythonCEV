'''Exercício Python 087: Aprimore o desafio anterior, mostrando no final: 
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''
matriz=[[1,2,3],[4,5,6],[7,8,9]]
def Recint(i,j):
	while True:
		try:
			n = int(input(f'Digite um valor para a posição {i}-{j} da matriz: '))
		except:
			print('Ocorreu um erro, tente novamente')
			continue
		break
	return n

for i in range(1,4):
	for j in range(1,4):
		matriz[i-1][j-1] = Recint(i,j)

for linha in matriz:
	for coluna in linha:
		print(f'|{coluna:5}|',end='')
	print('')

soma = 0
for ele in matriz:
	for num in ele:
		if num % 2 == 0:
			soma += num
print(f'Soma de todos os valores pares digitados = {soma}')
soma=0
for i in range(3):
	soma += matriz[i][2]
print(f'Soma de todos os valores da terceira coluna = {soma}')
print(f'Maior valor da segunda linha = {max(matriz[1])}')
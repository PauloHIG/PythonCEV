#!!!INCOMPLETO!!!
#Jogo da Velha
def verTab(lista):
	for i in range(3):
		if tabuleiro[i][0] == 'X' and tabuleiro[i][0] == tabuleiro[i][1] and tabuleiro[i][1] == tabuleiro[i][2] and tabuleiro[i][0] == tabuleiro[i][2]:
			print('X venceu')
		elif tabuleiro[i][0] == 'O' and tabuleiro[i][0] == tabuleiro[i][1] and tabuleiro[i][1] == tabuleiro[i][2] and tabuleiro[i][0] == tabuleiro[i][2]:
			print('O venceu')
		elif tabuleiro[0][i] == 'X' and tabuleiro[0][i] == tabuleiro[1][i] and tabuleiro[1][i] == tabuleiro[2][i] and tabuleiro[0][i] == tabuleiro[2][i]:
			print('X venceu')
		elif tabuleiro[0][i] == 'O' and tabuleiro[0][i] == tabuleiro[1][i] and tabuleiro[1][i] == tabuleiro[2][i] and tabuleiro[0][i] == tabuleiro[2][i]:
			print('O venceu')
		else:
			print('nem linha e nem coluna')
def verDiagonais(lista):
	print('')




#criação do Tabuleiro
tabuleiro = [[],[],[]]
for i in range(3):
	for j in range (3):
		tabuleiro[i].append(0)


#inserção de valores de vitoria para teste
for cont in range(3):
	tabuleiro[i][cont]='X'

	

#mostrando o tabuleiro
for linhas in tabuleiro:
	print(linhas)
verTab(tabuleiro)
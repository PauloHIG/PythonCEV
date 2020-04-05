#!!!INCOMPLETO!!!
#Jogo da Velha
def verTab(tabuleiro):
	for i in range(3):
		if tabuleiro[i][0] == 'X' and tabuleiro[i][0] == tabuleiro[i][1] and tabuleiro[i][1] == tabuleiro[i][2] and tabuleiro[i][0] == tabuleiro[i][2]:
			print('X venceu')
		elif tabuleiro[i][0] == 'O' and tabuleiro[i][0] == tabuleiro[i][1] and tabuleiro[i][1] == tabuleiro[i][2] and tabuleiro[i][0] == tabuleiro[i][2]:
			print('O venceu')
		elif tabuleiro[0][i] == 'X' and tabuleiro[0][i] == tabuleiro[1][i] and tabuleiro[1][i] == tabuleiro[2][i] and tabuleiro[0][i] == tabuleiro[2][i]:
			print('X venceu')
		elif tabuleiro[0][i] == 'O' and tabuleiro[0][i] == tabuleiro[1][i] and tabuleiro[1][i] == tabuleiro[2][i] and tabuleiro[0][i] == tabuleiro[2][i]:
			print('O venceu')

def verDiagonal(lista):
	contx=0
	conty=0
	for i in range(3):
		if lista[i][i] == 'X':
			contx+=1
		if lista[i][i] == 'O':
			conty+=1

	if contx ==3:
		print('X venceu')
	elif conty ==3:
		print('O venceu')

def verDiagonal2(lista):
	contx=0
	conty=0
	for i in range(3):
		for j in range(3):
			if i+j==2:
				if lista[i][j] == 'X':
					contx+=1
				if lista[i][j] == 'O':
					conty+=1
	if contx ==3:
		print('X venceu')
	elif conty ==3:
		print('O venceu')

#criação do Tabuleiro
tabuleiro = [[],[],[]]
for i in range(3):
	for j in range (3):
		tabuleiro[i].append(0)


#inserção de valores de vitoria para teste
for cont in range(3):
	tabuleiro[cont][cont]='O'

for i in range(3):
		for j in range(3):
			if i+j==2:
				tabuleiro[i][j]='O'
	

#mostrando o tabuleiro
for linhas in tabuleiro:
	print(linhas)

verTab(tabuleiro)
verDiagonal(tabuleiro)
verDiagonal2(tabuleiro)
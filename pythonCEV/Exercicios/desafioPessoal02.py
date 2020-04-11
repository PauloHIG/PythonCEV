#!!!INCOMPLETO!!!
#Jogo da Velha
def verLinhaColuna(tabuleiro:list):
	for i in range(3):
		if tabuleiro[i][0] == 'X' and tabuleiro[i][0] == tabuleiro[i][1] and tabuleiro[i][1] == tabuleiro[i][2] and tabuleiro[i][0] == tabuleiro[i][2]:
			return 'X venceu'
			break
		elif tabuleiro[i][0] == 'O' and tabuleiro[i][0] == tabuleiro[i][1] and tabuleiro[i][1] == tabuleiro[i][2] and tabuleiro[i][0] == tabuleiro[i][2]:
			return 'O venceu'
			break
		elif tabuleiro[0][i] == 'X' and tabuleiro[0][i] == tabuleiro[1][i] and tabuleiro[1][i] == tabuleiro[2][i] and tabuleiro[0][i] == tabuleiro[2][i]:
			return 'X venceu'
			break
		elif tabuleiro[0][i] == 'O' and tabuleiro[0][i] == tabuleiro[1][i] and tabuleiro[1][i] == tabuleiro[2][i] and tabuleiro[0][i] == tabuleiro[2][i]:
			return 'O venceu'
			break
def verDiagonal(lista:list):
	contx=0
	conty=0
	for i in range(3):
		if lista[i][i] == 'O':
			conty+=1
	if contx ==3:
		return 'X venceu'
	elif conty ==3:
		return 'O venceu'
def verDiagonal2(lista:list):
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
		return 'X venceu'
	elif conty ==3:
		return 'O venceu'
def verVelha(lista:list):
	resto = 0
	for i in range(3):
		for j in range(3):
			if type(lista[i][j])==int:
				resto += 1
	if resto == 0:
		return 'Velha!'
def verTudo(lista:list):
	msg=None
	if msg == None:
		msg = verLinhaColuna(lista)
		if msg == None:
			msg = verDiagonal(lista)
			if msg == None:
				msg = verDiagonal2(lista)
				if msg == None:
					msg = verVelha(lista)
		
	return msg
def insereLetras(linhas:list,jogada):
	#todo esse código aqui é para garantir que os jogadores só digitem números e 1 a 9 sem interromper o programa 
	while True:
		pos = input('Digite a posição linha pra colocar {}(1-9): '.format(jogada))
		try:
			pos = int(pos)#verifica se o valor é inteiro
		except:
			print('Somente números inteiros de 1 a 9')
			continue #não permite que o código continue executando mesmo com o erro, o que faz isso é o pass
		if pos<1 or pos>9:
			print('Somente números de 1 a 9')
			continue
		break
	#não consegui pensar em outra maneira de converter os números de 1 a 9 para as posições da matriz
	if pos==7:
		i=0
		j=0
	elif pos==8:
		i=0
		j=1
	elif pos==9:
		i=0
		j=2
	elif pos==4:
		i=1
		j=0
	elif pos==5:
		i=1
		j=1
	elif pos==6:
		i=1
		j=2
	elif pos==1:
		i=2
		j=0
	elif pos==2:
		i=2
		j=1
	elif pos==3:
		i=2
		j=2
	if type(tabuleiro[i][j])==int:
		tabuleiro[i][j] = jogada
	else:
			print('Posição já preenchida')
def insereRandom(linhas:list):
	print('nada ainda')
def renovaTabuleiro(lista:list):
	cont=1
	'''como os botões numericos do nosso teclado são de baixo para cima, eu tive que preencher o tabuleiro desse jeito
		ao invés de um simples for i in range(3):, a idéia é facilitar o jogo usando apenas o teclado'''
	for i in range(2,-1,-1):
		for j in range (3):
			lista[i].append(cont)
			cont+=1
#criação do Tabuleiro
tabuleiro = [[],[],[]]
renovaTabuleiro(tabuleiro)

msg = None
vez = 'X'
while msg==None:
	for linhas in tabuleiro:
		for colunas in linhas:
			print('|', colunas,'|',end='')
		print('')
	insereLetras(tabuleiro,vez)
	if vez == 'X':
		vez = 'O'
	else:
		vez ='X'
	msg=verTudo(tabuleiro)

print(msg)

for linhas in tabuleiro:
		for colunas in linhas:
			print('|', colunas,'|',end='')
		print('')
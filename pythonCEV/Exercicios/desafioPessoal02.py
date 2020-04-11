#!!!INCOMPLETO!!!
#Jogo da Velha
from random import randint
import sys
def verLinhaColuna(lista:list):
	for i in range(3):
		if lista[i][0] == 'X' and lista[i][0] == lista[i][1] and lista[i][1] == lista[i][2] and lista[i][0] == lista[i][2]:
			return 'X'
		elif lista[i][0] == 'O' and lista[i][0] == lista[i][1] and lista[i][1] == lista[i][2] and lista[i][0] == lista[i][2]:
			return 'O'
		elif lista[0][i] == 'X' and lista[0][i] == lista[1][i] and lista[1][i] == lista[2][i] and lista[0][i] == lista[2][i]:
			return 'X'
		elif lista[0][i] == 'O' and lista[0][i] == lista[1][i] and lista[1][i] == lista[2][i] and lista[0][i] == lista[2][i]:
			return 'O'
def verDiagonal(lista:list):
	conty=0
	contx=0
	for i in range(3):
		if lista[i][i] == 'O':
			conty+=1
		elif lista[i][i]=='X':
			contx+=1
	if contx ==3:
		return 'X'
	elif conty ==3:
		return 'O'
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
		return 'X'
	elif conty ==3:
		return 'O'
def verVelha(lista:list):
	resto = 0
	for i in range(3):
		for j in range(3):
			if type(lista[i][j])==int:
				resto += 1
	if resto == 0:
		return 'Ninguém'
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
def insereJogada(linhas:list,jogada):
	while True:
		#esse código aqui é para garantir que os jogadores só digitem números e 1 a 9 sem interromper o programa 
		while True:
			try:
				pos = int(input('Digite a posição linha pra colocar {}(1-9): '.format(jogada)))#verifica se o valor é inteiro,
			except:
				print('Somente números de 1 a 9')
				continue #não permite que o código continue executando mesmo com o erro, o que faz isso é o pass
			if pos<1 or pos>9:
				print('Somente números de 1 a 9')
				continue
			break
		#não consegui pensar em outra maneira de converter os números de 1 a 9 para as posições da matriz
		if pos==1:
			i=2
			j=0
		elif pos==2:
			i=2
			j=1
		elif pos==3:
			i=2
			j=2
		elif pos==7:
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
		if type(tabuleiro[i][j])==int:
			tabuleiro[i][j] = jogada
			break
		else:
				print('Posição já preenchida')
def inserePC(linhas:list,jogada):
	print('PC está escolhendo uma posição aleatoria')
	while True:	
		pos = randint(1,9)
		if pos==1:
			i=2
			j=0
		elif pos==2:
			i=2
			j=1
		elif pos==3:
			i=2
			j=2
		elif pos==7:
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
		if type(tabuleiro[i][j])==int:
			tabuleiro[i][j] = jogada
			break
def renovaTabuleiro(lista:list):
	cont=1
	'''como os botões numericos do nosso teclado são de baixo para cima, eu tive que preencher o tabuleiro desse jeito
		ao invés de um simples for i in range(3):, a idéia é facilitar o jogo usando apenas o teclado'''
	for i in range(2,-1,-1):
		for j in range (3):
			lista[i][j]=cont
			cont+=1
def exibir(lista:list):
	for linhas in lista:
			for colunas in linhas:
				print('|', colunas,'|',end='')#ok, só economizei umas 3 linhas, queria deixar o código mais limpo
			print('')
#criação do Tabuleiro
tabuleiro = [[7,8,9],[4,5,6],[1,2,3]]
msg = None
vez = 'X'
pontX=0
pontO=0
#loop do jogo
while True:
	while msg==None:
		exibir(tabuleiro)
		insereJogada(tabuleiro,vez)
		if vez == 'X':
			vez = 'O'
		else:
			vez ='X'
		msg=verTudo(tabuleiro)
	exibir(tabuleiro)
	#mensagens caso uma partida termine
	if msg=='X':
		pontX+=1
		print('{} venceu!'.format(msg))
	elif msg=='O':
		pontO+=1
		print('{} venceu!'.format(msg))
	else:
		print('Velha!')
	print('Placar: \nX:{} O:{}'.format(pontX,pontO))
	#decisão para continuar no loop
	while True:
		escolha=input('Quer continuar:(s/n): ')
		if escolha in('s','n','S','N'):
			break
		else:
			print('Somente S(Sim) ou N(Não)')
	if escolha == 'n':
		print('Saindo...')
		break
	elif escolha == 's':
		renovaTabuleiro(tabuleiro)
		msg=None
sys.exit()
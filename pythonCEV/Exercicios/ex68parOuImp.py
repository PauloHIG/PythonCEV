#67 jogo de par ou impar, só acaba quando o usuário perder e conta quantas vezes o usuario venceu
from random import randint

def escJogado():
	while True:
		jogador = input('\nVocê quer ser par ou ímpar?(P/I) ')
		if jogador == '':#pra impedir o usuário de digitar nada, é a primeira verificação que devo fazer
			print('Digite algo')
			continue
		if jogador not in 'PpIi':#por ultimo a condição pra quebrar o while
			print('Somente P(par) ou I(impar)')
			continue
		break

	return jogador
def digitaNu():
	while True:
		try:
			numJog = int(input('Digite o seu número: '))
		except:
			print('tente novamente')
			continue
		break
	return numJog

vitJog = 0
while True:
	escJogador = escJogado()#ps,o nome da função nunca deve ser o mesmo da variável
	numPC = randint(1,10)
	numJog = digitaNu()

	print(f'O numero do PC é {numPC}')
	print('Resultado:\n')
	print(f'A soma deu {numJog+numPC}',end=' ')
	if (numPC+numJog)%2 == 0:
		if escJogador in 'Pp':
			print('Jogador venceu')
			vitJog+=1
		else:
			print('PC venceu')
			break
	else:
		if escJogador in 'Ii':
			print('Jogador venceu')
			vitJog+=1
		else:
			print('PC venceu')
			break
print(f'Você venceu {vitJog} vezes')
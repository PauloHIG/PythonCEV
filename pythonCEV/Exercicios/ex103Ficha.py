'''Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador 
e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado 
corretamente.'''
def ficha(nome=None,gols=None):
	if nome:
		print(f'Nome: {nome}')
	else:
		print('Nome: desconhecido')
	if gols:
		print(f'Nº de gols marcados :{gols}')
	else:
		print('Nº de gols marcados : desconhecido')


nome = input('Nome do jogador: ')
try:#precisei fazer isso, por algum motivo o int(input()) não está aceitando nulo como resposta
	gols = int(input('Quantidade de gols marcados: '))
except:
	gols = None
ficha(nome,gols)
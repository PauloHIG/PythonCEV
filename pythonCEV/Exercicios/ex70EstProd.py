'''Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos. 
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. '''

#reciclado do exercício anterior
def escSN():
	while True:
		resp = input('Quer continuar? (S/N): ')
		if resp not in ('SsNn'):
			print('aperte enter ou digite S(sim) ou N(não)')
			continue
		break
	return resp
def precoIn():
	while True:
		try:
			preco = float(input('Digite o preço do produto R$: '))
		except:
			print('Algo deu errado, tente novamente, use ponto no lugar da vírgula')
			continue
		if preco <=0:
			print('Eita promoção boa hein?')
			continue
		break
	return preco

total = maisMil = 0
maisBp = 0 #preco do mais barato
maisBn = '' #nome do mais barato
while True:
	nome = input('Digite o nome do produto: ')
	preco = precoIn()
	if maisBp == 0 or maisBp > preco:#no ex 65, usei dois ifs desnecessariamente messa mesma situação, basta usar um or
		maisBp = preco
		maisBn = nome

	if preco > 1000:
		maisMil +=1
	total+=preco
	con = escSN()
	if con.lower() == 'n':
		break
print('Estatísticas')
print(f'Foi gasto um total de R${total:.2f}\n{maisMil} produtos custam mais de 1000R$\n{maisBn} é o produto mais barato')
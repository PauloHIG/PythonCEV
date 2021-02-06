'''Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em 
um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. 
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''
from datetime import datetime

traba = dict()
def RecAno():
	while True:
		try:
			anasc = int(input(''))
		except:
			print('Ocorreu um erro, tente novamente, digite apenas o ano ')
			continue
		if anasc > datetime.now().year:
			print('Digite um ano válido')
			continue
		break
	return anasc
def recFloat():
	while True:
		try:
			flo = float(input())
		except:
			print('Ocorreu um erro')
			continue
		break
	return flo
traba['Nome'] = input('Nome: ')

#calculando a idade
print('Ano de nascimento',end=': ')
ano = RecAno()
traba['Idade'] = (datetime.now().year) - ano

traba['CTPS'] = int(input('CTPS: '))
#se CTPS for maior que 0
if traba['CTPS'] > 0:
	print('Ano de contratação: ', end='')
	traba['Contratação']= RecAno()
	print('Salário: ',end='')
	traba['Salário R$'] = recFloat()
	traba['Idade da aposentadoria'] =((datetime.now().year) - ano) + (traba['Contratação']+35-(datetime.now().year))
	#a formula calcula baseado apenas em que você tem que ter 35 anos de trabalho

	for chave,valor in traba.items():
		print(f'{chave:23} : {valor}')
else:
	for chave,valor in traba.items():
		print(f'{chave:6} : {valor}')
from datetime import datetime
'''Exercício Python 101: Crie um programa que tenha uma função chamada voto()
que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.'''
def voto(anonasc):
	idade = datetime.now().year - anonasc
	if idade <16:
		return 'VOTO NEGADO'
	elif idade <18:
		return 'VOTO OPCIONAL'
	else:
		return 'VOTO OBRIGATÓRIO'
def recIdade():
	while True:
		try:
			ano = int(input('Digite o seu ano de nascimento: '))
		except:
			print('Digite um ano válido')
			continue
		if ano >datetime.now().year:
			print('Digite um ano válido')
			continue
		break
	return ano
print(voto(recIdade()))
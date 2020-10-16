'''Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que
 leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER'''

from datetime import datetime
#relembrando como usar o datetime so para pegar o ano atual
ano = datetime.now().year
while True:
	try:
		anonasc = int(input('Digite o ano de nascimento do atleta: '))
	except:
		print('por favor, somente o ano, sem meses e dias ')
		continue
	if anonasc > ano:
		print('Digite um ano válido')
		continue
	break
if (ano-anonasc) <= 9:
	clasificacao = 'MIRIM'
elif(ano-anonasc)<=14:
	clasificacao = 'INFANTIL'
elif(ano-anonasc)<=19:
	clasificacao = 'JÚNIOR'
elif(ano-anonasc)<=25:
	clasificacao = 'SÊNIOR'
else:
	clasificacao = 'MASTER'
print('O atleta tem {} anos'.format(ano-anonasc))
print('Classificação:{}'.format(clasificacao))

#ex 32 faça um programa que mostra se um ano é bisexto
'''
Divisível por 4. Sendo assim, a divisão é exata com o resto igual a zero;
Não pode ser divisível por 100. Com isso, a divisão não é exata, ou seja, deixa resto diferente de zero;
Pode ser que seja divisível por 400. Caso seja divisível por 400, a divisão deve ser exata, deixando o resto igual a zero.
'''
from datetime import date
while True:
	try:
		ano = int(input('Digite um ano(0 para o ano atual): '))
	except:
		print('Somente o ano, sem pontos, barras nem vírgulas')
		continue#o continue faz com que o try seja executado quantas vezes for necessário desde que esteja dentro de um loop infinito
	break
if ano == 0:
	ano = date.today().year
if ano%4 == 0 and ano % 100 != 0 or ano % 400 == 0:
	print('{} é um ano é bissexto'.format(ano))
else:
	print('{} não é um ano bissexto'.format(ano))
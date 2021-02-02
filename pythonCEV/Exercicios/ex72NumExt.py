'''Exercício Python 072: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, 
de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''

NumExt = ('zero','um', 'dois', 'três','quatro','cinco','seis','sete','oito','nove','dez',
'onze','doze','treze','catorze','quinze','dezesseis','dezessete', 'dezoito', 'dezenove','vinte')
while True:
	try:
		num = int(input('Digite um numero de 0 a 20:'))
	except:
		print('Ocorreu um erro, tente novamente')
		continue
	if num< 0 or num >20:
		print('Tente novamente, é apenas entre 0 e 20')
		continue
	break
print(f'{num} por extenso é {NumExt[num]}')
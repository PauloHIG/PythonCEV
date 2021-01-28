#ex52 Numeros primos
import colorama
from colorama import init
from termcolor import colored
init()
#por algum motivo preciso, importar tudo isso para as cores funcionarem no terminal do windows usando a função colored
#sim, estou imitando o Curso em vídeo ao usar cores para mostrar se o número é ou não divisível 
while True:
	try:
		numero = int(input('Execute onde as cores possam ser vistas\nDigite um número para verificar se ele é Primo por quais números ele é divisível\n'))
	except:
		print('Somente números inteiros')
		continue
	break
cont = 0
for i in range(1,numero+1):
	if numero % i == 0:
		cont+=1
		print(colored(i,'green'),end=' ')
	else:
		print(colored(i,'yellow'),end=' ')
if cont==2:
	print('O número {} é primo'.format(numero))
else:
	print('O número {} não é primo'.format(numero))
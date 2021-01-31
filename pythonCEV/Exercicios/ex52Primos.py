#ex52 Numeros primos
import colorama
from colorama import init
from termcolor import colored
from sys import exit
init()
#por algum motivo preciso, importar tudo isso para as cores funcionarem no terminal do windows usando a função colored
#sim, estou imitando o Curso em vídeo ao usar cores para mostrar se o número é ou não divisível 

print('Execute onde as cores possam ser vistas, instale o modulo colored\n')
print('Digite um número para verificar se ele é Primo por quais números ele é divisível')

while True:#pro usuário não digitar nada errado no número
	try:
		numero = int(input('número: '))
	except:
		print('\nSomente números inteiros, tente novamente')
		continue
	if numero < 0 :
		print('\nSomente números naturais, tente outro')
		continue
	break

if numero == 0: #pra encerrar o programa caso o número sera 0 
	print('O número {} é composto?'.format(numero))
	exit()#o programa se encerra aqui quando o usuario escolhe 0, porque o 'for' só funciona se o numero for 1 ou mais, porque ele usa a divisão e não se divide por 0

cont = 0
divisiveis = []

#o código abaixo mostra se todos os números de 1 até onde o usuario digitou dividem o numero digitado
for i in range(1,numero+1):#é desse 'for' que eu tô falando
	if numero % i == 0:#o numero não pode ser 0 por causa da divisão
		cont+=1
		print(colored(i,'green'),end=' ')#vai ficar verdinho se o número for divisível por i
		divisiveis.append(i)
	else:
		print(colored(i,'yellow'),end=' ')

if cont==2:#se o numero é divisível apenas por 2 números(1 e ele mesmo) ele é primo
	print('\nO número {} é primo'.format(numero))
elif cont >=1:#1 é excessão por ser um divisor universal
	print('\nO número {} é composto'.format(numero))

print('Ele é divisível pelos numeros abaixo')
for num in divisiveis:
	print(colored(num,'green'),end=' ')
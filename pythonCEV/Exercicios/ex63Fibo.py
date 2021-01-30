#Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 
#Fn = Fn - 1 + Fn - 2
t1 = 1#esse PRECISA começar com 1
t2 = 0#esse PRECISA começar com 0, motivo? fazer os dois primeiros elementos serem 1
t3 = 0
n = int(input('Quantos números de fibonacci você que ver? '))

for i in range(n):
	if i <n-1:
		print(t3,end=',')
	else:
		print(t3, end = '...')
	#tudo isso embaixo é o calculo de fibonacci que eu conseguim usando três variáveis
	t3 = t1 + t2
	temp = t2
	t2 = t3
	t1 = temp
'''Exercício Python 064: Crie um programa que leia vários números inteiros pelo teclado.
 O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
  No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''
re=0
cont = 0
soma=0
while True:
	while True:
		try:
			re = int(input('Digite um número(999 pra sair)'))
		except:
			print('Erro, tente novamente')
			continue
		break
	if re == 999:
		break
	else:
		cont+=1
		soma+=re
		continue
print('Você digitou {} números e a soma deles é {}'.format(cont,soma))
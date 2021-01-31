'''Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''
esco = 's'
maior = menor = somatot = 0
tot = 1
while True:
	while True:
		try:
			n = int(input('Digite o {}º número: '.format(tot)))
		except:
			print('um número inteiro \n \n')
			continue
		break
		
	if tot ==1:
		menor = n
	somatot+=n
	
	if maior < n:
		maior = n
	if menor > n:
		menor = n
	while True:
		esco = input('Quer digitar mais um número?(N pra sair)')
		if esco not in ('sSNn'):
			print('!!ERRO!!\n \n')
			continue
		else:
			break
	if esco in 'sS':
		tot +=1
	else:
		break
print('\n\nO maior número é {}\nO menor número é {}\nE a média entre eles é {}'.format(maior,menor,somatot/tot))
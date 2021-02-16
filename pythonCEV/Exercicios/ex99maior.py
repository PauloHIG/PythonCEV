'''Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu 
programa tem que analisar todos os valores e dizer qual deles é o maior.'''
def maior(* numeros):#com o asterisco, posso colocar um número indefinido de variáveis,e, nesse caso especifico, usar elas como uma lista(desempacotar)
	maior=cont=0
	for n in numeros:
		if cont == 0:#é absolutamente necessário fazer isso, caso o maior número seja menor que 0
			maior = n
		if maior < n:
			maior = n
		cont+=1
	return maior

	
print(maior(-1,-2,-4))
print(maior(6,3,-2,-100))
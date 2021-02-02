'''Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''

num =(int(input('Digite um número: ')),int(input('Digite um número: ')),
	int(input('Digite um número: ')),int(input('Digite um número: ')))

print(f'O 9 apareceu {num.count(9)} vezes')
print(f'O primeiro valor 3 está na posição {num.index(3)}' if 3 in num else 'Não tem o número 3 na tupla')
print('Numeros pares:')
for n in num:
	if n %2 ==0:
		print(n)
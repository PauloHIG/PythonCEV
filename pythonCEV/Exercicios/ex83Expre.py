'''Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo 
deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.'''
exp = input('digite uma expressão matemática qualquer: ')
val = '???'
aberto = 0
for letra in exp:
	if letra ==')' and aberto >0:
		aberto -=1#fechar, só pode fechar se abrir
	if letra =='(':
		aberto +=1#abrir

if exp.count('(') == exp.count(')') and aberto == 0:
	val = 'válida'
else:
	val = 'inválida'
print(f'A expressão é {val}')
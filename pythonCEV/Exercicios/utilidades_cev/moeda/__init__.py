#é aqui dentro do init que coloco as funções que usarei em outro programa
def metade(valor=0,formatado=True):
	fval=valor
	if formatado:
		fval = moeda(valor)
	print(f'A metade de {fval} é {moeda(valor/2)}')
	return valor/2

def dobro(valor=0,formatado=True):
	fval = valor
	if formatado:
		fval = moeda(valor)
	print(f'O dobro de {fval} é {moeda(valor*2)}')
	return valor*2

def aumentar(valor=0,porcentagem=0,formatado=True):
	fval = valor
	if formatado:
		fval = moeda(valor)
	print(f'Aumentando {porcentagem}% de {fval} temos {moeda(valor+(valor*(porcentagem/100)))}')
	return(valor+(valor*(porcentagem/100)))

def diminuir(valor=0,porcentagem=0,formatado=True):
	'''a função recebe três variáveis, o valor, a porcentagem que você quer diminuir
	 e a opção de formatar na moeda brasileira que está ativada por padrão'''
	fval = valor
	if formatado:
		fval = moeda(valor)
	print(f'Diminuindo {porcentagem}% de {fval} temos {moeda(valor-(valor*(porcentagem/100)))}')
	return(valor-(valor*(porcentagem/100)))
	
def moeda(n=0):
	return(f'R$ {n:.2f}'.replace('.',','))

def resumo(valor=0,pormais=0,pormenos=0):
	'''executa todas as funções do modulo, precisando do valor e, na ordem, a porcentagem pra aumentar e a porcentagem pra diminuir\n por padrão, todos os valores são 0'''
	dobro(valor)
	metade(valor)
	aumentar(valor,pormais)
	diminuir(valor,pormenos)

'''
Exercício Python 109: Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais,
informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

Exercício Python 110: Adicione o módulo moeda.py criado nos desafios anteriores, 
uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.

Exercício Python 111: Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. 
Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.
'''
'''Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos
 e vai retornar um dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)

Adicione também as docstrings dessa função para consulta pelo desenvolvedor.'''
def notas(*notas, sit=None):
	'''Esta função recebe várias notas de uma turma inteira, pode-se colocar quantas notas forem necessárias
	pra mostrar a situação geral da sala, deve-se colocar sit=True na chamada da função, mas é opcional
	se eu tivesse usado uma lista no lugar de um parametro de variavel empacotada
	ela retorna um dicionário com os seguintes detalhes: 
	- Quantidade de notas
	- A maior nota
	- A menor nota
	- A média da turma
	- A situação (opcional)
	'''
	info = {}
	info['Quantidade de notas'] = len(notas)
	info['Maior nota'] = max(notas)
	info['Menor nota'] = min(notas)
	info['Media da turma'] = sum(notas)/len(notas)
	if sit:
		if (sum(notas)/len(notas)) <5:
			info['Situação'] = 'RUIM'
		elif (sum(notas)/len(notas))<=6:
			info['Situação'] = 'OK'
		elif (sum(notas)/len(notas))<=8:
			info['Situação'] = 'BOA'
		elif (sum(notas)/len(notas))<=10:
			info['Situação'] ='ÓTIMA'
	return info

informações = notas(10,9,sit=True)
print(informações)
help(notas)
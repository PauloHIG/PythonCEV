'''022: Crie um programa que leia o nome completo de uma pessoa e mostre: 
O nome com todas as letras maiúsculas e minúsculas. 
Quantas letras ao todo (sem considerar espaços). 
Quantas letras tem o primeiro nome.'''
def exercicio():
	nome = 'Paulo Henrique Ito Gabriel'
	print(nome.upper())
	print(nome.lower())
	nomer = nome.replace(' ','')#gambiarra pra remover o espaço
	print('Seu nome tem {} letras sem contar com os espaços'.format(len(nomer)))
	nomer = nome.split()
	print('Seu primeiro nome tem {} letras'.format(len(nomer[0])))
def CeV():
	nome = str(input('Digite seu nome: ')).strip()#o strip já elimina os espaços do coneço e do fim
	print(nome.upper())
	print(nome.lower())
	print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))#olha o esquema aí para eliminar todos os espaços na contagem
	print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))#ao encontrar a posição do primeiro ' ' a contagem para, a posição do espaço equivale à quantidade de letras da primeira palavra 
exercicio()
CeV()
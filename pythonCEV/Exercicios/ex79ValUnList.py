'''ex79 
Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente. 
fazer lista a=b cria duas listas ligadas, a solução pra isso é o fatiamento com a=b[:] por exemplo
'''
def RecNum():
	while True:
		try:
			n = int(input('Digite um valor: '))
		except:
			print('ocorreu um erro, tente novamente')
			continue
		break
	return n
def DecCon():
	while True:
		con = input('Quer continuar?(N pra sair)')
		if con not in 'NnSs':
			print('Digite S ou N apenas')
			continue
		break
	return con
lista=[]

while True:
	num = RecNum()
	if num not in lista:
		lista.append(num)
	else:
		print('Já tem esse número na lista')
	cont = DecCon()
	if cont.lower() == 'n':
		break
print(sorted(lista))
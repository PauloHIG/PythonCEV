def cabeçalho(texto):
	print('-'*36)
	print(texto.center(36))#essa função vai ser bem útil daqui pra qualqer menu que eu fizer no cmd
	print('-'*36)
def menu(lista):
	for i in range(len(lista)):
		print(f'{i+1} - {lista[i]}')#vai mostrar a opção e seu número, na ordem em que aparecem na lista, inspirado pelo curos em vídeo
	return len(lista)#pra usar na função abaixo, pois preciso que o número máximo aceitado pelo programa seja exatamente o da ultima opção
def recopcao(opFinal):
	'''recebe a escolha do usuario e retorna seu valor, precisa do número retornado pela função menu() deste modulo'''
	while True:
		try:
			opc = int(input('->'))
		except:
			print('Digite uma opção válida')
			continue
		if opc<1 or opc>opFinal:
			print(f'Somente uma das {opFinal} opções')
			continue
		break
	return opc
def menucompleto(opções):#pro codigo principal ficar mais bonito
	cabeçalho('Menu')
	opc = menu(opções)#retorna o tamanho da lista
	esc = recopcao(opc)#usa o tamanho da lista para definir o maior numero que o usuario pode digitar e retorna o numero que o usuario escolheu
	return esc
#tabuada
def tabuada(n):
	print("-"*12) #pode se multiplicar strings
	print("tabuada do ",n)
	for i in range(1, 11):
		print('{} X {:2} = {}'.format(n, i, n * i))#o {:2} cria um espaço de 2 dígitos para alinhar com os que só tem 1
	print("-"*12)

ta=int(input('Digite o número para ver sua tabuada: '))
tabuada(ta)

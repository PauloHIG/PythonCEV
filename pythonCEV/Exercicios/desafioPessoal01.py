#Criar uma calculadora usando apenas soma
#subtração é permitida, mas será usada como uma soma com um número negativo
#!!!INCOMPLETO!!!
def multiplicação(n1,n2):
	if type(n2) is int: 
		i=1
		nr=n1
		if n2 >0:
			while i<n2:
				nr = nr+n1
				i+=1
		elif n2<0:
			while i>n2:
				nr = nr+(-n1)
				i-=1
		else:
			nr=0
		return nr
	else:
		print('O multiplicador só pode ser inteiro')

def restDivisão(n1,n2):
	cont=0
	if n2>0:
		while n1>=n2:
			n1 = n1+(-n2)
			cont+=1
		if n1 >0:
			return n1
		else:
			print ('A divisão não têm resto')
			return n1
	else:
		print('Só use valores inteiros e o divisor só pode ser maior que 0')

def divisão(n1,n2):
	cont=0
	if n2>0:
		while n1>=n2:
			n1 = n1+(-n2)
			cont+=1
		return cont
	else:
		print('Só use valores inteiros e o divisor só pode ser maior que 0')

re = multiplicação(-12.34,10)
print('multiplicação = {:.2f}'.format(re))
re = divisão(11,2)
print("Divisão = ",re)
re = restDivisão(11,2)
print('Resto da divisão = {}'.format(re))

#Criar uma função de multiplicação usando apenas soma
def multiplicação(n1,n2):
	i=1
	nr=n1
	while i<n2:
		nr = nr+n1
		i+=1
	return nr
resultado = multiplicação(3,100)
print(resultado)

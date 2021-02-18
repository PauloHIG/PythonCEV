#é aqui dentro do init que coloco as funções que usarei em outro programa
def metade(valor=0):
	return valor/2
def dobro(valor=0):
	return valor*2
def aumentar(valor=0,porcentagem=0):
	return(valor+(valor*(porcentagem/100)))
def diminuir(valor=0,porcentagem=0):
	return(valor-(valor*(porcentagem/100)))
def moeda(n=0):
	print(f'R$ {n:.2f}'.replace('.',','))
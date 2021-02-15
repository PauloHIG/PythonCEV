#ex96 area do terreno
def calc_area(largura,cumprimento):
	return largura*cumprimento
la = float(input('Digite a largura do terreno(m) '))
cpr = float(input('Digite o cumprimento do terreno(m): '))
print(calc_area(la,cpr))
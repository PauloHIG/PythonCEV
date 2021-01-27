tab = int(input('Qual tabuada você quer saber? '))
for i in range(1,11):
	print('{} X {:2} = {}'.format(tab,i,tab*i))
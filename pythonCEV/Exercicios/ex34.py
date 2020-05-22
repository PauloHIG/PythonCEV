#ex 34 aumento, se o salario for >=1250 o aumento é de 10%, para salários menores, o aumento é de 15%
while True:
	#loop para o usuario não travar o programa, ainda não sei uma maneira melhor de fazer isso
	try:
		sal = float(input('Digite o salário do funcionario: '))
	except:
		print('Somente o valor do salário')
		continue
	if sal <= 0:
		print('Digite um salário válido')
		continue
	break

if sal > 1250:
	aumento = 10
else:
	aumento = 15
nsal = sal + (sal*(aumento/100))
print('O antigo salario era {:.2f}R$ com o aumento de {}% o salário agora é {:.2f}R$'.format(sal,aumento,nsal))
'''
Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros'''

#while só pra o usuario digitar exatamente o que eu quero
preço = 4000.00
while True:
	try:
		preço = float(input('Digite o preço das compras: '))
	except:
		print('Por favor, digite apenas o número (valor da compra) e use vírgula no lugar do ponto')
		continue
	break
print('Preço R$ {:.2f}'.format(preço))
print('''Escolha uma forma e pagamento
	[1] à vista dinheiro ou cheque: 10% de desconto
	[2] à vista no cartão: 5% de desconto
	[3] em até 2x no cartão: preço formal
	[4] 3x ou mais no cartão : 20% de juros 
	''')
#limitando as escolhas do usuário com a verificação, para não dar erro
while True:
	try:
		escolha = int(input('Escolha uma forma de pagamento: '))
	except:
		print('Por favor, digite apenas um número correspondente á sua escolha, não é necessario mais do que isso')
		continue
	if escolha < 1 or escolha > 4:
		print('Por favor, escolha somente entre as 4 opções, digitando um unico número de 1 a 4 para escolher')
		continue
	break

if escolha == 1:
	preço = preço - (preço/10)#dividindo por 10, pego 10%
	print('Você escolheu pagar com dinheiro ou cheque, o preço final é de R$ {:.2f}'.format(preço))

elif escolha == 2:
	preço = preço - (preço/20)#dividindo por 20, pego 5%
	print('Você escolheu pagar à vista no cartão, o preço final é de R$ {:.2f}'.format(preço))

elif escolha == 3:
	print('você escolheu pagar 2x no cartão, o preço será R$ {:.2f}'.format(preço))

elif escolha == 4:
	#boa e velha verificação de input do usuário
	while True:
		try:
			parcelas = int(input('em quantas vezes?\n'))
		except:
			print('Só a quantidade de vezes em que você quer parcelar no cartão')
			continue
		if parcelas <=2:
			print('Você escolheu a opção de 3 ou mais')
			continue
		break
	#calculo do valor de cada parcela, mas no fim das contas só adiciona 20% ao valor original da compra
	cadaParcela = (preço/parcelas) + ((preço/parcelas)/5)# a divisão por 5 é uma maneira de calcular 20%, os calculos precisam ser feitos com o preço dividido pelo número de parcelas
	novopreço = cadaParcela*parcelas
	print('Você pagará em {} parcelas de R$ {:.2f}'.format(parcelas,cadaParcela))
	print('O preço final será de R$ {:.2f}'.format(novopreço))
'''o ideal é uma opção a mais para cancelar a compra e até mesmo
 trocar a forma de pagamento com a opção de confirmar pagamento ou trocar a forma de pagamento'''
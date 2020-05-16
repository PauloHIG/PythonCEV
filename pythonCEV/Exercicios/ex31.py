#ex 31 perguntar a distacia de uma viagem em KM, cobrando 0,50 centavos por km para viagens com menos de 200km e 0,45 para viagens mais longas
while True:
	try:
		dis = float(input('Digite a distância da sua viagem(km)'))
	except:
		print('Somente um valor em quilômetros')
		continue
	break
if dis <= 200:
	preço = dis*0.50
else:
	preço = dis*0.45
print('O preço da viagem será {:.2f}R$'.format(preço))
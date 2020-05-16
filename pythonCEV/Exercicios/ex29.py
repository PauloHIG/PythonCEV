vel = int(input('Digite uma velocidade de um carro como exemplo(km):'))
if vel >80:
	multa = 7*(vel-80)
	print('Multado!! você ultrapassou o limite de 80km/h, vai receber uma multa de {:.2f} R$'.format(multa))
elif vel == 80:
	print('Você está bem no limite! sua velocidade atual é 80km/h')
else:
	print('Sua velocidade atual é de {}km/h'.format(vel))
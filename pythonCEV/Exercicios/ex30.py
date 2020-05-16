#mostrar se um numero é par ou ímpar
print('Par ou ímpar')
def exercicio():
	while True:
		try:
			n = int(input('Digite um numero inteiro: '))
		except:
			print('Somente um número inteiro')
			continue
		break
	if n%2==0:
		print(n,' é um número par')
	else:
		print(n,' é um número ímpar')
exercicio()
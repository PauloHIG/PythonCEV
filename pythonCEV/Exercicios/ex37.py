#converter decimal para binario, octal e hexadecimal


#Para converter um número decimal para binário, basta realizar divisões sucessivas do número decimal por 2 (base do sistema binário).
def dectobin(numero):
	bina = ''
	resto = numero
	while resto >=1:
		#ou seja, ficarei fazendo várias divisões com o resultado das divisões anteriores até que o resultado seja 1
		bina = bina + str(resto%2)
		resto = resto//2
	bina = bina[::-1]#inverte o texto
	return bina

while True:
	try:
		numero = int(input('Digite um numero inteiro: '))
	except:
		print('somente um número inteiro')
		continue
	break

while True:
	print('''Qual conversão você quer fazer?
1 - Binario
2 - Octal
3 - Hexadecimal''')
	opcao = int(input(''))
	if opcao == 1:
		print('{} para binário é:{}'.format(numero,dectobin(numero)))
		break
	elif opcao ==2:
		print('{} para octal é:{}'.format(numero,oct(numero)[2:]))
		break
	elif opcao == 3:
		print('{} para hexadecimal é: {}'.format(numero,hex(numero)[2:]))
		break
	else:
		print('Opção inválida')
#essa pequena biblioteca foi criada para caso eu precise de funções que validem dados digitados pelo usuario, por exemplo, receber um numero inteiro pelo usuario sem dar erro
def recNome(frase='->',fraseErro='Nada foi digitado'):
	'''Todas as funçoes aqui tem por padrão, uma frase para indicar o que o usuario tem que digitar e uma frase de erro, na chamada ta função, pode-se colocar a frase que for necessária'''
	while True:
		nome = input(frase)
		if nome == '':
			print(fraseErro)
			continue
		break
	return nome
def recIdade(frase='->',fraseErro='Ocorreu um erro'):
	'''Todas as funçoes aqui tem por padrão, uma frase para indicar o que o usuario tem que digitar e uma frase de erro em caso de ua excessão, na chamada ta função, pode-se colocar a frase que for necessária'''
	while True:
		try:
			idade = int(input(frase))
		except:
			print(fraseErro)
			continue
		if idade<0:
			print('Digite uma idade valida')
			continue
		break
	return idade
def recInt(frase='->',fraseErro='Ocorreu um erro'):
	'''Todas as funçoes aqui tem por padrão, uma frase para indicar o que o usuario tem que digitar e uma frase de erro, na chamada ta função, pode-se colocar a frase que for necessária'''
	while True:
		try:
			num = int(input(frase))
		except:
			print(fraseErro)
			continue
		break
	return num
def recFloat(frase='->',fraseErro='Ocorreu um erro'):
	'''Todas as funçoes aqui tem por padrão, uma frase para indicar o que o usuario tem que digitar e uma frase de erro, na chamada ta função, pode-se colocar a frase que for necessária'''
	while True:
		try:
			num = float(input(frase))
		except:
			print(fraseErro)
			continue
		break
	return num
def recAnoNasc(frase='->',fraseErro='Ocorreu um erro'):
	'''Todas as funçoes aqui tem por padrão, uma frase para indicar o que o usuario tem que digitar e uma frase de erro, na chamada ta função, pode-se colocar a frase que for necessária'''
	from datetime import datetime
	while True:
		try:
			ano = int(input(frase))
		except:
			print(fraseErro)
			continue
		if ano > datetime.now().year:
			print('Digite um ano de nascimento válido')
			continue
		break
	return ano
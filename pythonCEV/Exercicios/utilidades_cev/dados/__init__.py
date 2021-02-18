'''Exercício Python 112: Dentro do pacote utilidadesCeV que criamos no desafio 111,
temos um módulo chamado dado. Crie uma função chamada leiaDinheiro()
que seja capaz de funcionar como a função imputa(), mas com uma validação de dados para aceitar apenas valores que seja monetários.'''
def validaMoeda():
	'''Tratamento para o usuario digitar um valor válido na moeda,
	 para que o valor possa ser usado para cálculos, a vírgula será substituída pelo ponto'''
	while True:
		valor = input('Digite um valor R$ ')
		try:
			float(valor.replace(',','.').strip())
		except:
			print(f'ERRO {valor.strip()} é inválido, tente novamente \n')
			continue
		break
	return float(valor.replace(',','.').strip())
def ler_int():
	while True:
		try:
			i = int(input(' '))
		except:
			print('Ocorreu um erro, tente novamente')
			continue
		break
	return i
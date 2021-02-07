from statistics import mean
dicio = dict()
dicio['Nome'] = []
dicio['Sexo'] = []
dicio['Idade'] = []
#a primeira coisa que fiz foi esse monte de funções pra não travar o programa caso algo errado seja digitado
def recSex(i):
	while True:
		sex = input(f'Digite o sexo da pessoa {i} (M/F)')
		if len(sex)!=1 or sex not in 'MmFf':
			print('Erro, tente novamente, digite apenas M(masculino) ou F(feminino)')
			continue
		if sex in 'MmFf' and len(sex)==1:
			break
	return sex.upper()
def recIdade(i):
	while True:
		try:
			idade = int(input(f'Digite a idade da pessoa {i}: '))
		except:
			print('Ocorreu um erro, digite apenas a idade')
			continue
		if idade <0:
			print('Digite uma idade válida')
			continue
		break
		idade = idade.upper()
	return idade
def deciCont():
	while True:
		deci = input('Quer continuar?(N pra sair): ')
		if deci not in ('SsnN'):
			print('Ocorreu um erro, digite N pra sair')
			continue
		break
	return deci
def recNome(i):
	while True:
		nome = input(f'Nome da pessoa {i}: ')
		if len(nome) == 0:
			print('Precisa digitar o nome')
			continue
		break
	return nome

i=1 #loop do cadastro, apesar do uso do while, quero usar o contador
while True:
	dicio['Nome'].append(recNome(i))
	dicio['Sexo'].append(recSex(i))
	dicio['Idade'].append(recIdade(i))
	i+=1
	cont = deciCont()
	if cont.lower() =='n':
		break
	print('--'*13)
#exibições
print('--'*13)
qte = len(dicio["Nome"])#preferi colocar em uma varíavel para o pc não ficar refazendo a conta no range
print(f'Quandidade de pessoas cadastradas: {qte}')
medidade = mean(dicio['Idade'])#preferi colocar em uma varíavel para o pc não ficar refazendo a conta no for
print(f'Média de idade: {medidade:.0f}')
print('Mulheres na lista: ')
if 'F' not in dicio['Sexo']:#o primeiro argumento precisa ser uma string nessa situação, is lista in string não fuciona, mas string in lista funciona
	print('Nenhuma')
else:
	for i in range(qte):
		if dicio['Sexo'][i] =='F':
			print(dicio['Nome'][i])
print('Pessoas com idade acima da média: ')
for i in range(qte):
	if dicio['Idade'][i] >medidade:
		print(f'Nome: {dicio["Nome"][i]:10} idade: {dicio["Idade"][i]}')

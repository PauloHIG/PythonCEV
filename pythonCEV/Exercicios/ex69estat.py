'''Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas. 
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. 
No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.'''	
#preferi separar em funções
def escSN():
	while True:
		resp = input('Quer continuar? (S/N): ')
		if resp not in ('SsNn'):
			print('aperte enter ou digite S(sim) ou N(não)')
			continue
		break
	return resp
def cadIdade():
	while True:
		try:
			idade = int(input('Digite a idade da pessoa: '))
		except:
			print('ocorreu um erro, tente novamente')
			continue
		if idade <0:
			print('Digite uma idade válida')
			continue
		break
	return idade
def cadSex():
	while True:
		sex = input('Sexo da pessoa(M/F): ')
		if sex =='':
			print('Digite uma informação válida')
			continue
		if sex not in ('MmFf'):
			print('Digite M(masculino) ou F(feminino)')
			continue
		break
	return sex

MaIdade = 0 #contador de maiores de 18
HomCont = 0 #conta a quantidade de homens
Mvinte =0 #conta a quantidade de mulheres com menos de 20 anos
while True:
	idade = cadIdade()
	sexo = cadSex()
	if idade >18:
		MaIdade+=1
	if sexo.lower() =='m':
		HomCont+=1
	if sexo.lower() == 'f' and idade <20:
		Mvinte +=1
	print('\n')
	escolha = escSN()
	if escolha.lower() == 'n':
		break
print('\nEstatíticas')
print(f'{MaIdade} pessoas com mais de 18 anos \n{HomCont} homens \n{Mvinte} mulheres com menos de 20 anos')
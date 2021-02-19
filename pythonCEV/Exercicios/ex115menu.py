#115 primeiro passo, criar um menu usando modularização
from ex115modulo import *#importa as funções de menu e cabeçalho
from ex115modulo.lerdados import *#biblioteca que meche com arquivos txt, ela não só lê como permite que sejam inserido dados nos arquivos
from validados import recNome,recIdade#validados é a biblioteca que valida diversos tipos de dados, foi feita para estudar mas pode vir a ser bem util pra outras coisas
from time import sleep
opc=-1
while opc!=3:
	opc = menucompleto(['Ver pessoas cadastradas','Cadastrar uma pessoa','sair'])
	if opc == 1:
		cabeçalho(f'Mostrando as pessoas')
		mostra_pessoas('dados')
	elif opc == 2:
		cabeçalho(f'OPÇÃO {opc}')
		escreve_dado('dados',recNome('Digite o nome da pessoa: '),recIdade('Digite a idade da pessoa: '))
	else:
		print('saindo do programa, volte sempre')
	sleep(0.2)
#ex47 soma de numeros impares, multiplos de 3 entre 1 e 500
soma = 0
for i in range(1,501,2):#pulando de 2 em 2 como aprendido no exercio anterior, um trabalho a menos para o processador
	if i % 3 == 0:#com isso, não há necessidade de calcular se o número é impar, por pular de 2 em 2, i sempre será impar
		soma = soma + i
print('A doma dos numeros ímpares e múltiplos de 3 entre 1 e 500 dá {}'.format(soma))
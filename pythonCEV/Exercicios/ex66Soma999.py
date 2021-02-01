#ex 66 

soma = 0
while True:
	while True:
		try:
			n = int(input('Digite um número(999 pra sair): '))
		except:
			print('Ocorreu um erro, tente novamente')
			continue
		break
	if n == 999:
		break
	soma += n
print(f'A soma dos números que você digitou é {soma}')
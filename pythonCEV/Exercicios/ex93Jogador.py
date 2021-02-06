'''Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do 
jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será 
guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''
jogador = dict()
#pra não repetir codigo, fiz essa função
def recInt():
	while True:
		try:
			num = int(input())
		except:
			print('Ocorreu um erro, digite novamente')
			continue
		break
	return num


jogador['Nome'] = input('Nome do jogador: ')

print('Quantidade de partidas: ',end='')
jogador['Nº de partidas'] = recInt()

jogador['Gols'] = []#assim eu adiciono quantos valores eu quiser na lista
for i in range(jogador['Nº de partidas']):
	print(f'Quantidade de gols da {i+1} º partida: ',end='')
	jogador['Gols'].append(recInt())#lembrando que jogador['Gols'] é uma lista agora

jogador['Total de gols'] = sum(jogador['Gols'])#somando os gols

print('-'*12)
for chave,valor in jogador.items():
	print(f'{chave:14}:{valor}')
print('-'*12)
for i in range(jogador['Nº de partidas']):
	print(f'Na partida {i+1} ele fez {jogador["Gols"][i]} gols')
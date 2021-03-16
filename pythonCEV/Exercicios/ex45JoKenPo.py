# jo ken po
from random import randint

print("Jo Ken Po \nEsse jogo terá 5 rodadas e o vencedor será o que tiver vencido mais vezes")
conJ = 0
conPC = 0
for i in range(1, 6):
    jogadas = ["Pedra", "Papel", "Tesoura"]
    # para a escolha do jogador, é um pouquinho mais complicado
    print(
        """Escolha sua Jogada
	1 PEDRA
	2 PAPEL
	3 TESOURA
		"""
    )
    while True:
        try:
            jogador = int(input())
            jogador -= 1  # é simples, o zero não está em uma posição boa para o jogador usar apenas uma mão, então é melhor que eu o deixe usar de 1 a 3 e subtraia a escolha para usar de 0 a 2 na lista
        except:
            print("tente novamente, digite apenas um número")
            continue
        if jogador < 0 or jogador > 2:
            print("somente um numero de 1 a 3")
            continue
        break
    PC = randint(0, 2)

    print("Sua Jogada: ", jogadas[jogador])
    print("Jogada do PC: ", jogadas[PC])

    # pedra>tesoura Papel>pedra tesoura>papel 1>0 2>1 0>2
    # inevitáveis montes de if, não tive ideia melhor
    print("Resultado da {}ª rodada".format(i))
    if jogador == 0 and PC == 1:
        print("PC Venceu")
        conPC += 1
    elif jogador == 1 and PC == 0:
        print("Jogador Venceu")
        conJ += 1
    elif jogador == 1 and PC == 2:
        print("PC Venceu")
        conPC += 1
    elif jogador == 2 and PC == 1:
        print("Jogador Venceu")
        conJ += 1
    elif jogador == 2 and PC == 0:
        print("PC Venceu")
        conPC += 1
    elif jogador == 0 and PC == 2:
        print("Jogador Venceu")
        conJ += 1
    elif jogador == PC:
        print("Empate")
    print("placar Jogador = {},PC = {}".format(conJ, conPC))
if conPC > conJ:
    print("PC venceu o Jo Ken Po")
elif conJ > conPC:
    print("Jogador Venceu o Jo Ken Po")
else:
    print("Acabaram empatados")

"""Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso."""
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
esco = 0
while esco != 5:
    while True:
        try:
            esco = int(
                input(
                    """Escolha o que deseja fazer com os números {} e {}\n
	[ 1 ] somar
	[ 2 ] multiplicar
	[ 3 ] maior
	[ 4 ] novos números
	[ 5 ] sair do programa\n""".format(
                        n1, n2
                    )
                )
            )
        except:
            print("Ocorreu algum erro, tente novamente e digite apenas numeros")
            continue
        break
    if esco == 1:
        print("A Soma de {} e {} é {}".format(n1, n2, n1 + n2))
    elif esco == 2:
        print("{} vezes {} dá {}".format(n1, n2, n1 * n2))
    elif esco == 3:
        print("O maior entre {} e {} é {}".format(n1, n2, max(n1, n2)))
    elif esco == 4:
        n1 = int(input("Digite um número: "))
        n2 = int(input("Digite outro número: "))
    if esco > 5 or esco < 1:
        print("Escolha somente entre 1 e 5 conforme as opções")
print("Saindo...")

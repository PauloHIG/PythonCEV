"""Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. 
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer."""
from random import randint

numero = randint(1, 10)
print("Pensei em um número de 1 a 10, tente adivinhar")
tent = 1
while True:
    while True:
        try:
            adv = int(input("{}ª tentativa: ".format(tent)))
        except:
            print("ocorreu algum erro")
            continue
        if adv > 10 or adv < 1:
            print("Pensei apenas em um número entre 1 e 10")
            continue
        break
    if adv == numero:
        print("Acertou!!! o numero que eu pensei foi {} e foram necessárias {} tentativas".format(numero, tent))
        break
    else:
        tent += 1
        if adv > numero:
            print("O numero que eu pensei é MENOR")
        else:
            print("O número que eu pensei é MAIOR")
        continue
print("Fim de Jogo")

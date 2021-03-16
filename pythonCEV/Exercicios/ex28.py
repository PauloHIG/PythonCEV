# ex 28, o computador vai "pensar" em um numero de 0 a 5 e o usuario ai tentar descobrir
from random import randint
from time import sleep


def exercicio():
    print("Escolhi um numero entre 0 e 5, tente adivinhar qual é\n")
    n = randint(0, 5)
    n1 = int(input())
    print("3.. 2.. 1..")
    sleep(3)
    if n == n1:
        print("Acertou!! o número é: {}".format(n))
    else:
        print("Errou!! que eu escolhi é: {}".format(n))


exercicio()

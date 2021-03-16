# ex98
from time import sleep

"""Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada"""


def cont1():
    for i in range(1, 11):
        print(i, end=" ")
        sleep(0.30)


def cont2():
    for i in range(10, -1, -2):
        print(i, end=" ")
        sleep(0.50)


def contper(inicio, fim, intervalo):
    if intervalo < 1:
        for i in range(inicio, fim - 1, intervalo):
            print(i)
            sleep(0.3)
    if intervalo > 1:
        for i in range(inicio, fim + 1, intervalo):
            print(i)
            sleep(0.3)


"""cont1()
print('')
cont2()
print('')"""

inicio = int(input("Escolha onde a contagem vai começar: "))
fim = int(input("Digite aonde a contagem vai terminar: "))
intervalo = int(input("De quanto em quanto a contagem vai ir?"))
print("Contagem personalizada: ")
contper(inicio, fim, intervalo)

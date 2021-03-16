"""Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função 
vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela 
função anterior"""
from random import randint


def sorteia():
    saida = []
    for i in range(5):
        saida.append(randint(1, 10))
    return saida


def somaPar(lista):
    suma = 0
    for n in lista:
        if n % 2 == 0:
            suma += n
    return suma


números = sorteia()
print(números)
print(somaPar(números))

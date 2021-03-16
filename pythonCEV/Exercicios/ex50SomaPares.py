"""Exercício Python 050: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
 Se o valor digitado for ímpar, desconsidere-o."""
soma = 0
print("Digite 6 números, os pares serão somados e a soma será mostrada no final")
for i in range(6):
    n = int(input("({}/6): ".format(i + 1)))
    if n % 2 == 0:
        soma += n
print("Soma dos números pares = {}".format(soma))

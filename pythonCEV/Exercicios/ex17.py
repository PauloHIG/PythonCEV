"""Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. 
Calcule e mostre o comprimento da hipotenusa. formula: h**2 = ca**2 + co**2"""
# exemplo de teste: se ca = 4 e co =3 então a hipotenusa é 25
from math import hypot
from matematica import hipotenusa  # funções matematicas feitas or mim em python, está na mesma pasta, por isso funciona

co = float(input("Digite o valor do cateto oposto: "))
ca = float(input("Digite o valor do cateto adjacente: "))

print("A hipotenusa é {}".format(hipotenusa(ca, co)))
print("Hipotenusa usando a biblioteca math: {}".format(hypot(co, ca)))

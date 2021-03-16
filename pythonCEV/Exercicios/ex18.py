# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import radians, sin, cos, tan

ang = float(input("Digite o valor de um ângulo qualquer: "))
while ang < 1 or ang > 90:
    ang = float(input("Somente entre 1° e 90°: "))

angr = radians(ang)  # as funções do math para calcular seno, cosseno e tangente são feitas em radianos
print(
    "O seno de {:.0f}° é {:.4f}, o cosseno é {:.4f} e a tangente é {:.4f}".format(ang, sin(angr), cos(angr), tan(angr))
)

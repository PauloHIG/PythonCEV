# ex 35 ler o comprimento de três retas e ver se elas podem formar um triângulo
"""Condição de existência de um triângulo

Dados três segmentos de reta distintos, se a soma das medidas de dois deles é sempre maior que a medida do terceiro, 
então, eles podem formar um triângulo. Por exemplo, dados os segmentos AB = 16 cm, CD = 20 cm e EF = 30 cm, 
é possível usá-los para construir um triângulo, pois as somas abaixo são verdadeiras: """


def tipoTriangulo(A, B, C):
    if A == B and A == C:
        print("Esse é um triângulo equilátero")
    elif A == B and A != C or A == C and A != B or C == B and A != C:
        print("Esse é um triângulo isósceles")
    elif A != B and A != C and B != C:
        print("Esse é um triângulo escaleno")


A = 40
B = 40
C = 40
if A + B > C and A + C > B and C + B > A:
    # apesar de eu ter feito todas as contas, basta somar as duas menores para saber as retas podem formar um triângulo
    print("As retas podem formar um triângulo")
    tipoTriangulo(A, B, C)
else:
    print("As retas não podem formar um triangulo")

"""Exercício Python 055: Faça um programa que leia o peso de cinco pessoas. 
No final, mostre qual foi o maior e o menor peso lidos."""
pesos = []
for i in range(1, 6):
    peso = float(input("Digite o peso da {}ª pessoa(KG): ".format(i)))
    pesos.append(peso)
menor = min(pesos)  # isso é o jeito python de resolver as coisas
maior = max(pesos)  # o python serve justamente pra isso, o erro seria não usar essas funções
print("O Maior peso foi {:.2f} Kg".format(maior))
print("O Menor peso foi {:.2f} Kg".format(menor))

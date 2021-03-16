"""Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
 No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista."""
lista = []
for i in range(5):
    while True:
        try:
            lista.append(int(input(f"Digite o {i+1} numero: ")))
        except:
            print("ocorreu um erro, tente novamente")
            continue
        break

print(f"O maior número da lista é {max(lista)} e está nas posições: ", end=" ")
for i in range(5):
    if lista[i] == max(lista):
        print(i, end=" ")

print(f"\nO menor número da lista é {min(lista)} e está nas posições:", end=" ")
for i in range(5):
    if lista[i] == min(lista):
        print(i, end=" ")

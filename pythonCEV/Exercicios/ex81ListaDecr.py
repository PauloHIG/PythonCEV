"""Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista."""


def recNum():
    while True:
        try:
            i = int(input("Digite um número: "))
        except:
            print("Ocorreu um erro, tente novamente")
            continue
        break
    return i


def Continuar():
    while True:
        resp = input("Quer Continuar (N pra sair): ")
        if resp not in "nNsS":
            print("Digite apenas N se quiser sair")
            continue
        break
    return resp


lista = []
while True:
    lista.append(recNum())
    sair = Continuar()
    if sair.lower() == "n":
        break

print(sorted(lista, reverse=True))
print(f"Foram digitados {len(lista)} números")
if 5 in lista:
    print("O valor 5 está na lista")

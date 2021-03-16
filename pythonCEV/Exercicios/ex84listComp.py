"""Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final,mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves."""
pessoas = []


def Continuar():
    while True:
        resp = input("Quer Continuar (N pra sair): ")
        if resp not in "nNsS":
            print("Digite apenas N se quiser sair")
            continue
        break
    return resp


def RecPes(i):
    while True:
        try:
            peso = float(input(f"Peso da {i}ª pessoa(Kg): "))
        except:
            print("Ocorreu um erro, tente novamente")
            continue
        break
    return peso


i = 1
while True:
    pessoas.append(
        [input(f"Nome da {i}ª pessoa: "), RecPes(i)]
    )  # pondo entre chaves, posso dar append de uma lista dentro de outra lista
    cont = Continuar()
    if cont.lower() == "n":
        break
    i += 1

print(f"A quantidade de pessoas cadastradas foi {len(pessoas)}")
mais = pessoas[0][1]
menos = pessoas[0][1]
for pessoa in pessoas:
    if mais < pessoa[1]:  # pessoa[1] é o peso e sempre vai ser
        mais = pessoa[1]
    if menos > pessoa[1]:  # só inverti esse sinal
        menos = pessoa[1]

print(f"O maior peso é {mais} e pessoas mais pesadas são:", end="")
i = 1
for pessoa in pessoas:
    if pessoa[1] == mais:
        print(pessoa[0], end="")
        if i < len(pessoas) - 1:
            print(", ", end="")
        else:
            print(".", end="\n")
    i += 1
# aqui tudo se repete com uma pequena diferença
print(f"O menor peso é {menos} e pessoas mais leves são:", end=" ")
i = 1
for pessoa in pessoas:
    if pessoa[1] == menos:
        print(pessoa[0], end="")
        if i < len(pessoas) - 1:
            print(", ", end="")
        else:
            print(".", end="")
    i += 1

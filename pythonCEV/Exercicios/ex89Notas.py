"""Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No 
final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno 
individualmente."""
from statistics import mean

lista = []


def RecNot(i):
    while True:
        try:
            n = float(input(f"Digite a {i}ª nota do aluno: "))
        except:
            print("Ocorreu um erro, tente novamente")
            continue
        if n < 0 or n > 10:
            print("Digite uma nota válida")
            continue
        break
    return n


def deciCont():
    while True:
        deci = input("Quer continuar?(N pra sair): ")
        if deci not in ("SsnN"):
            print("Ocorreu um erro, digite N pra sair")
            continue
        break
    return deci


i = 0
while True:
    nome = input(f"Digite o nome do {i+1}º aluno: ")
    nota1 = RecNot(1)
    nota2 = RecNot(2)
    lista.append([nome, [nota1, nota2]])
    cont = deciCont()
    if cont.lower() == "n":
        break
    i += 1
for aluno in lista:
    print(f"No. {lista.index(aluno)} Nome: {aluno[0]} Média {mean(aluno[1])}")
indice = 0
while indice != 999:
    indice = int(input("Quer ver as notas de qual aluno?: "))
    if indice in range(len(lista)):
        print(f"Nome: {lista[indice][0]} Notas: {lista[indice][1][0]},{lista[indice][1][1]}")
    elif indice < 999:
        print("não tem esse aluno na lista")

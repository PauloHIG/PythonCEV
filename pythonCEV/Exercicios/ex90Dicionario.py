# ex90 dicionarios
"""Exercício Python 090: Faça um programa que leia nome e média de um aluno, 
guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela."""
from statistics import mean


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


aluno = {}
aluno["Nome"] = input("Nome do aluno: ")
aluno["Nota"] = [RecNot(1), RecNot(2)]
if mean(aluno["Nota"]) > 6:
    sit = "aprovado"
elif mean(aluno["Nota"]) >= 5:
    sit = "recuperação"
else:
    sit = "reprovado"
print(f'Nome: {aluno["Nome"]} notas: {aluno["Nota"][0]}, {aluno["Nota"][1]} situação:{sit}')

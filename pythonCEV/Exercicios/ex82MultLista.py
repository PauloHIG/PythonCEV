"""Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. 
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
 respectivamente. Ao final, mostre o conteúdo das três listas geradas."""


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
listaPar = []
listaImpar = []
for num in lista:
    if num % 2 == 0:
        listaPar.append(num)
    else:
        listaImpar.append(num)
print(f"A lista: {lista}")
print(f"Numeros pares da lista: {listaPar}")
print(f"Numeros ímpares da lista: {listaImpar}")

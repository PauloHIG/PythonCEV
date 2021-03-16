# Escolher um aluno aleatoriamente
def função():
    import random

    lista_de_nome = []
    for i in range(1, 5):
        lista_de_nome.append(input("Digite o nome do {}º aluno: ".format(i)))
    for nome in lista_de_nome:
        print(nome)
    print("\n O aluno sorteado foi:{}".format(random.choice(lista_de_nome)))


função()
# apenas para testar, criei uma função com acentos brasileiros e descobri que posso importar dentro de uma função

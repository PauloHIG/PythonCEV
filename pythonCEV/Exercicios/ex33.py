# ex 33 ler três números e mostrar qual é o maior e  qual é o menor
lista = []
for i in range(3):
    print("Digite o {}º número".format(i + 1))
    while True:
        try:
            lista.append(int(input()))
        except:
            print("somente um número inteiro")
            continue
        break
menor = lista[0]  # ambas as variavéis receberão inicialmente um elemento da lista
maior = lista[0]  # se for um numero qualquer fora da lista, mesmo que seja um 0, pode dar problema
# é aqui que eu verifico qual é o menor e qual é o maior elemento da lista
for elemento in lista:
    if menor > elemento:
        menor = elemento
    if maior < elemento:
        maior = elemento
# prints finais
print("Sua lista: ")
print(lista)
print("O menor numero da lista é {}".format(menor))
print("O maior numero da lista é {}".format(maior))

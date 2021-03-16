"""Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. 
O programa encerrará quando ele disser que quer mostrar 0 termos."""
print("10 Termos da Progressão Aritimética")
while True:
    try:
        ptermo = int(input("Digite o primeiro termo da PA: "))
    except:
        print("Somente número inteiro")
        continue
    break
while True:
    try:
        razao = int(input("Digite a razão da PA: "))
    except:
        print("Somente número inteiro")
        continue
    break

i = 1
acumulador = ptermo

while i < 11:
    print("{}º termo = {}".format(i, acumulador))
    acumulador += razao
    i += 1

mais = 1
while True:
    while True:
        try:
            mais = int(input("Quantos termos a mais você quer ver? "))
        except:
            print("Somente número inteiro")
            continue
        break

    if mais == 0:
        break
    else:
        mais += i  # obviamente, os termos a mais precisam ser somados com i

    while i < mais:
        print("{}º termo = {}".format(i, acumulador))
        acumulador += razao
        i += 1
print("Ao todo foram {} termos".format(i - 1))  # subtraio porque o i acaba ficando um número maior que o total

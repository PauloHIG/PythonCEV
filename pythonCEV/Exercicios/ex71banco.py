"""Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
 No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o 
 programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1."""

while True:
    try:
        valor = int(input("Qual o valor que você quer sacar?(valor inteiro)"))
    except:
        print("Valor inteiro apenas, sem os centavos")
        continue
    if valor < 0:
        print("Este não é para depositar")
        continue
    break
nvalor = valor
cedCont = 0
cedAtual = 50
while True:
    if nvalor - cedAtual >= 0:
        nvalor -= cedAtual
        cedCont += 1
    else:
        print(f"{cedCont} cédulas de {cedAtual}R$\n" if cedCont > 0 else "", end="")
        cedCont = 0
        if cedAtual == 50:
            cedAtual = 20
        elif cedAtual == 20:
            cedAtual = 10
        elif cedAtual == 10:
            cedAtual = 1
        elif cedAtual == 1:
            break

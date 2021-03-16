"""Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas.
 No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.nota:usar date
print(datetime.now().year)#relembrando como pega o ano atual
 """
import colorama
from colorama import init
from termcolor import colored

init()
from datetime import datetime

contMa = 0  # maior de idade
contMe = 0  # menor de idade
for i in range(7):
    while True:
        try:
            anonasc = int(input("Digite o ano de nascimento da {}ª pessoa: ".format(i + 1)))
        except:
            print(
                colored("! ERRO !", "red")
            )  # a tabela de cores normalmente não funciona, pra executar em outro PC é melhor instalar os modulos de cor
            print("Digite novamente apenas o ano de nascimento")
            continue
        if anonasc > datetime.now().year:
            print("Parece que essa pessoa ainda vai nascer, digite outra idade")
            continue
        break
    idade = (datetime.now().year) - anonasc
    print("Esta pessoa tem {} anos".format(idade))
    if idade >= 18:
        contMa += 1
    else:
        contMe += 1
print("Aqui temos {} maiores de idade e {} menores de idade".format(contMa, contMe))

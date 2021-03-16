"""Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai 
aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores."""
# usarei alguns modulos de cores já que o código de cores normal não está funcionando no meu sistema operacional
from colorama import init
from termcolor import colored

init()
# print(colored('batata','red','on_white'))
a = ""
print(colored("Manual de funções e bibliotecas do Python", None, "on_green"))
while True:
    a = input("Quer ajuda em qual função ou biblioteca?: ")
    if a.upper() == "FIM":
        break
    colored("", "blue", "on_white")
    help(a)

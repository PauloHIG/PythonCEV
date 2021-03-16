"""Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python, 
só que fazendo a validação para aceitar apenas um valor numérico."""


def leiaInt(texto=None):
    if texto == None:
        texto = ""
    while True:
        try:
            num = int(input(texto))
        except:
            print("\033[0;31m Digite apenas um numero inteiro")  # não funciona no windows por algum motivo, só quando import oalguns pacotes como fiz no jogo da velha
            continue
        break
    return num


a = leiaInt("Digite um número: ")
print(a)

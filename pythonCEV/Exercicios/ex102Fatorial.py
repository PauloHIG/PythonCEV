"""Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a 
calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do 
fatorial."""


def fatorial(num, show=None):  # para lembrar, o None cria uma varíavel não obrigatoria
    """Função para calculo de fatorial
	recebe a um parametro inteiro e positivo pra calcular seu fatorial
	tem o parâmetro show que não é obrigatorio, para mostrar o calculo do fatorial, é só colocar 1 ou True na função pra mostrar o calculo
	"""
    fact = 1
    print(f"Fatorial de {num}")
    for i in range(num, 0, -1):
        if show:
            print(f"{i} X " if i > 1 else f"{i} = ", end="")  # eu não copiei do CeV
        fact *= i
    print(fact)


fatorial(5, True)  # o zero e o false são interpretados como false no if show
help(fatorial)  # bem interessante, posso mostrar como usar a função

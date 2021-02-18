'''Exercício Python 108 e 109: Adapte o código do desafio
107​, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.'''
from utilidades_cev import moeda as mo#essa inportação é baseada no exercício 111
from utilidades_cev.dados import validaMoeda
val = 1000.232
val = validaMoeda()
mo.resumo(val,10,90)

'''Exercício Python 109: Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais,
informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
'''
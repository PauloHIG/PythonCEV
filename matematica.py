#Transformarei operações matematicas em funções e as colocarei aqui
#funcoes de operaçoes
def soma(n1,n2):
    return n1 + n2
def sub(n1,n2):
    return n1 - n2
def multi(n1,n2):
    return n1 * n2
def div(n1,n2):
    return n1 / n2
def divint(n1,n2):
    return n1 // n2 #divisao inteira, fiz de outra maneira em outro exercicio
def modu(n1,n2):
    return n1 % n2 #resto da divisão
def pot(n1,n2):
    return n1 ** n2 #potenciaçao
'''
ordem de precedencia em python
1º = ()
2º = **
3º = * / % //
4º = + -
'''

#raiz quadrada, cubica, e a de qualquer numero
def raizq(n1):
    return n1**(1/2)
def raizcub(n1):
    return n1**(1/3)
def raiz(n1,r):
    return n1**(1/r)

#tabuada do 1 ao 10 de qualquer numero
def tabuada(n):
    print("\ntabuada do {} :".format(n))
    for i in range(1, 11):
        print('{} X {} = {}'.format(n, i, n * i))

#Fatorial
def fatorial(n):
    fac = 1
    while n >1:
        fac = fac*n
        n = n-1
    return fac

def hipotenusa(ca,co):
    return ((ca**2) + (co**2))**0.5

#Operadores aritimeticos

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
    return n1 % n2 #em python o resto da divisao se faz com o simbolo %
def pot(n1,n2):
    return n1 ** n2 #potenciaçao

def raizq(n1):
    return n1**(1/2)
def raizcub(n1):
    return n1**(1/3)
def raiz(n1,r):
    return n1**(1/r)
#tabuada
def tabuada(n):
    print("\ntabuada do {} :".format(n))
    for i in range(1, 11):
        print('{} X {} = {}'.format(n, i, n * i))



'''
print(raizq(81))
print(raizcub(27))
ordem de precedencia em python
1º = ()
2º = **
3º = * / % //
4º = + -

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
s = n1+n2
d = n1/n2
di= n1//n2
m = n1*n2
p = n1**n2
r = n1 % n2

print('A soma e {}, a multiplicaçao e {}, a divisao e {:.3f}, a divisao inteira e {}, o resto e {}, a potencia e {}'.format(s,m,d,di,r,p))

o {:.3f} que se ve ali em cima e a limitaçao das casas decimais do numero flutuante'''
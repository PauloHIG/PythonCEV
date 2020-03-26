n1 = int(input('Digite o primeiro numero '))
n2 = int(input('Digite o segundo numero '))

def soma(n1, n2):
    return n1 + n2

def multi(n1, n2):
    return n1 * n2

def divint(n1, n2):
    return int(n1 / n2)

def divdec(n1, n2):
    return n1 / n2

def restoDivi(n1, n2):
    return n1 % n2

def subtracao(n1, n2):
    return n1 - n2

def raiz(n1,n2):
    return n1**n2
print('A soma é: {}'.format(soma(n1, n2)))
print('A subtraçao é:{}'.format(subtracao(n1, n2)))
print('O resultado da divisao é {} e o resto é {}'.format(divint(n1, n2), restoDivi(n1, n2)))
print('{} elevado a {} é {}'.format(n1,n2,raiz(n1,n2)))
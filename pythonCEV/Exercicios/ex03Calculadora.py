# calculadora simples
n1 = int(input("Digite o primeiro numero "))
n2 = int(input("Digite o segundo numero "))


def soma(n1, n2):
    return n1 + n2


def multi(n1, n2):
    return n1 * n2


def divint(n1, n2):
    return int(n1 / n2)


def div(n1, n2):
    return n1 / n2


def restoDivi(n1, n2):
    return n1 % n2


def subtracao(n1, n2):
    return n1 - n2


def pot(n1, n2):
    return n1 ** n2


print("A soma é: {}".format(soma(n1, n2)))
print("A subtração é:{}".format(subtracao(n1, n2)))
print("O resultado da divisão inteira de {}/{} é {} e o resto é {}".format(n1, n2, divint(n1, n2), restoDivi(n1, n2)))
print("{} elevado a {} é {}".format(n1, n2, pot(n1, n2)))

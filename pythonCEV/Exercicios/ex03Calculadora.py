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


print(f"A soma é: {soma(n1, n2)}")
print(f"A subtração é:{subtracao(n1, n2)}")
print(f"O resultado da divisão inteira de {n1}/{n2} é {divint(n1, n2)} e o resto é {restoDivi(n1, n2)}")
print(f"{n1} elevado a {n2} é {n1**n2}")

# 023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# no exemplo ele quer que separe e mostre qual é o milhar, qual é a centena e assim por diante
def exercicio():
    n = 3245
    print("Numero:", n)
    n = str(n)
    print("Milhar:{}\nCentena:{}\nDezena:{}\nUnidade:{}".format(n[0], n[1], n[2], n[3]))


def CeV():
    # na maneira do curso em vídeo tem um jeito bem interessante de resolver o problema surgido na solução anterior
    n = int(input("Digite um número(0-9999): "))
    print(n)
    u = (
        n // 1 % 10
    )  # a chave pra entender como isso funciona é lembrar que o resto de uma divisão por 10 sempre vai ser a unidade
    d = (
        n // 10 % 10
    )  # para o número da dezena se tornar o da unidade e virar o resto da divisão por 10, é preciso dividir o numero por 10
    c = (
        n // 100 % 10
    )  # o mesmo vale para os outros, a centena irá virar a unidade para virar o resto da divisão por 10, por exemplo, 3245//10 = 32, 32%10 = 2
    m = n // 1000 % 10  # é importante que a divisão seja inteira
    print("Milhar:{}\nCentena:{}\nDezena:{}\nUnidade:{}".format(m, c, d, u))


# exercicio()
CeV()

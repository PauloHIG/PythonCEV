# mostrar se um numero é par ou ímpar
print("Par ou ímpar")


def exercicio():
    # tenho mantido essa pratica de colocar um tratamento de exceção em todo input do usuário, para não interromper o programa caso ele digite qualquer coisa
    while True:
        try:
            n = int(input("Digite um numero inteiro: "))
        except:
            print("Somente um número inteiro, não digite pontos nem vírgulas")
            continue
        break
    if n % 2 == 0:
        print(n, " é um número par")
    else:
        print(n, " é um número ímpar")


exercicio()

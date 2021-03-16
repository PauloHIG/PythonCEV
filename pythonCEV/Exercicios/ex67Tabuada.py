# tabuada 2, o usuario pode perguntar a tabuada de qualquer numero menos numeros negativos
def tabuada(n):
    for i in range(1, 11):
        print(f"{n} X {i:2} = {n*i}")


while True:
    while True:
        try:
            n = int(input("Digite um número pra saber sua tabuada: "))
        except:
            print("Ocorreu um erro, tente novamente")
            continue
        break
    if n < 0:
        break
    tabuada(n)
print("fim do programa")

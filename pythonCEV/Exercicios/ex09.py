#tabuada
def tabuada(n):
    print("\ntabuada do {}:".format(n))
    for i in range(1, 11):
        print('{} X {} = {}'.format(n, i, n * i))


for i in range(1,11):
    tabuada(i)

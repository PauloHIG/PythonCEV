# ex60 fatorial
# fatoral de 0 = 1
while True:
    try:
        n = int(input("Digite o número pra saber seu fatorial: "))
    except:
        print("Precisa ser um número inteiro")
        continue
    if n < 0:
        print("Somente um número positivo")
        continue
    break
fat = 1

print("{}! = ".format(n), end="")
for i in range(n, 0, -1):  # ele não vai até o zero, vai até o 1
    fat = fat * i
    print("{} X ".format(i) if i > 1 else "{} = ".format(i), end="")
print("{}".format(fat))

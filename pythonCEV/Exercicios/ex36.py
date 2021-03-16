# ex36 Calcular se o usuário pode pagar a prestação de uma casa, o valor da prestação não pode ser maior que 30% do salário do usuário
# como sempre, vou usar o try para não interromper o programa caso o usuário digite algo errado
while True:
    try:
        preço_casa = float(input("Digite o preço da casa R$ "))
    except:
        print("somente o preço da casa, sem vírgulas e sem textos ")
        continue
    break
while True:
    try:
        salario = float(input("Digite o seu salário: "))
    except:
        print("somente o salário, sem textos ")
        continue
    break
while True:
    try:
        anos = int(input("Em quantos anos você vai pagar? "))
    except:
        print("somente a quantidade de anos em que você pretende pagar, por favor")
        continue
    break
meses = anos * 12
prestação = preço_casa / meses
print("A prestação para uma casa de R${:.2f} em {} anos dá R${:.2f} por mês".format(preço_casa, anos, prestação))
print("30% do seu salário de R${:.2f} é R${:.2f}".format(salario, (salario * 0.3)))
if prestação < salario * 0.3:
    print("prestação aprovada")
elif prestação > salario * 0.3:
    print("prestação negada")

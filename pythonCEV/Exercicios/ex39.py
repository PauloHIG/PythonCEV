import datetime

ano = datetime.date.today().year
while True:
    try:
        idade = int(input("Em que ano você nasceu?: "))
    except:
        print("Somente o ano")
        continue
    break
alistamento = idade + 18
if ano == alistamento:
    print("Você tem que se alistar ainda esse ano")
elif ano < alistamento:
    print("O ano em que você deve se alistar é {}".format(alistamento))
elif ano > alistamento:
    print("Você está atrasado para o alistamento, era pra ser feito em {}".format(alistamento))

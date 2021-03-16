# aqui vai meu truque para impedir que o usuário use acentos
frase = input("Detetor de palíndromo\nDigite uma frase: ")
while True:
    try:
        frase.encode("ascii")  # o ascii não aceita acentos, portanto vai dar erro caso o usuário digite
    except:
        print("Não utilize acentos")
        frase = input("Digite a frase novamente: ")
        continue
    break
frases = frase.replace(" ", "").lower()  # tirando o espaço e deixando em minúsculo

if frases == frases[::-1]:
    print("{} é um palíndromo".format(frase))
else:
    print("{} não é um palíndromo".format(frase))

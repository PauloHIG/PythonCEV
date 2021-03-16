# 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
cidade = input("Digite sua cidade: ").strip()  # removendo espaços inúteis, strip() será bem útil
print("santo" in cidade.lower())  # retorna True ou False


def CEV():
    # versão do Guanabara
    cid = str(input("Digite sua cidade: ")).strip()
    print(cid[:5].lower() == "santo")  # lê as 5 primeiras letras e verifica se tem 'santo' retornando True ou False


CEV()

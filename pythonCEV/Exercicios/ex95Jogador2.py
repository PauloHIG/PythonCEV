jogador = dict()
time = []
# pra não repetir codigo, fiz essas funções
def recNome():
    while True:
        nome = input(f"Nome do jogador: ")
        if len(nome) == 0:
            print("Precisa digitar o nome")
            continue
        break
    return nome


def recInt():
    while True:
        try:
            num = int(input())
        except:
            print("Ocorreu um erro, digite novamente: ", end=" ")
            continue
        break
    return num


def deciCont():
    while True:
        deci = input("Quer continuar?(N pra sair): ")
        if deci not in ("SsnN"):
            print("Ocorreu um erro, digite N pra sair")
            continue
        break
    return deci


while True:
    jogador.clear()
    jogador["Nome"] = recNome()
    print("Quantidade de partidas: ", end="")
    npart = recInt()  # número de partidas
    jogador["Gols"] = []  # assim eu adiciono quantos valores eu quiser na lista
    for i in range(npart):
        print(f"	Quantidade de gols da {i+1} º partida: ", end="")
        jogador["Gols"].append(recInt())  # lembrando que jogador['Gols'] é uma lista agora
    time.append(jogador.copy())
    deci = deciCont()
    if deci.lower() == "n":
        break

print("Exibindo dados do time")
print("id			Nome			Gols			Total")
for ender, dicio in enumerate(time):  # o enumerate coloca o id(endereço) da lista e o seu elemento
    print(f"{ender:<11}", end=" ")
    for valores in dicio.values():
        print(
            f"{str(valores):<16}", end=""
        )  # esse str(valores) resolveu um problema sério, não posso usar o fatiamento se o valor for uma lista, então converto-a para string
    print(f'{sum(dicio["Gols"])}')

while True:
    print("Mostrar dados de qual jogador? (id) digite 999 se quiser sair:", end="")
    j = recInt()
    if j == 999:
        print("Saindo...")
        break
    try:
        print("---" * 15)
        print(f"Nome:{time[j]['Nome']} ")
        i = 1
        for gol in time[j]["Gols"]:
            print(f"Partida {i} gols: {gol}")
            i += 1
    except:
        print("Você digitou um id inválido")

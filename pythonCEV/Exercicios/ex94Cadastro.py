"""Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em 
um dicionário e todos os dicionários em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média"""

# tem uma versão em que um dicionario recebe as listas e não o contrário, chamada apenas de Cadastro.py
# a primeira coisa que foram essas funções pra não travar o programa caso algo errado seja digitado
def recSex(i):
    while True:
        sex = input(f"Digite o sexo da pessoa {i} (M/F)")
        if len(sex) != 1 or sex not in "MmFf":
            print("Erro, tente novamente, digite apenas M(masculino) ou F(feminino)")
            continue
        if sex in "MmFf" and len(sex) == 1:
            break
    return sex.upper()


def recIdade(i):
    while True:
        try:
            idade = int(input(f"Digite a idade da pessoa {i}: "))
        except:
            print("Ocorreu um erro, digite apenas a idade")
            continue
        if idade < 0:
            print("Digite uma idade válida")
            continue
        break
        idade = idade.upper()
    return idade


def deciCont():
    while True:
        deci = input("Quer continuar?(N pra sair): ")
        if deci not in ("SsnN"):
            print("Ocorreu um erro, digite N pra sair")
            continue
        break
    return deci
#é bom lembrar que se eu sempre precisar usar funcões como essas acima, o ideal é criar uma biblioteca

def recNome(i):
    while True:
        nome = input(f"Nome da pessoa {i}: ")
        if len(nome) == 0:
            print("Precisa digitar o nome")
            continue
        break
    return nome


pessoas = []
pessoa = dict()
i = 1
while True:
    pessoa.clear()
    pessoa["Nome"] = recNome(i)
    pessoa["Sexo"] = recSex(i)
    pessoa["Idade"] = recIdade(i)
    pessoas.append(pessoa.copy())  # ela só pode receber a copia, senão fica tudo igual no final
    i += 1
    deci = deciCont()
    if deci.lower() == "n":
        break
    print("--" * 15)
print("--" * 15)
# calculando umas coisinhas
quant = len(pessoas)
soma = 0
for i in range(quant):
    soma += pessoas[i]["Idade"]
media = soma / quant
# os prints finais
print(f"Quantidade de pessoas cadastradas: {quant}")

print("Pessoas do sexo feminino: ")
for pessoa in pessoas:
    if pessoa["Sexo"] == "F":
        print(pessoa["Nome"])

print(f"Média de idade: {media:.0f}")

print("Pessoas com idade acima da média: ")
for pessoa in pessoas:
    if pessoa["Idade"] > media:
        print(f"Nome: {pessoa['Nome']:7} idade:{pessoa['Idade']}")

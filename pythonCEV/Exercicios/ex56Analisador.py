"""Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
 No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho
  e quantas mulheres têm menos de 20 anos."""
from statistics import mean  # para calcular a media estou importanto mean do statistics

nome = []
idade = []
sexo = []
mvinte = 0  # mulherres com menos de 20 anos
hvelho = 0  # idade do homem mais velho
nvelho = "nenhum"  # nome do homem mais velho


def RecebeIdade():
    while True:
        try:
            idade = int(input("Idade da {}ª pessoa ".format(i + 1)))
        except:
            print("Digite apenas a idade da pessoa")
            continue
        if idade < 0:
            print("Hmm, parece que essa pessoa ainda não nasceu, digite uma idade válida")
            continue
        break
    return idade


def RSexo():
    while True:
        try:
            sexo = input("Sexo da {}ª pessoa (M/F) ou P se prefere não declarar: ".format(i + 1))
        except:
            continue
        if len(sexo) > 1:
            print("Apenas uma letra F(feminino), M(masculino) ou P(prefere não declarar)")
            continue
        if sexo.lower() not in ("f m p"):
            print("Não tem essa opção, desculpe, tente novamente ou digite P se não se encaixa em nenhuma das duas")
            continue
        break
    return sexo


for i in range(4):
    nome.append(input("Nome da {}ª pessoa ".format(i + 1)))
    idade.append(RecebeIdade())
    sexo.append(RSexo())
    print("--" * 12)
    if idade[i] < 20 and sexo[i].lower() == "f":
        mvinte += 1
    if hvelho < idade[i] and sexo[i].lower() == "m":
        hvelho = idade[i]
        nvelho = nome[i]

if hvelho == 0:  # pequeno detalhe pra idade não ficar '0 anos na hora de exibir a mensagem'
    hvelho = "?"

print("Média da idade é de {} anos".format(mean(idade)))
print("Homem mais velho: {} idade {} anos".format(nvelho, hvelho))
print("Mulheres com menos de 20 anos:{}:".format(mvinte))

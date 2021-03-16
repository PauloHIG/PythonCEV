"""Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, 
mostrando os 10 primeiros termos da progressão usando a estrutura while.

(PrimeiroTermo +((TermoEscolhido-1)*razão)) formula pra pegar um termo qualquer"""
print("10 Termos da Progressão Aritimética")
while True:
    try:
        ptermo = int(input("Digite o primeiro termo da PA: "))
    except:
        print("Somente número inteiro")
        continue
    break
while True:
    try:
        razao = int(input("Digite a razão da PA: "))
    except:
        print("Somente número inteiro")
        continue
    break
i = 1
acumulador = ptermo
while i < 11:
    print("{}º termo = {}".format(i, acumulador))
    acumulador += razao
    i += 1

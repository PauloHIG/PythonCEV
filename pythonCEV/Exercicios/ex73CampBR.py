"""Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética. 
d) Em que posição está o time da Chapecoense."""
times = (
    "Internacional",
    "Flamengo",
    "Atlético-MG",
    "São Paulo",
    "Fluminense",
    "Palmeiras",
    "Grêmio",
    "thletico-PR",
    "Ceará",
    "Corinthians",
    "Santos",
    "Atlético-GO",
    "Bragantino",
    "Vasco",
    "Bahia",
    "Sport",
    "Fortaleza",
    "Goiás",
    "Coritiba",
    "Botafogo",
)
for time in times:
    print(time)

print("\nOs 5 primeiros:")
for i in range(5):
    print(times[i])

print("\nOs 4 últimos:")
print(times[-4:])

print("\nEm ordem alfabética:")
for time in sorted(times):
    print(time)

print("\nPosição do Flamengo:")  # na lista que eu peguei não tem chapecoense
print(
    f'{times.index("Flamengo")+1}ª posição'
)  # fui obrigado a usar aspas duplas, provavelmente por causa que o print usa aspa simples

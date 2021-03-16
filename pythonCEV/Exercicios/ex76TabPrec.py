"""Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular."""
lista = (
    "nota de dois",
    3.99,
    "maquina do tempo",
    1000000.00,
    "Como escapar de um apocalipse robô",
    40.00,
    "Como nunca mais errar em alinhamento",
    0.00,
    "dá pra misturar alinhamento e limitação de casas",
    100.10,
)

print("Tabela de preços: ")
for i in range(0, len(lista), 2):
    print(
        "Item:{: <50} Preço: {:>10.2f}R$".format(lista[i], lista[i + 1])
    )  # assim que se alinha um texto para a esquerda com .<30
# esse exercicio respondeu minhas dúvidas sobre como alinhar e colocar duas casas decimais no float

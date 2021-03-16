# calculo de desconto
preco = float(input("Digite o preço do produto R$"))
desc = 5
precof = preco - (
    preco * desc / 100
)  # calculo de porcentagem, multiplicação e divisão têm a mesma ordem de precedência, não é necessario usar parentesis na divisão como fiz anteriormente
print("R${:.2f} com {}% de desconto é = R${:.2f}".format(preco, desc, precof))

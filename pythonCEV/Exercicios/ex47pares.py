# ex47 mostrar numeros pares de 1 a 50
msgFinal = ""
for i in range(2, 51):
    if i % 2 == 0:
        msgFinal = msgFinal + str(i) + " "
print(msgFinal)

""" a versão do curso em video tem coisas interessantes e um jeito diferente de resolver o problema
for n in range(1,51,2):
	print(n,end =" ")
como deu pra ver, uma solução diferente era simplesmente pular de 2 em 2 no "passo" da função range(inicio,fim, passo)
isso serviu pra gastar menos processamento uma vez que metade dos calculos não são necessários
foi bom relembrar o uso do (end = ' ') para os prints não pularem uma linha
	"""
for n in range(2, 51, 2):
    print(n, end=" ")

#Aluguel de carro
#pegar a quantidade de quilômetros rodados e a quantidade de dias para saber o preço do alguel, o alguel é de 60R$ por dia e R$ 0,15 por km rodado 
dias = int(input('Dias alugados:'))
km = float(input('Quantidade de quilômetros rodados : '))
preço = (dias*60)+(km*0.15)
print('O total do aluguel é de R${:.2f}'.format(preço))
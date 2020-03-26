#aumento de 15% no salario
sal = 1000.00
n = 15
alm = sal+(sal*(n/100))#fiz assim alm = sal * 1.15, mas queria fazer de modo a poder se colocar qualquer tipo de aumento
print('Seu salario era R${:.2f}, voce rSecebeu um aumento de 15%, agora seu salario e R${:.2f}'.format(sal, alm))
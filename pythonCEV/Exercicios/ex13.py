#aumento de 15% no salario de um funcionário
sal = float(input('Digite o salário do funcionário R$'))
n = 15
alm = sal+(sal*n/100)#lembre-se de que operações com a mesma ordem de precedência não precisam ser separados entre parêntesis
print('O salário era R${:.2f}, com {}% de aumento, o novo salário é de R${:.2f}'.format(sal,n , alm))
'''
ordem de precedência em python
1º = ()
2º = **
3º = * / % //
4º = + -'''
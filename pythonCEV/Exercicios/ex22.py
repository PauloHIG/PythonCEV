'''022: Crie um programa que leia o nome completo de uma pessoa e mostre: 
O nome com todas as letras maiúsculas e minúsculas. 
Quantas letras ao todo (sem considerar espaços). 
Quantas letras tem o primeiro nome.'''
nome = 'Paulo Henrique Ito Gabriel'
print(nome.upper())
print(nome.lower())
nomer = nome.replace(' ','')#gambiarra pra remover o espaço
print('Seu nome tem {} letras sem contar com os espaços'.format(len(nomer)))
nomer = nome.split()
print('Seu primeiro nome tem {} letras'.format(len(nomer[0])))
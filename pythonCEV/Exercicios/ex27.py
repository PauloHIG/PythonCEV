# 027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.'''
nome = str(input("Digite seu nome: "))
n = nome.split()
print("Nome:{}".format(nome))
print("Primeiro nome:{}".format(n[0]))
print("Ultimo nome: {}".format(n[len(n) - 1]))  # gambiarra pra pegar o ultimo elemento da lista

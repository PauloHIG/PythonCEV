"""
para mostrar tipos primitivos de variaveis e testar
n = input("o que eu quiser")
print(type(n))
n.isnumeric() e vários outros...
"""

n = input("Digite algo \n")  # quando o valor de uma varíavel está ocupada, ele é verdadeiro
print('TESTANDO A STRING n:\n')
print('Tipo primitivo da variavel: ', type(n)) #sempre vai ser string nesse caso
print("e numerico?: ", n.isnumeric())  # isnumeric() mostra se e possivel converter uma string para um numero
print('e alpha?: ', n.isalpha()) #testa se so tem letras do alfabeto
print("e alfanumerico?: ", n.isalnum())  # testa se e alfanumerico (tem letras e numeros)
print("todas as letras estao maiusculas?: ", n.isupper())  # testa se a variavel esta com todas as letras maiusculas
print('e so um espaço?: ', n.isspace())
print('esta no padrao ASCII?: ', n.isascii())


#aula12
texto ='''
Helena
Alice
Laura
Manuela 
Isabella 
Sophia
Luísa
Heloísa
Valentina
Júlia
Cecília
Eloá
Lívia
Lorena
Maria Luísa
Giovanna
Liz
Antonella
Maitê 
Mariana
Miguel
Arthur
Heitor
Bernardo
Théo
Davi
Gabriel
Paulo
Pedro
Samuel
Lorenzo
Benjamin
Matheus
Lucas
Benício
Gael
Joaquim
Nicolas
Henrique
Rafael
Isaac
'''
nome = input('Digite seu nome: ')
if nome.lower() in texto.lower():
	print('Seu nome é popular')
else:
	print('Olá, {}'.format(nome))
#a aula é sobre o uso do if e do elif, equivalente ao else if de outras linguagens
#porem eu quis testar uma coisa aqui
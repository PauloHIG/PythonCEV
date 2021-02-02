#Aula 16-tuplas
lanche = 'hamburger','suco','pizza','pudim'#criação de uma tupla

print(lanche)#exibe tudo com parentesis
print(lanche[1])#igual o funcionamento das listas
print(lanche[-4])#vai dar hamburger
print(lanche[1:3])#o 3 vai ser ignorado, igual acontece no "for in range()"
#tuplas são imutáveis
for cont in range(len(lanche)):
	print(f'Eu vou comer {lanche[cont]}')
#honestamente, ainda não sei a utilidade da tupla, parece uma lista com a desvantagem de ser imutável
print(sorted(lanche))#não muda a configuração, mas ele transforma em uma lista pra poder reorganizar a tupla

#pra ter uma ideia de como funciona o sorted(), coloquei o alfabeto na versão qwerty e o sorted() mostra em ordem alfabetica
alfabeto = 'qwertyuiopasdfghjklçzxcvbnm'
print(alfabeto)
print(sorted(alfabeto))#na hora do print, vê se que a string também é transformada em uma lista
for letra in (sorted(alfabeto)):
	print(letra,end=' ')

#soma de tuplas
a = (2,1,10,9,3,1)
b = (4,7,6,5,10,8)
c = a+b #a ordem da soma tem influência
print('\n',c)
print(sorted(c))
print(c.count(1))#mostrará quantas vezes aparece o 1 dentro da tupla, coloquei 2 de proposito 
print(c.index(8))#mostra a posição do número 8, ou seja, o index é uma ferramenta de pesquisa
print(c.index(10,3))#tem um 10 na posição 2, mas estou procurando outro a partir da posição 3

#a tupla não pode ser alterada, mas pode ser deletada
del(lanche)#o del pode ser usado pra qualquer tipo de variável
lanche = 'Salada','fruta','legume','agua'
print(lanche)
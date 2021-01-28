'''Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
No final, mostre os 10 primeiros termos dessa progressão.'''
print('Progressão aritimética,10 primeiros termos')
while True:
	try:
		PTermo = int(input('Digite o primeiro termo da PA: '))
	except:
		print('Somente número inteiro')
		continue
	break
while True:
	try:
		r = int(input('Digite a razão da PA: '))
	except:
		print('Somente número inteiro')
		continue
	break
def PA(PTe,r):	
	lista = [PTe]
	for i in range(1,10):#a função range é basicamente uma função de progressão aritimetica pronta
		lista.append(lista[i-1]+r)
	return lista
def enesimo(PTe,r):
	pos = int(input('Para saber o termo de uma posição qualquer, digite a posição: '))#vi a formula na wikipedia e quis incluir ela aqui
	return (PTe+((pos-1)*r))#serve pra absolutamente qualquer posição, além das 10 do exercício

print(PA(PTermo,r))
print(enesimo(PTermo,r))
#bem mais longo do que precisava, com o erro de não aproveitar o range("primeiro termo", "Decimo termo usando formula do enesimo + razão", "Razão")
'''Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida
IMC = peso/altura**2
'''

while True:
	try:
		peso = float(input('Digite seu peso(Kg): '))
	except:
		print('Ocorreu um erro, digite novamente, não se esqueça de usar ponto no lugar da virgula')
		continue
	break		
while True:
	try:
		altura = float(input('Digite sua altura(metros): '))
	except:
		print('Ocorreu um erro, digite novamente, não se esqueça de usar ponto no lugar da virgula')
		continue
	break
		
IMC = peso/(altura**2)
print('Seu IMC é:{:.2f}'.format(IMC))
if IMC <18.5:
	print('Está abaixo do peso')
elif IMC < 25:
	print('Você está com o peso ideal')
elif IMC <30:
	print('Você está com sobrepeso')
elif IMC < 40:
	print('Você está com obesidade')
else:
	print('Você está com obesidade Mórbida')
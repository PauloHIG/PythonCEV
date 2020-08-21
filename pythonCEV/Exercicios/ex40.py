def entrada():
	while True:
		try:
			nota = int(input(''))
		except:
			print('somente a nota inteira do aluno (1-10)')
			continue
		if nota <0 or nota >10:
			print('Somente uma nota válida (entre 0 e 10)')
			continue
		break
	return nota
print('Digite a primeira nota do aluno')
n1 = entrada()
print('Digite a segunda nota do aluno')
n2 = entrada()
media = (n1+n2)/2
if media >=6:
	print('a média do aluno foi:{} Aluno aprovado'.format(media))
elif media <6:
	print('a média do aluno foi:{} Aluno reprovado'.format(media))
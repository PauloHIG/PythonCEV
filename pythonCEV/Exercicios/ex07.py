# media de aluno

'''
ordem de precedencia em python
1º = ()
2º = **
3º = * / % //
4º = + -
'''

n1 = int(input('Digite a primeira nota: '))
n2 = int(input('Digite a segunda nota: '))
med = (n1 + n2) / 2
if med >= 6:
    re = 'o aluno passou'
else:
    re = 'o aluno foi reprovado'
print('A media foi: {}, {}'.format(med, re))

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
#apenas pra mostrar que o Python aceita acentos nas variáveis, no entanto é bom não se acostumar com isso
média = (n1 + n2) / 2
if média >= 6:
    re = 'o aluno passou'
else:
    re = 'o aluno foi reprovado'
print('A média foi: {}, {}'.format(média, re))

import aula07 as ope
'''
teste para verificar se eu consigo importar funçoes de outro arquivo
ordem de precedencia em python
1º = ()
2º = **
3º = * / % //
4º = + -
res = 5 + ope.multi(3,2)
print('5+3*2 = ', res)
res = (ope.multi(3,5))+(ope.pot(4,2))
print('3*5+4**2 = ', res)

res = (5+4)**2
res = res*3
print('3*(5+4)**2 = ', res)'''

for i in range(1,6):
	ope.tabuada(i)
def a():
	print('Start of a()')
	b()
def b():
	print('Start of b()')
	c()
def c():
	print('Start of c()')
	42/0#erro causado propositalmente, para mostrar o 'traceback' do python
a()
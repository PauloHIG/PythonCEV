#ex96 escreva
def escreva(mensagem):
	print('^'*(len(mensagem)+4))
	print(f'  {mensagem}')
	print('^'*(len(mensagem)+4))
msg = input('Digite uma mensagem: ')
escreva(msg)
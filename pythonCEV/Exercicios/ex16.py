#pegar um numero real e mostrar sua porção inteira
from math import trunc
n = float(input('Digite um número real: '))
nint = int(n)

#primeira forma de resolver,sem importar nada
print('A porção inteira de {} é {}'.format(n,nint))

#outra maneira de resolver com o math.trunc()
print('O valor "truncado" de {} é {}'.format(n,trunc(n)))

#nint receberá apenas a porção inteira de n que é um numero real
nint = trunc(n)
print('nint({}) é uma variável do tipo inteiro({})'.format(nint,type(nint)))
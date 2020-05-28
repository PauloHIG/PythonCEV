#cores
#padrão ANSI para cores
#escape sequence
#\033[0;33;44m exemplo

'''
033 representa cor em python
existe difenrença entre codigo de estilo, de texto e de fundo, o que a gente coloca entre [ e mm todos são opcionais

código de estilo(só os que funcionam em python)
0:none(sem estilo)
1:negrito
4:sublinhado
7:negativo(inverte as cores de fundo e d texto)

codigos de cores do texto
30:branco
31:vermelho
32:verde
33:amarelo
34:azul
35:roxo
36:ciano
37:cinza
codigos de cores do fundo
40:branco
41:vermelho
42:verde
43:amarelo
44:azul
45:roxo
46:ciano
47:cinza'''

print('\033[32m'+'Olá mundo')#funciona na internet, mas não aqui
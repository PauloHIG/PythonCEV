#aula 9
#fatiamento de String
texto = 'Texto com Espaços'
print(texto[::2])#exibe a string pulando caracteres, nesse exemplo ele pula de 1 em1 1
print(len(texto))#retorna a quantidade de elementos na string contando com os espaços

print(texto.count('o'))#conta quantas vezes uma letra aparece em uma string, diferencia entre maiúscula e minúscula
print(texto.lower().count('t'))#cominando com o lower e um count com uma letra minuscula, não preciso pre preocupar com a diferenciação

print(texto.find('com'))#mostra a posição de uma letra ou palavra(ou o que você bem entender) se ela estiver no texto, a contagem começa do 0, se não tiver nada, ele retorna -1

texto = texto.replace('com Espaços','substituto com letras minúsculas')#substitui uma ou várias palavras por outra, não esqueça da diferenciação entre maiúscula e minuscula
print(texto)

print(texto.title())#todas as palavras começarão letras maiúsculas, como em um título

texto = '        espaços inúteis       '
texto = texto.strip()#remove os espaços inuteis do começo e do fim, tem as variações rstrip() e lstrip(), que removem só os espaços da direita e da esquerda respectivamente
print(texto)

texto = 'mais de uma Palavra'
x=texto.split()#divide uma string em uma lista onde cada elemento é uma palavra
print(x[3])#exibirá 'palavra, uma vez que ela está na posição 3 da lista x que recebeu a string texto splitada
print(x[3][0])#como em uma matriz,você ten a "linha"(palavra) e a "coluna"(letra), que nesse exemplo é P
print('-'.join(texto))#o que estiver nas aspas simples é o que ficará entre cada uma das letras

print('''colocando três aspas eu posso
printar um texto grande com mais de uma linha,
e mais uma vez descubro que não dá pra subestimar um curso da CeV 
mesmo que seja feito para iniciantes ''')

print(texto.lower().find('palavra'))#a combinação de lower() ou upper() com o find ajuda a não diferenciar entre maiuscula e minuscula na hora de usar o find() 

def mostra_arq(nomearq):
	cria_arquivo(nomearq)
	arq = open(f'{nomearq}.txt','r')
	print(arq.read())
	arq.close()
def cria_arquivo(nomearq):
	'''cria arquivo caso ele ainda não tenha sido criado, recebe o nome do arquivo que sempre será .txt automaticamente'''
	try:
		f = open(f"{nomearq}.txt", "r")
	except:
		print(f'criando arquivo {nomearq}')#
		f = open(f"{nomearq}.txt", "a")
	f.close()
def escreve_dado(nomearq,nome,idade):
	'''feito especialmente para o exercicio 115 do curso em vídeo, precisa de ter o nome do arquivo, o nome da pessoa que será inserido no arquivo e da idade que será inserida também'''
	cria_arquivo(nomearq)#primeiro ele tenta ver se o arquivo existe, caso contrário, ele cria um
	arq = open(f"{nomearq}.txt", "a")# o 'w' reescreve o arquivo e acaba não sendo util
	arq.write(f'{nome};{idade}\n')#estou separando o nome e a idade com ponto e vírgula(;) isso será util 
	arq.close()
def mostra_pessoas(nomearq):
	cria_arquivo(nomearq)
	arq = open(f'{nomearq}.txt','r')
	for linha in arq.readlines():
		dado = linha.split(';')#assim funciona a função split
		print(f'{dado[0]:<30} {dado[1]}',end='')
	
	arq.close()
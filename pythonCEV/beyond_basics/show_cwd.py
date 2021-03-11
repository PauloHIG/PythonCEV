#diretorio atual(cwd) currently working directory
from pathlib import Path
import os

print(Path.cwd())#pra acessar o diretório atual, basta não começar com 'c:/'(pasta raíz do windows), porém, se eu quiser ver o diretorio atual, posso usar o pathlib
os.chdir('C:\\Users\\paulo\\Desktop')#change directory, muda o diretorio
print(os.getcwd())#outra maneira de ver o diretorio atual em forma de String
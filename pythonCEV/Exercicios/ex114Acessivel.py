import urllib
import urllib.request as zeld
try:
	site = zeld.urlopen('https://www.youtube.com/')
except:
	print('O site não está acessível')
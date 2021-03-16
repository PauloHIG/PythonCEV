import urllib
import urllib.request as zelda

try:
    site = zelda.urlopen("https://www.youtube.com/")
except:
    print("O site não está acessível")
else:
    print("Tá tranquilo")

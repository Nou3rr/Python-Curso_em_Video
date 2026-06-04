import urllib
import urllib.request

try:
    site = urllib.request.urlopen("http://google.com.br")
except urllib.error.URLError:
    print("Não foi possível acessar o site")
else:
    print("O site está online")
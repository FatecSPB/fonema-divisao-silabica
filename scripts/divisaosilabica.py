abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r",
"s","t","u","v","w","x","y","z"]

from bs4 import BeautifulSoup
import urllib.request

file = open('../data/divisaosilabica.csv','wb')
file.write("palavra,tipo,divisao_silabica\n".encode('utf-8'))

for letra in abc:
    r = urllib.request.urlopen('http://www.portaldalinguaportuguesa.org/index.php?action=syllables&act=list&letter='+letra)
    data = r.read()
    soup = BeautifulSoup(data)
    rows = soup.find(id="rollovertable").findAll("tr")
    for row in rows:
        cells = row.findAll("td")
        if cells:
            palavra = cells[0].find('b').find('a').getText()

            file.write(palavra.encode('utf-8'))
            file.write(','.encode('utf-8'))
            tipo = cells[0].getText().split("(")[1].split(")")[0]
            file.write(tipo.encode('utf-8'))
            file.write(','.encode('utf-8'))
            divisaosilabica = cells[1].getText()
            file.write(divisaosilabica.replace("&middot;",".").encode('utf-8'))
            file.write("\n".encode('utf-8'))

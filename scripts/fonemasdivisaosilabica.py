abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r",
"s","t","u","v","w","x","y","z"]

from bs4 import BeautifulSoup
import urllib.request

file = open('../data/foneticadivisaosilabica.csv','wb')
file.write("palavra,fonetica-divisao_silabica\n".encode('utf-8'))

start = 0
change = False


for letra in abc:

    change = False
    start = 0
    while not change:

        r = \
            urllib.request\
                .urlopen('http://www.portaldalinguaportuguesa.org/index.php?action=fonetica&act=list&region=rjx&letter='
                                   +letra+'&start='+str(start))

        data = r.read()
        soup = BeautifulSoup(data)
        rows = soup.find(id="rollovertable").findAll("tr")
        count = 0
        for row in rows:
            cells = row.findAll("td")
            count = count +1
            if cells:
                palavra = cells[0].getText()
                categoria = cells[1].getText()
                fonetica = cells[2].getText()

                file.write(palavra.replace('\n', ' ').replace('\r', '').encode('utf-8'))
                file.write(','.encode('utf-8'))
                file.write(fonetica.replace('\n', ' ').replace('\r', '').encode('utf-8'))
                file.write("\n".encode('utf-8'))
        print(count)
        if count < 21:
            change = True
        start = start + 20
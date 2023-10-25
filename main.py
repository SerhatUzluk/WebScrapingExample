from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('file:///C:/Users/serha/Documents/My%20Web%20Sites/web_scrapping_odev.html')
bs = BeautifulSoup(html.read(), 'html.parser')
a = len(bs)
for i in range(a + 1):
    fiyat = bs.findAll(id='price')[i].get_text().strip()
    print(i + 1, '. ürün')
    print(fiyat)
for i in range(a + 1):
    marka = bs.findAll(id='brand')[i].get_text().strip()
    print(i + 1, '. ürün')
    print("\n", marka)

for i in range(a + 1):
    tur = bs.findAll(id='type')[i].get_text().strip()
    print(i + 1, '. ürün')
    print("\n", tur)

for i in range(a + 1):
    tanim = bs.findAll(id='description')[i].get_text().strip()
    print(i + 1, '. ürün')
    print("\n", tanim)

for i in range(a + 1):
    talimat = bs.findAll(id='instructions')[i].get_text().strip()
    print(i + 1, '. ürün')
    print("\n", talimat)

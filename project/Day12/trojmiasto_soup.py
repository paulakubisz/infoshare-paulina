import requests
from bs4 import BeautifulSoup
from pprint import  pprint

adres = 'https://trojmiasto.pl'

odpowiedz = requests.get(adres)

# print(odpowiedz.status_code)
# odpowiedz.raise_for_status()
# print(odpowiedz.text)

trojmiasto_zupa = BeautifulSoup(odpowiedz.text, "html.parser")

linki = trojmiasto_zupa.select(".news-list a")
# pprint(linki)

for link in linki:
    print(link.getText())
    print(str(link))
    print(link.attrs) #zwraca slownik slownik z atrybutami

print(f"Wiadomość: {link.get(title)}")

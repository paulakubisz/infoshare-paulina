import requests

adres = 'https://trojmiasto.pl'

odpowiedz = requests.get(adres)

assert isinstance(odpowiedz, requests.Response)




# print(odpowiedz.status_code)

#print(odpowiedz.text)

# with open("trojmiasto.html", "w") as plik:
#     plik.write(odpowiedz.text)
#

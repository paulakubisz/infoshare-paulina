
przedmioty = ['bułka', 'chleb', 'makaron', 'cukier']
ceny =       [2.00,     5.00   , 3.50    ]
sztuki =     [20, 5, 7, 40]

# bułka - 20 szt. - cena 2.00 - wartość 40.00

print('---------while')
# while
licznik = 0

while licznik < len(przedmioty):
    przedmiot = przedmioty[licznik]
    cena = ceny[licznik]
    sztuk = sztuki[licznik]
    print(f'{przedmiot} - {sztuk} szt. - cena {cena:.2f} wartosc: {cena * sztuk}')
    licznik += 1

print('---------for\n')

for i in range(len(przedmioty)):
    print(f'{przedmioty[i]} - {sztuki[i]} szt. - cena {ceny[i]} wart: {ceny[i] * sztuki[i]}')

print('---------zip\n')

for towar, price, szt in zip(przedmioty, ceny, sztuki):
    print(f'{towar} - {price} - {szt}')

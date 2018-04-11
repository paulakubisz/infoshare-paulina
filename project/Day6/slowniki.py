#Dickt
# sa pary klucz - wartosc
# kluczem maga byc tuple, stringi, liczba - zawsze musi byc unikatowy
# wartoscia -moga byc powtarzelne

#wyszukujemy przez np. x['klucz'# ]


#program ile reszty mam wydac

monety =      [5, 2, 1, 0.5, 0.2, 0.1]
ilosc_monet = [0, 0, 0,  0,   0,   0]

zakupy = 17.40
banknot = 20.00

reszta = banknot - zakupy

for index, moneta in enumerate(monety):
    if reszta >= moneta:
        ile_monet = reszta // moneta
        ilosc_monet[index] = ile_monet
        reszta -= moneta * ilosc_monet

for moneta, ilosc in zip(monety, ilosc_monet):
    print(f" moneta {moneta} - {ilość} sztuk")



slownik = {1 : "ola", 2: "ala", "imie": "janek",
           "nazwiska" : ["kowalski", "nowak"]}

print(slownik[2])

slownik[2] = 'janek'

print(slownik)

for klucz, wartosc in slownik.items():
    print(f"klucz - {klucz} ma wartosc - {wartosc}")


print(slownik["nazwiska"][1])
#print()
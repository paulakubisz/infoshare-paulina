def imie_wiek_osoby(imie, wiek):
    '''
    Oblicza wiek osoby w miesiacach i wypisuje na ekranie.
    :param imie: str
    :param wiek: int
    '''
    imie = imie.capitalize()
    miesiace = wiek * 12
    print(f'{imie} ma {miesiace} miesięcy!')

x = imie_wiek_osoby('Arek', 12)
# imie_wiek_osoby('Ola', 28)
# imie_wiek_osoby('Monika', 1)
# imie_wiek_osoby('Asia', 10)

print(x)
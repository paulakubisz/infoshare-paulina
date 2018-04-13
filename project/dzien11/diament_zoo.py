from dzien11.diament import Zwierze, Kon, Osiol, Mul

pantofelek = Zwierze('obiekt X')
pantofelek.powiedz()
pantofelek.ruszaj()
print(30*'-')

konik = Kon('Rafał', 'kary')
konik.ruszaj()
konik.powiedz()
print(konik.masc)
print(30*'-')

osiolek = Osiol('Uparciuch')
osiolek.powiedz()
osiolek.ruszaj()
# dynamicznie dodajemy atrybut
osiolek.masc = 'szary'
print(osiolek.masc)
print(30*'-')

zamulacz = Mul('torrent', 'brązowy')
zamulacz.ruszaj()
zamulacz.powiedz()
print(zamulacz.masc)


print(help(Mul))


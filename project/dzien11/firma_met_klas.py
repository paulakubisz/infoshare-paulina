from pprint import pprint

from dzien11.pracownik import Pracownik

p1 = Pracownik('John Travolta', 3000, 'gwiazda wyblakła')
p2 = Pracownik('John Turturo', 1500, 'stara gwiazda')
p3 = Pracownik('John Rambo', 5000, 'killer')

print(Pracownik.ilosc_pracownikow)

del p2

# print(Pracownik.ilosc_pracownikow)
# print('Koniec programu')
# print('----------------')

# Pracownik.ustaw_podwyzke(30)

Pracownik.ustaw_podwyzke(210)

p1.ustaw_podwyzke(220)
p3.ustaw_podwyzke(500)

print(Pracownik.max_podwyzka)

prawidlowy = Pracownik.sprawdz_pesel('2354235235')
print(prawidlowy)

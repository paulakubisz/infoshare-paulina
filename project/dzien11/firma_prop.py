from pprint import pprint

from dzien11.pracownik import Pracownik

p1 = Pracownik('John Travolta', 3000, 'gwiazda wyblakła')
p2 = Pracownik('John Turturo', 1500, 'stara gwiazda')
p3 = Pracownik('John Rambo', 5000, 'killer')

# pprint(Pracownik.__dict__, indent=4)

# Pracownik.ustaw_podwyzke(230)
# Pracownik.__max_podwyzka = 250
# print(Pracownik.__max_podwyzka)

print(p1.pensja)
p1.pensja = 3500
print(p1.pensja)

p1.pensja = 5600
print(p1.pensja)




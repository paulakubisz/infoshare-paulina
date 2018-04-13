from dzien10.czlowiek import Czlowiek
from dzien10.kot import Kot
from dzien10.student import Student
from dzien10.zwierze import Zwierze

zwierz1 = Zwierze('obiekt x')
zwierz2 = Zwierze('pantofelek')

zwierz1.wypisz_nazwe()
zwierz2.wypisz_nazwe()

ludz1 = Czlowiek('Adrian', 'Kowalski', 34)
ludz1.wypisz_nazwe()
ludz1.powiedz_cos()
print(ludz1.wiek)

kotek1 = Kot('Mruczuś', 'rudy')
kotek1.wypisz_nazwe()
print(kotek1.masc)

kotek1.rusz_sie()
ludz1.rusz_sie()
zwierz1.rusz_sie()

student1 = Student("Adam", "Kowalski", 20)

student1.powiedz_cos()

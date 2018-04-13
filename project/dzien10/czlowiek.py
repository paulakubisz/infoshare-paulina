from dzien10.zwierze import Zwierze

class Czlowiek(Zwierze):

    def __init__(self, imie, nazwisko, wiek):
        Zwierze.__init__(self, imie)
        # self.nazwa = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def wypisz_nazwe(self):
        print("Człowiek:", self.nazwa)


    def powiedz_cos(self):
        print('Cześć, mam na imię', self.nazwa)

    def rusz_sie(self):
        print(f'Człowiek {self.nazwa} chodzi.')

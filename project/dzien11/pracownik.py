class Pracownik(object):

    ilosc_pracownikow = 0
    dzien_podatkowy = '30.04.2018'
    _max_podwyzka = 200

    def __init__(self, imie, pensja, stanowisko, pesel=None):
        self.imie = imie.capitalize()
        self.stanowisko = stanowisko
        self.pesel = pesel
        self.godziny = {}
        self.__pensja = pensja
        Pracownik.ilosc_pracownikow += 1

    def pracuj(self, l_godzin, miesiac):
        self.godziny[miesiac] = l_godzin

    def daj_podwyzke(self, wartosc):
        if wartosc <= self.max_podwyzka:
            self.__pensja += wartosc
        else:
            self.__pensja += self.max_podwyzka

    def zmien_stanowisko(self, nowe_stanowisko):
        self.stanowisko = nowe_stanowisko.title()
        print(self.stanowisko)


    def __del__(self):
        Pracownik.ilosc_pracownikow -= 1
        # print(f'Pracownik {self.imie} usunięty.')

    @classmethod
    def ustaw_podwyzke(cls, wartosc):
        cls._max_podwyzka = wartosc
        # if wartosc > cls.max_podwyzka /10:
        #     cls.max_podwyzka *= 1.1
        # else:
        #     cls.max_podwyzka += wartosc

    @staticmethod
    def sprawdz_pesel(pesel):
        if len(pesel) < 11:
            return False
        else:
            return True


    @property
    def pensja(self):
        return f'Pensja: {self.__pensja}'

    @pensja.setter
    def pensja(self, value):
        if value > 4000:
            print('Za duża pensja!!!')
            self.__pensja = 3999
        else:
            self.__pensja = value




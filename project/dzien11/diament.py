class Zwierze(object):
    def __init__(self, nazwa):
        self.nazwa = nazwa

    def powiedz(self):
        print('Zwierze nie mówi.')

    def ruszaj(self):
        print(f'Zwierz {self.nazwa} poruszył się.')

class Kon(Zwierze):
    def __init__(self, nazwa, masc):
        super().__init__(nazwa)
        self.masc = masc

    def powiedz(self):
        print(f'Koń {self.nazwa} mówi Patataj.')

class Osiol(Zwierze):

    def ruszaj(self):
        print(f'Nie ruszam się jestem osłem!')


class Mul(Kon, Osiol):
    def ruszaj(self):
        Zwierze.ruszaj(self)

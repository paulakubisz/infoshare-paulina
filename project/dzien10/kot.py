from dzien10.zwierze import Zwierze

class Kot(Zwierze):
    def __init__(self, imie, masc):
        super().__init__(imie)
        self.masc = masc
        self.wiek = None

    def zamiaucz(self):
        print("Miaaaaau")

    def rusz_sie(self):
        print(f'Kot {self.nazwa} poszedł do miski.')

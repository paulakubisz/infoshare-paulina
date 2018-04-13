from piec import Piec

class Dom(object):

    def __init__(self, powierzchnia, miejscowosc, cena):
        self.powierzchnia = powierzchnia
        self.miejscowosc = miejscowosc
        self.cena = cena
        self.oddany = False
        self.piecyk = None

    def oddaj_do_uzytku(self):
        if not self.oddany:
            self.oddany = True
            self.cena *= 1.15


    def __str__(self):
        return f'Dom w {self.miejscowosc} pow. {self.powierzchnia} ' \
               f'cena: {self.cena}.'


    def __gt__(self, other):
        return self.powierzchnia > other.powierzchnia

    def __add__(self, other):
        return (self.cena + other.cena,
                self.powierzchnia + other.powierzchnia)


class DomLetniskowy(Dom):
    def __init__(self,powierzchnia , miejscowosc, caloroczny):
        super().__init__(powierzchnia, None, miejscowosc)
        self.caloroczny = caloroczny

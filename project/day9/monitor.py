class Monitor(object):

    def __init__(self, marka, przekatna):
        self.marka = marka
        self.przekatna = przekatna
        self.rozdzielczosc = "1920x1080"
        self.kolor = "czarny"
        self.wlaczony = False

    def wlacz(self):
        self.wlaczony = True

    def wylacz(self):
        self.wlaczony = False

    def obroc(self):
        rozdzialka = self.rozdzielczosc.split('x')
        nowa_rozdzialka = rozdzialka[1] + 'x' + rozdzialka[0]
        self.rozdzielczosc = nowa_rozdzialka

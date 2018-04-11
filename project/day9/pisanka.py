import random

class Pisanka(object):
    def __init__(self, kolor):
        self.color = kolor
        self.typ = None
        self.zostalo = 100

    def __str__(self):
        return f"Jajo typu {self.typ}', zostało:{self.zostalo}, koloru: {self.color}"

    def __repr__(self):
        return f"<Jajo koloru: {self.color}>"


    def przefarbuj(self):
        kolory = ['zielony', 'czerwony', 'żółty', 'różowy', ]
        wylosowany_kolor = random.choice(kolory)
        self.color = wylosowany_kolor

    def zjedz(self, procent):
        if procent > self.zostalo:
            self.zostalo = 0
        else:
            self.zostalo -= procent #sel.zostalo - procent


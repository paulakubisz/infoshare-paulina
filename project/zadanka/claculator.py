class Calculator():

    def dodaj(self, a ,b):
        wynik = a+b
        print(wynik)

    def odejmij(self,a, b):
        wynik = a-b
        print(wynik)

kalkulator = Calculator()
kalkulator.dodaj(3,4)
kalkulator.odejmij(4,5)
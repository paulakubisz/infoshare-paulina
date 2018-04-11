from unittest import TestCase
from dzien11.pracownik import Pracownik

class TestsPracownik(TestCase):

    def setUp(self):
        imie = "adam"
        stanowisko = "kierowca"
        pensja = 2000
        self.pracownik = Pracownik(imie,pensja,stanowisko)

    def test_init(self):
        # arrange
        # act
        #assert
        imie_expected = imie.capitalize()
        self.assertEqual(imie_expected, pracownik.imie)
        stan_exp = stanowisko
        self.assertEqual(stan_exp, pracownik.stanowisko)


    def test_pensja(self):

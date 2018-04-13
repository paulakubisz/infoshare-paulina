from unittest import TestCase
from project.dzien11.pracownik import Pracownik

class TestsPracownik(TestCase):

    def setUp(self):
        self.imie = 'adam'
        self.stanowisko = 'kierowca'
        self.pensja = 2000
        self.pracownik = Pracownik(self.imie,
                                   self.pensja,
                                   self.stanowisko)

    def test_init(self):
        # assert
        imie_expected = self.imie.capitalize()
        self.assertEqual(imie_expected, self.pracownik.imie)
        stan_exp = self.stanowisko
        self.assertEqual(stan_exp, self.pracownik.stanowisko)


    def test_pensja_get(self):
        pensja_exp = f'Pensja: {self.pensja}'

        self.assertEqual(pensja_exp, self.pracownik.pensja)

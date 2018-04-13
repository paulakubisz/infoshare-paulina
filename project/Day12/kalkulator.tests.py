from unittest import TestCase
from project.Day12.kalkulator import dodaj
from project.tools.catch_print import get_print_output

class KalkulatorTest(TestCase):

    def test_dodaj(self):
        #arrange
        a = 23
        b = 17
        #act
        output = get_print_output(dodaj,a,b)
        #assert
        self.assertEqual(a+b, output)
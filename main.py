from trojmian import Trojmian
import unittest


class TestTrojmian(unittest.TestCase):

    def test1_2_3(self):
        kwadratowa = Trojmian()
        wynik = kwadratowa.licz_miejsca_zerowe(1, 2, 3)
        self.assertIs(wynik, False)

    def test0_2_3(self):
        kwadratowa = Trojmian()
        wynik = kwadratowa.licz_miejsca_zerowe(0, 2, 3)
        self.assertEqual(wynik, -1.50)

    def test1_5_4(self):
        kwadratowa = Trojmian()
        wynik = kwadratowa.licz_miejsca_zerowe(1, 5, 4)
        self.assertEqual(wynik, [-4, -1])


if __name__ == '__main__':
    unittest.main()

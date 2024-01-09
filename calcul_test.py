import unittest
from calcul import ajouter, multiplier, soustraire, ajouter_puis_multiplier


class TestCalcul(unittest.TestCase):

    def test_ajouter(self):
        self.assertEqual(ajouter(1, 2), 3)
        self.assertEqual(ajouter(-1, 1), 0)
        self.assertEqual(ajouter(-1, -1), -2)

    def test_multiplier(self):
        self.assertEqual(multiplier(2, 3), 6)
        self.assertEqual(multiplier(0, 3), 0)
        self.assertEqual(multiplier(-2, 3), -6)

    def test_soustraire(self):
        self.assertEqual(soustraire(2, 2), 0)
        self.assertEqual(soustraire(2, 0), 2)
        self.assertEqual(soustraire(0, 2), -2)

    def test_ajouter_puis_multiplier(self):
        self.assertEqual(ajouter_puis_multiplier(
            1, 2, 3), 9)      # (1+2)*3 = 9
        self.assertEqual(ajouter_puis_multiplier(
            2, 3, 4), 20)     # (2+3)*4 = 20
        self.assertEqual(ajouter_puis_multiplier(
            0, 5, 2), 10)     # (0+5)*2 = 10


if __name__ == '__main__':
    unittest.main()

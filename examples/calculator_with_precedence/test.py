"""Tests para parser."""
import unittest
from parser import parse


class ParserTest(unittest.TestCase):
    """Tests para el parser."""

    def test_suma_bien_dos_numeros(self):
        self.assertEqual(parse("1+1"), 2)

    def test_suma_bien_tres_numeros(self):
        self.assertEqual(parse("1+   2 + 3"), 6)

    def test_multiplica_dos_numeros(self):
        self.assertEqual(parse("3 * 4"), 12)

    def test_multiplica_y_suma(self):
        self.assertEqual(parse("2 * 4 + 3"), 11)

    def test_suma_y_multiplica(self):
        self.assertEqual(parse("2 + 4 * 3"), 14)

    def test_resuelve_parentesis(self):
        self.assertEqual(parse("(2 + 3) * 4"), 20)

    def test_resuelve_negacion(self):
        self.assertEqual(parse("-2"), -2)

if __name__ == '__main__':
    unittest.main()

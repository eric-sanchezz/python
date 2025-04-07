import unittest
import math

from pt2_act2 import obtenir_numero  
from pt2_act2 import calcular  

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None

def arrel_quadrada(a):
    try:
        if a < 0:
            raise ValueError
        return math.sqrt(a)
    except ValueError:
        return None


class TestCalculadora(unittest.TestCase):

    def setUp(self):
        print("Inicialitzant test...")

    def tearDown(self):
        print("Finalitzant test...")

    def test_suma(self):
        self.assertEqual(sumar(2, 3), 5)
        self.assertEqual(sumar(0, 0), 0)

    def test_resta(self):
        self.assertEqual(restar(5, 3), 2)
        self.assertEqual(restar(0, 0), 0)

    def test_multiplicacio(self):
        self.assertEqual(multiplicar(4, 5), 20)
        self.assertEqual(multiplicar(0, 100), 0)

    def test_divisio(self):
        self.assertEqual(dividir(10, 2), 5)
        self.assertIsNone(dividir(4, 0)) 

    def test_arrel_quadrada(self):
        self.assertEqual(arrel_quadrada(9), 3)
        self.assertIsNone(arrel_quadrada(-9)) 

if __name__ == '__main__':
    unittest.main()

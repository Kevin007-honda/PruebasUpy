import unittest
import math
from calculadora import * # Importamos todas las funciones de calculadora.py

class TestCalculadora(unittest.TestCase):

    def test_seno(self):
        self.assertAlmostEqual(seno(0), 0)
        self.assertAlmostEqual(seno(math.pi / 2), 1)
        self.assertAlmostEqual(seno(math.pi), 0)

    def test_coseno(self):
        self.assertAlmostEqual(coseno(0), 1)
        self.assertAlmostEqual(coseno(math.pi / 2), 0)
        self.assertAlmostEqual(coseno(math.pi), -1)

    def test_tangente(self):
        self.assertAlmostEqual(tangente(0), 0)
        self.assertAlmostEqual(tangente(math.pi / 4), 1)
        # Para ángulos donde la tangente tiende a infinito, podríamos probar límites o manejar la excepción si es necesario.

    def test_arcoseno(self):
        self.assertAlmostEqual(arcoseno(0), 0)
        self.assertAlmostEqual(arcoseno(1), math.pi / 2)
        self.assertAlmostEqual(arcoseno(-1), -math.pi / 2)
        with self.assertRaises(ValueError):
            arcoseno(1.1) # Prueba para valores fuera del dominio [-1, 1]

    def test_arcocoseno(self):
        self.assertAlmostEqual(arcocoseno(1), 0)
        self.assertAlmostEqual(arcocoseno(0), math.pi / 2)
        self.assertAlmostEqual(arcocoseno(-1), math.pi)
        with self.assertRaises(ValueError):
            arcocoseno(-1.1) # Prueba para valores fuera del dominio [-1, 1]

    def test_arcotangente(self):
        self.assertAlmostEqual(arcotangente(0), 0)
        self.assertAlmostEqual(arcotangente(1), math.pi / 4)
        self.assertAlmostEqual(arcotangente(-1), -math.pi / 4)

    def test_potencia(self):
        self.assertAlmostEqual(potencia(2, 3), 8)
        self.assertAlmostEqual(potencia(5, 0), 1)
        self.assertAlmostEqual(potencia(4, 0.5), 2)

    def test_log_base_10(self):
        self.assertAlmostEqual(log_base_10(100), 2)
        self.assertAlmostEqual(log_base_10(1), 0)
        with self.assertRaises(ValueError):
            log_base_10(0)
        with self.assertRaises(ValueError):
            log_base_10(-1)

    def test_log_natural(self):
        self.assertAlmostEqual(log_natural(math.e), 1)
        self.assertAlmostEqual(log_natural(1), 0)
        with self.assertRaises(ValueError):
            log_natural(0)
        with self.assertRaises(ValueError):
            log_natural(-1)

    def test_raiz_cuadrada(self):
        self.assertAlmostEqual(raiz_cuadrada(9), 3)
        self.assertAlmostEqual(raiz_cuadrada(0), 0)
        with self.assertRaises(ValueError):
            raiz_cuadrada(-1)

    def test_raiz_enesima(self):
        self.assertAlmostEqual(raiz_enesima(8, 3), 2)
        self.assertAlmostEqual(raiz_enesima(16, 4), 2)
        self.assertAlmostEqual(raiz_enesima(27, 3), 3)
        with self.assertRaises(ValueError):
            raiz_enesima(-8, 3) # Raíz cúbica de un negativo es válida, pero pow con exponente fraccionario no siempre

    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
        with self.assertRaises(ValueError):
            factorial(-1)
        with self.assertRaises(TypeError):
            factorial(5.5)

    def test_inverso(self):
        self.assertAlmostEqual(inverso(2), 0.5)
        self.assertAlmostEqual(inverso(0.5), 2)
        with self.assertRaises(ZeroDivisionError):
            inverso(0)

    def test_pi(self):
        self.assertAlmostEqual(pi(), math.pi)

    def test_seno_hiperbolico(self):
        self.assertAlmostEqual(seno_hiperbolico(0), 0)
        self.assertAlmostEqual(seno_hiperbolico(1), math.sinh(1))

    def test_coseno_hiperbolico(self):
        self.assertAlmostEqual(coseno_hiperbolico(0), 1)
        self.assertAlmostEqual(coseno_hiperbolico(1), math.cosh(1))

    def test_tangente_hiperbolica(self):
        self.assertAlmostEqual(tangente_hiperbolica(0), 0)
        self.assertAlmostEqual(tangente_hiperbolica(1), math.tanh(1))

    def test_combinaciones(self):
        self.assertEqual(combinaciones(5, 2), 10)
        self.assertEqual(combinaciones(4, 0), 1)
        self.assertEqual(combinaciones(3, 3), 1)
        with self.assertRaises(ValueError):
            combinaciones(2, 3) # r > n
        with self.assertRaises(ValueError):
            combinaciones(-1, 2) # n < 0
        with self.assertRaises(ValueError):
            combinaciones(3, -1) # r < 0

if __name__ == '__main__':
    unittest.main()
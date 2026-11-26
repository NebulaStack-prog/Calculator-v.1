import math
import runpy
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sources = list(ROOT.glob("Calculator_v.*.py"))
if len(sources) != 1:
    raise RuntimeError("Expected exactly one calculator source")
Calculator = runpy.run_path(str(sources[0]))["Calculator"]


class CalculatorTests(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator.__new__(Calculator)

    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(10, 4), 6)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(-3, 4), -12)

    def test_division(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(10, 0)

    def test_power(self):
        self.assertEqual(self.calc.power(2, 10), 1024)

    def test_square_root(self):
        self.assertEqual(self.calc.sqrt(81), 9)

    def test_negative_square_root(self):
        with self.assertRaises(ValueError):
            self.calc.sqrt(-1)

    def test_factorial(self):
        self.assertEqual(self.calc.factorial(5), 120)
        self.assertEqual(self.calc.factorial(0), 1)

    def test_double_factorial(self):
        self.assertEqual(self.calc.double_fact(6), 48)
        self.assertEqual(self.calc.double_fact(5), 15)

    def test_gcd(self):
        self.assertEqual(self.calc.gcd(48, 18), 6)

    def test_lcm(self):
        self.assertEqual(self.calc.lcm(12, 18), 36)
        self.assertEqual(self.calc.lcm(0, 18), 0)

    def test_trigonometry(self):
        self.assertAlmostEqual(self.calc.sin(30), 0.5)
        self.assertAlmostEqual(self.calc.cos(60), 0.5)

    def test_angle_conversion(self):
        self.assertAlmostEqual(self.calc.deg_to_rad(180), math.pi)
        self.assertAlmostEqual(self.calc.rad_to_deg(math.pi), 180)

    def test_linear_equation(self):
        self.assertEqual(self.calc.solve_linear(2, -8), 4)

    def test_logarithm(self):
        self.assertAlmostEqual(self.calc.logarithm(2, 8), 3)

    def test_invalid_logarithm(self):
        with self.assertRaises(ValueError):
            self.calc.logarithm(1, 8)

    def test_tangent_undefined(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.tan(270)


if __name__ == "__main__":
    unittest.main()

import unittest
import basic_calculator


class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEquals(basic_calculator.addition(2, 2), 4)
        self.assertEquals(basic_calculator.addition(-2, 2), 0)
        self.assertEquals(basic_calculator.addition(-2, -2), -4)

    def test_substraction(self):
        self.assertEquals(basic_calculator.substraction(2, 2), 0)
        self.assertEquals(basic_calculator.substraction(-2, 2), -4)
        self.assertEquals(basic_calculator.substraction(-2, -2), 0)

    def test_multiplication(self):
        self.assertEquals(basic_calculator.multiplication(2, 2), 4)
        self.assertEquals(basic_calculator.multiplication(-2, 2), -4)
        self.assertEquals(basic_calculator.multiplication(-2, -2), 4)

    def test_division(self):
        self.assertEquals(basic_calculator.division(2, 2), 1)
        self.assertEquals(basic_calculator.division(-2, 2), -1)
        self.assertEquals(basic_calculator.division(-2, -2), 1)
        self.assertEquals(basic_calculator.division(1, 2), 0.5)

        with self.assertRaises(ValueError):
            basic_calculator.division(2, 0)

    def test_power(self):
        self.assertEquals(basic_calculator.power(2, 2), 4)
        self.assertEquals(basic_calculator.power(-2, 2), 4)
        self.assertEquals(basic_calculator.power(2, 0), 1)
        self.assertEquals(basic_calculator.power(0, 2), 0)

        with self.assertRaises(ValueError):
            basic_calculator.power(2, -2)

    def test_sqroot(self):
        self.assertEquals(basic_calculator.sqroot(4), 2)
        self.assertEquals(basic_calculator.sqroot(0), 0)

        with self.assertRaises(ValueError):
            basic_calculator.sqroot(-2)




if __name__ == '__main__':
    unittest.main()

# To Run in Console:
# python -m unittest test_calculator.py

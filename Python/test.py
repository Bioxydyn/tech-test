import unittest
from equation import wash_in_equation

class TestEquation(unittest.TestCase):
    def test_1(self):
        self.assertEqual(wash_in_equation(5),1.0)

    def test_2(self):
        self.assertAlmostEqual(wash_in_equation(15), 2.703796849,  delta=0.02703796849)

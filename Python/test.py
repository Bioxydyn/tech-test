import unittest
from equation import wash_in_equation

class TestEquation(unittest.TestCase):
    def test(self):
        self.assertEqual(wash_in_equation(0),0)

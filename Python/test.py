import unittest
from equation import wash_in_equation, area_under_wash_in_equation

class TestEquation(unittest.TestCase):
    def test_washInEquation(self):
        self.assertEqual(wash_in_equation(5),1.0)
        self.assertAlmostEqual(wash_in_equation(15), 2.703796849, delta=0.01)

    def test_areaUnderCurve(self):
        self.assertEqual(area_under_wash_in_equation(0.0), 0.0)
        self.assertAlmostEqual(area_under_wash_in_equation(15), 19.5544378120266, delta=0.4)

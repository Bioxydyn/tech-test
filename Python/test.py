import unittest
from equation import wash_in_equation, 

class TestEquation(unittest.TestCase):
    def test_washInEquation(self):
        self.assertEqual(wash_in_equation(5),1.0)
        self.assertAlmostEqual(wash_in_equation(15), 2.703796849,  delta=0.01)

    def teast_areaUnderCurve(self):
        self.assertEqual(area_under_wash_in_equation(5),1.0)
        self.assertAlmostEqual(area_under_wash_in_equation(15), 19.554623001714354,  delta=0.4)

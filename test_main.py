import unittest
from main import CalculationBenefit

class TestCalculations(unittest.TestCase):
    Calculationclasstest = CalculationBenefit()

    def test_classexist(self):
        self.assertEqual([300, 300], CalculationBenefit().funcA("coo","coo"), "error calcbenefit")

if __name__ == '__main__':
    unittest.main()
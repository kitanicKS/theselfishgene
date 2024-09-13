"""Module providing an Axelrod computer test."""

import unittest
from main import CalculationBenefit

class TestCalculations(unittest.TestCase):
    """Class provides a test for functions for benefit calculation"""
    Calculationclasstest = CalculationBenefit()

    def test_classexist(self):
        """Function for first test."""
        self.assertEqual([300, 300], CalculationBenefit().func_a("coo","coo"), "error calcbenefit")

if __name__ == '__main__':
    unittest.main()

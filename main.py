"""Module providing an Axelrod computer test."""

# pylint: disable=R1710
# pylint: disable=R0903

class CalculationBenefit():
    """Class provides functions for benefit calculation"""
    def __init__(self):
        pass

    def func_a(self, movera, moverb):
        """Function for first test."""
        if movera=="coo" and moverb=="coo":
            return [300,300]

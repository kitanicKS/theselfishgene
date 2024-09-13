
class CalculationBenefit():
    """Class provides functions for benefit calculation"""
    def __init__(self):
        pass

    def funcA(self, movera, moverb):
        if movera=="coo" and moverb=="coo":
            return [300,300]
        else:
            return "error"
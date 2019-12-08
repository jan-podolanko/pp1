import math
class fraction():
    def __init__(self, a, b):
        self.numerator = a
        self.denominator = b
    def display_fraction(self):
        print(f'{int(self.numerator)}/{int(self.denominator)}')
    def simplify(self):
        self.gcd = math.gcd(self.numerator,self.denominator)
        self.numerator /= self.gcd
        self.denominator /= self.gcd

x = fraction(1,2)
x.display_fraction()
x = fraction(12,21)
x.simplify()
x.display_fraction()
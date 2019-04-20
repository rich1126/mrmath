import math
"""
This is a fraction class that allows creation of fractions
by defining a numerator and denominator, or by stating
an integer of float.

All fractions are immediately reduced to lowest terms.
Supports basic arithmetic operations, and float.

"""
class frac:
    def __init__(self, numerator, denominator = None):
        """
        Initializes class, not allowing for 0 denominator.
        If no denominator is stated, looks for a decimal
        and converts. Otherwise, takes integer.
        Otherwise, accepts numerator and denominator
        and reduces to lowest terms.
        Also defaults to negative fractions being displayed
        as "-x/y"
        """
        if denominator == 0:
            raise ZeroDivisionError
        elif denominator == None:
            if '.' in str(numerator):
                p = len(str(numerator).split('.')[1])
                if '-' not in str(numerator):
                    num0 = ( int(str(numerator).split('.')[0])*(10**p)
                         +int(str(numerator).split('.')[1])
                         )
                    den0 = 10**p
                else:                    
                    num0 = ( int(str(numerator).split('.')[0])*(10**p)
                         -int(str(numerator).split('.')[1])
                         )
                    den0 = 10**p
                self.num = int(num0 / math.gcd(num0, den0))
                self.den = int(den0 / math.gcd(num0, den0))
            else:
                self.num = numerator
                self.den = 1
        else:
            if denominator < 0:
                numerator *= -1
                denominator *= -1
            self.num = int(numerator / math.gcd(numerator,denominator))
            self.den = int(denominator / math.gcd(numerator,denominator))

    def __repr__(self):
        """
        If denominator is 1, juts return as integer. Otherwise
        display as normal fraction: x/y.
        """
        if self.den != 1:
            return f'{self.num}/{self.den}'
        else:
            return f'{self.num}'

    def __add__(self, other):
        if type(other) == int or type(other) == float:
            other = frac(other)
        num = (self.num * other.den) + (self.den * other.num)
        den = self.den * other.den
        return frac(num, den)

    def __sub__(self, other):
        if type(other) == int or type(other) == float:
            other = frac(other)
        num = (self.num * other.den) - (self.den*other.num)
        den = self.den * other.den
        return frac(num, den)

    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            return frac(self.num * other, self.den)
        else:
            return frac(self.num * other.num, self.den * other.den)

    __rmul__ = __mul__

    def __truediv__(self, other):
        if type(other) == int or type(other) == float:
            other = frac(other)
        return frac(self.num * other.den, self.den * other.num)

    def __rtruediv__(self, other):
        if type(other) == int or type(other) == float:
            other = frac(other)
        return frac(other.num * self.den, other.den * self.num)

    def __float__(self):
        return int(self.num) / int(self.den)

    def __pow__(self, power):
        return frac(self.num ** power, self.den ** power)

    def __eq__(self, other):
        if type(other) == frac:
            if self.num == other.num and self.den == other.den:
                return True
            else: return False
        else:
            return False

    def __lt__(self, other):
        if float(self) < float(other):
            return True
        else:
            return False

    def __gt__(self, other):
        return other < self

    def __le__(self, other):
        if self < other or self == other:
            return True
        else:
             return False

    def __ge__(self, other):
        return other <= self

    def roundInt(self):
        return int(round(float(self)))

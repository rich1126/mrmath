import math

class Complex(object):

    def __init__(self,r,i):
        self.Real = r
        self.Imaginary = i

    def __repr__(self):
        return '%s + %si' % (self.Real, self.Imaginary)

    def __add__(self,rhs):
        return Complex(self.Real+rhs.Real, self.Imaginary+rhs.Imaginary)
    def __mul__(self,other):
        return Complex(self.Real*other.Real -self.Imaginary*other.Imaginary,
                self.Imaginary*other.Real + self.Real*other.Imaginary)
    __rmul__ = __mul__

    def __abs__(self):
        return (self.Real**2 + self.Imaginary**2)**0.5



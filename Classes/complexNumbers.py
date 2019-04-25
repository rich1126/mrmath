import math
from frac import *
from vector2D import *

class Complex(object):

    def __init__(self,r,i = 0):
        if type(r) == float:
            if int(r) == r:
                self.Real = int(r)
            else:
                self.Real = r
        else:
            self.Real = r
        
        if type (i) == float:
            if int(i) == i:
                self.Imaginary = int(i)
            else:
                self.Imaginary = i
        else: 
            self.Imaginary = i

    def __repr__(self):
        if self.Imaginary > 0:
            return f'{self.Real} + {self.Imaginary}i'
        elif self.Imaginary < 0:
            return f'{self.Real} - {-self.Imaginary}i'
        else:
            return f'{self.Real}'

    def __add__(self,other):
        if type(other) == int or type(other) == float or type(other) == frac:
            other = Complex(other)
        return Complex(self.Real+other.Real, self.Imaginary+other.Imaginary)
        
    def __sub__(self, other):
        if type(other) == int or type(other) == float or type(other) == frac:
            other = Complex(other)
        return Complex(self.Real - other.Real, self.Imaginary - other.Imaginary)
        
    def __neg__(self):
        return Complex(-self.Real, -self.Imaginary)
        
    def __mul__(self,other):
        if type(other) == int or type(other) == float or type(other) == frac:
            other = Complex(other)
        return Complex(self.Real*other.Real -self.Imaginary*other.Imaginary,
                self.Imaginary*other.Real + self.Real*other.Imaginary)
                
    def __rmul__(self,other):
        if type(other) == int or type(other) == float or type(other) == frac:
            other = Complex(other)
        return Complex(self.Real*other.Real -self.Imaginary*other.Imaginary,
                self.Imaginary*other.Real + self.Real*other.Imaginary)

    
    def __truediv__(self, other):
        if type(other) == int or type(other) == float or type(other) == frac:
            other = Complex(other)
        return Complex((self*other).Real / (other*other.conj()).Real, \
                        (self*other).Imaginary / (other*other.conj()).Real)
        
    def __rtruediv__(self, other):
        if type(other) == int or type(other) == float or type(other) == frac:
            other = Complex(other)
        return Complex((self*other).Real / (self*self.conj()).Real, \
                        (self*other).Imaginary / (self*self.conj()).Real)

    def __abs__(self):
        return (self.Real**2 + self.Imaginary**2)**0.5
        
    def asFrac(self):
        x = frac(self.Real)
        y = frac(self.Imaginary)
        return Complex(x,y)
        
    def asVector(self):
        return vtwo(self.Real, self.Imaginary)
        
    def conj(self):
        return Complex(self.Real, -self.Imaginary)



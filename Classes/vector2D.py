import math
from .complexNumbers import *
from .frac import *
from .asymptote import *

class vtwo: 
    """
    A class for 2D vectors. Supports basic vector operations.
    """

    def __init__(self, x = 1, y = 0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'({self.x}, {self.y})'

    def __add__(self, other):
        return vtwo(self.x + other.x, self.y + other.y)
        
    def __sub__(self, other):
        return vtwo(self.x - other.x, self.y - other.y)

    def scale(self, constant): ## Scalar multiplication
        return vtwo(constant * self.x, constant * self.y)

    def __abs__(self):
        return math.sqrt(float(self.x**2) + float(self.y**2))

    def __eq__(self,other):
        if other  == None:
            return False
        elif self.x == other.x and self.y == other.y:
            return True
        else:
            return False
            
    def __neg__(self):
        return vtwo(-self.x, -self.y)
    
    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def cross(self, other):
        return self.x * other.y - self.y*other.x

    def angle(self, u = 'r', other = None, precision = 2):
        """
        Gives standard-position angle 
        counterclockwise from x axis.

        If optional other given, finds angle between vectors.
        """
        self.x = float(self.x)
        self.y = float(self.y)
        if other == None:
            if self.x == 0:
                if self.y > 0:
                    a = math.pi/2
                if self.y < 0:
                    a = 3*math.pi/2
                else:
                    a = 0
            if self.x > 0:
                a = math.atan(self.y / self.x)
                if a < 0:
                    a += 2*math.pi
            else:
                a = math.atan(self.y / self.x) + math.pi
        else:
            other.x = float(other.x)
            other.y = float(other.y)
            if self == vtwo(0,0) or other == vtwo(0,0):
                raise ZeroDivisionError
            else:
                a =  math.acos(self.dot(other) / (abs(self)*abs(other)))
        if u == 'r':
            return round(a, precision)
        else:
            return round(a * 180 / math.pi,precision)

    def proj(self, other): ## Projection of self onto other
        c = self.dot(other) / other.dot(other)
        return other.scale(c)

    def asFrac(self):
        x = frac(self.x)
        y = frac(self.y)
        return vtwo(x,y)
    
    def asComplex(self):
        return Complex(self.x, self.y) 
        
    def draw(self, ctx, o): ## Draw onto an asy() diagram
        ctx.draw(str(o) + "--("+str(self.x + o.x)+","+str(self.y+o.y)+"),EndArrow")
        


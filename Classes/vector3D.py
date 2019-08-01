import math

from .frac import *

class vthree:
    """
    A class for 3D vectors. Supports basic vector operations
    """

    def __init__(self, x=1,y=0,z=0):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f'({self.x}, {self.y}, {self.z})'

    def __add__(self, other):
        return vthree(self.x+other.x, self.y+other.y, self.z+other.z)

    def __sub__(self,other):
        return vthree(self.x-other.x, self.y-other.y, self.z-other.z)

    def scale(self, constant): ## Scalar multiplication
        return vthree(constant*self.x, constant*self.y, constant*self.z)

    def __abs__(self):
        return math.sqrt( float(self.x**2)+float(self.y**2)+float(self.z**2))

    def __eq__(self, other):
        if other == None:
            return False
        elif self.x == other.x and self.y==other.y and self.z==other.z:
            return True
        else:
            return False

    def __neg__(self):
        return vthree(-self.x, -self.y, -self.z)

    def dot(self, other):
        return self.x*other.x + self.y*other.y + self.z*other.z

    def cross(self, other):
        return vthree(self.y*other.z-self.z*other.y, \
                self.z*other.x-self.x*other.z,\
                self.x*other.y - self.y*other.x)

    def unit(self):
        return self.scale(1/abs(self))



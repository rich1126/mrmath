import math
"""
This is a polynomial class that allows the creation of a polynomial.
It is stored as a list of coefficients, indexed from 0
[x^0, x^1, x^2 ... ]

Supports addition, subtraction, multiplication.
"""

class poly:
    def __init__(self, coeff):
        """
        Initializes class, where coeff is a list of coefficients.

        Immediately makes sure leading coefficient is not 0.
        Then establishes degree.
        """

        self.co = coeff
        while self.co[-1] == 0 and len(self.co) > 1:
            del self.co[-1]

        self.deg = len(self.co) - 1


    def __repr__(self):
        """
        Represents as polynomial in x
        If it's the 0 polynomial, you just get 0.
        If deg >= 1, all 0 coefficients do not appear.
        Currently preferring to do "+ -7x" type thing for clarity.
        """
        if self.deg == 0:
            return str(self.co[0])
        else:
            i = 0
            while self.co[i] == 0:
                i += 1
            if i == 0:
                polyString = str(self.co[i])
            else:
                polyString = str(self.co[i])+'x^'+str(i)
            for j in range(i+1,len(self.co)):
                if self.co[j] == 1:
                    polyString += ' + ' + 'x^' + str(j)
                elif self.co[j] != 0:
                    polyString += ' + ' + str(self.co[j]) + 'x^' + str(j)
                else:
                    pass

        return polyString

    def __neg__(self):
        newCo = [-i for i in self.co]
        return poly(newCo)

    def __add__(self,other):
        """
        Simple polynomial addition
        """
        newCoeff = [0 for i in range(1+max(self.deg, other.deg))]
        for i in range(len(self.co)):
            newCoeff[i] += self.co[i]

        for i in range(len(other.co)):
            newCoeff[i] += other.co[i]

        return poly(newCoeff)

    def __sub__(self,other):
        """
        Simple polynomial subtraction
        """
        return self+ (-other)

    def __mul__(self, other):
        """
        Multiplication by other polynomial or by constant
        """
        if type(other) == int or type(other) == float:
            other = poly([other]) 
        newCo = [0 for i in range(self.deg + other.deg+1)]
        for t1 in range(len(self.co)):
            for t2 in range(len(other.co)):
                newCo[t1+t2] += self.co[t1]*other.co[t2]
        return poly(newCo)

    def __rmul__(self, other):
        """
        Multiplication by other polynomial or by constant
        """
        if type(other) == int or type(other) == float:
            other = poly([other]) 
        newCo = [0 for i in range(self.deg + other.deg+1)]
        for termSelf in range(len(self.co)):
            for termOther in range(len(other.co)):
                newCo[termSelf + termOther] += \
                self.co[termSelf] * other.co[termOther]
        return poly(newCo)


    def eval(self, value):
        polyVal = 0
        for i in range(len(self.co)):
            polyVal += self.co[i] * (value**i)

        return polyVal

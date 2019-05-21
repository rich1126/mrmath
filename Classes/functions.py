# Miscellaneous functions that don't belong elsewhere

import math


##############################################
##############################################
'''
Defining Errors used later
'''

class Error(Exception):
    pass

class InvalidTriangleError(Error):
    '''Raised when triangle is invalid'''
    def __init__(self):
        self.message = 'Invalid Triangle'
        
    

###############################################
###############################################
'''
Actual functions begin here
'''

def triOrigin(a, b, c):
    '''
    Given three sides of a triangle, assume 
    one point at (0,0), other at (a,0). Finally,
    assumes third point is "above" horizontal line.
    Returns list of points making that triangle.
    '''
    if a + b <= c or a + c <= b or b + c <= a: #Check triangle inequality
        raise InvalidTriangleError()
    else:
        pointList = [(0,0), (a,0)]
        cTheta = (a**2 + c**2 - b**2) / (2*a*c) #Law of Cosines
        sTheta = math.sqrt(1 - cTheta**2) #Pythagorean Identity
        pointList.append((c*cTheta, c*sTheta))
        return pointList



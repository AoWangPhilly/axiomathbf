from sympy import *


class Vector:
    def __init__(self, i=0, j=0, k=0):
        self.vector = Matrix((i, j, k))

    def __str__(self):
        pass

    def getAngle(self, other):
        return acos(self.vector.dot(other) / (self.vector.norm() * other.norm()))
    
    def getDirCosine(self):
        


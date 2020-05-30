from sympy import *
from sympy.calculus.util import continuous_domain


class Vector:
    def __init__(self, i=0, j=0, k=0):
        self.vector = Matrix((i, j, k))
        self.__t = Symbol('t')

    def __str__(self):
        v = self.vector
        return '{}i + {}j + {}k'.format(v[0], v[1], v[2])

    def getAngle(self, other):
        return acos(self.vector.dot(other) / (self.vector.norm() * other.norm()))

    def getDirCosine(self):
        return [acos(unit/self.vector.norm()) for unit in self.vector]

    def getProjection(self, other):
        return (self.vector.dot(other)/(other.norm()**2))*other

    def getVector(self):
        return self.vector

    def setVector(self, vector):
        self.vector = vector

    def getCrossArea(self, other):
        return self.vector.cross(other).norm()

    def getPPVolume(self, v, w):
        return abs(self.vector.dot(v.cross(w)))

    def getPlane(self, point):
        normVect = self.vector
        return normVect[0] * (self.x - point.x) + normVect[1] * (self.y - point.y) +\
            normVect[2] * (self.z - point.z)

    def compareVector(self, other):
        result = ""
        if self.vector.dot(other) == 0:
            result = "Perpendicular"
        elif self.vector.cross(other).norm() == 0:
            result = "Parallel"
        else:
            result = "Skew"
        return "{} and {}: {}".format(self.vector, other, result)

    def getPointVectorLine(self, point):
        x, y, z = point
        v1, v2, v3 = self.vector
        return '<x,y,z> = <{},{},{}> + <{},{},{}>t'.format(x, y, z, v1, v2, v3)

    def getDomainOfVectFunc(self):
        domain = Interval(-oo, oo)
        domainOfFunctions = []
        t = self.__t
        for function in self.vector:
            domainOfFunctions.append(continuous_domain(function, t, S.Reals))
            domain = Intersection(continuous_domain(
                function, t, S.Reals), domain)
        return (domain, domainOfFunctions)

    def derive(self):
        return Matrix([diff(function, self.__t) for function in self.vector])

    def integrate(self):
        return Matrix([integrate(function, self.__t) for function in self.vector])

    def getTangentLine(self, point, t):
        pass

if __name__ == "__main__":
    pass
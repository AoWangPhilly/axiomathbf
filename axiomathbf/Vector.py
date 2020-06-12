from sympy.calculus.util import continuous_domain
from sympy import acos, Symbol, Interval, Intersection, diff, integrate, S, oo
from axiomathbf.Matrix import Matrix


class Vector(Matrix):
    """

    """

    def __init__(self, i=0, j=0, k=0):
        super().__init__(i, j, k)
        self.__t = Symbol('t')

    def __str__(self):
        """

        """
        v = self.matrix
        return '{}i + {}j + {}k'.format(v[0], v[1], v[2])

    def getAngle(self, other):
        """

        """
        return acos(self.matrix.dot(other) / (self.matrix.norm() * other.norm()))

    def getDirCosine(self):
        """

        """
        return [acos(unit/self.matrix.norm()) for unit in self.matrix]

    def getProjection(self, other):
        """

        """
        return (self.matrix.dot(other)/(other.norm()**2))*other

    def getVector(self):
        return self.matrix

    def setVector(self, matrix):
        self.matrix = matrix

    def getCrossArea(self, other):
        """

        """
        return self.matrix.cross(other).norm()

    def getPPVolume(self, v, w):
        """

        """
        return abs(self.matrix.dot(v.cross(w)))

    def getPlane(self, point):
        """

        """
        normVect = self.matrix
        return normVect[0] * (self.x - point.x) + normVect[1] * (self.y - point.y) +\
            normVect[2] * (self.z - point.z)

    def comparematrix(self, other):
        """


        """
        result = ""
        if self.matrix.dot(other) == 0:
            result = "Perpendicular"
        elif self.matrix.cross(other).norm() == 0:
            result = "Parallel"
        else:
            result = "Skew"
        return "{} and {}: {}".format(self.matrix, other, result)

    def getPointmatrixLine(self, point):
        """

        """
        x, y, z = point
        v1, v2, v3 = self.matrix
        return '<x,y,z> = <{},{},{}> + <{},{},{}>t'.format(x, y, z, v1, v2, v3)

    def getDomainOfVectFunc(self):
        """

        """
        domain = Interval(-oo, oo)
        domainOfFunctions = []
        t = self.__t
        for function in self.matrix:
            domainOfFunctions.append(continuous_domain(function, t, S.Reals))
            domain = Intersection(continuous_domain(
                function, t, S.Reals), domain)
        return (domain, domainOfFunctions)

    def derive(self):
        """

        """
        return Matrix([diff(function, self.__t) for function in self.matrix])

    def integrate(self):
        """

        """
        return Matrix([integrate(function, self.__t) for function in self.matrix])

    def getTangentLine(self, point, t):
        """

        """
        pass


if __name__ == "__main__":
    u = Vector(0, 2, 3)
    v = Vector(3, 4, 2)
    print(u)
    print(u.dot(v))

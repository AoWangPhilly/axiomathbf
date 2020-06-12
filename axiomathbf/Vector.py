from sympy.calculus.util import continuous_domain
from sympy import acos, Symbol, Interval, Intersection, diff, integrate, S, oo
from axiomathbf.Matrix import Matrix
from IPython.display import display, Math


class Vector(Matrix):
    """

    """

    def __init__(self, i=0, j=0, k=0):
        self.matrix = Matrix(i, j, k)
        self.__t = Symbol('t')

    def __str__(self):
        """

        """
        v = self.matrix
        return '{}i + {}j + {}k'.format(v[0], v[1], v[2])

    def _repr_pretty_(self, p, cycle):
        i, j, k = self.matrix
        return p.text(self.__str__()) if cycle else display(Math(str(i) + '\hat{i}+' + str(j) + '\hat{j}+' + str(k) + '\hat{k}'))

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
        print((self.matrix.dot(other)/(other.norm()**2)))
        print(type((self.matrix.dot(other)/(other.norm()**2))))
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
        i, j, k = [diff(function, self.__t) for function in self.matrix]
        return Vector(i, j, k)

    def integrate(self):
        """

        """
        i, j, k = [integrate(function, self.__t) for function in self.matrix]
        return Vector(i, j, k)

    def getTangentLine(self, point, t):
        """

        """
        pass


if __name__ == "__main__":
    # u = Vector(0, 2, 3)
    # v = Vector(3, 4, 2)
    # print(u)
    # print(u.getCrossArea(v))
    v = Vector(1,2)
    b = Vector(-3,4)
    print(v.getProjection(b))

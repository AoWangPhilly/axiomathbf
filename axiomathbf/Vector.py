from sympy.calculus.util import continuous_domain
from sympy import acos, Symbol, Interval, Intersection, diff, integrate, S, oo, Rational, Integer
from axiomathbf.Matrix import Matrix
from IPython.display import display, Math


class Vector(Matrix):
    """

    """

    def __init__(self, i=0, j=0, k=0):
        super().__init__(i, j, k)
        self.__t = Symbol('t')

    def __str__(self):
        """

        """
        i, j, k = self.matrix
        return '{}i + {}j + {}k'.format(i, j, k)

    def _repr_pretty_(self, p, cycle):
        i, j, k = self.matrix
        return p.text(self.__str__()) if cycle else display(Math(str(i) + '\hat{i}+' + str(j) + '\hat{j}+' + str(k) + '\hat{k}'))

    def _dunderHelper(self, other, operator):
        if isinstance(other, Vector):
            print("reached1")
            m = eval('[{0}[idx]{1}{2}[idx] for idx in range(3)]'.format(
                self.matrix, operator, other))
        if isinstance(other, (int, float, Rational, Integer)):
            m = eval('[unit{0}{1} for unit in self.matrix]'.format(
                operator, other))
        return Vector(m[0], m[1], m[2])

    def getAngle(self, other):
        """

        """
        return acos(self.dot(other) / (self.norm() * other.norm()))

    def getDirCosine(self):
        """

        """
        return [acos(unit/self.norm()) for unit in self.matrix]

    def getProjection(self, other):
        """

        """
        return other*(self.dot(other)/(other.norm()**2))

    def getVector(self):
        return self.matrix

    def setVector(self, matrix):
        self.matrix = matrix

    def getCrossArea(self, other):
        """

        """
        return self.cross(other).norm()

    def getPPVolume(self, v, w):
        """

        """
        return abs(self.dot(v.cross(w)))

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
        if self.dot(other) == 0:
            result = "Perpendicular"
        elif self.cross(other).norm() == 0:
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
    u = Vector(0, 2, 3)
    v = Vector(3, 4, 2)
    print(u)
    print(u.getCrossArea(v))
    print(u.dot(v))
    print(u.getProjection(v))

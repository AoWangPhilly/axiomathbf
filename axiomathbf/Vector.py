"""
Program: Vector.py
Purpose: The Vector module is used to solve all the vector-related problems 
in the Math 200 homework problems. 
Author: Ao Wang
Date: June 13, 2020
"""

import math
from sympy.calculus.util import continuous_domain
from sympy import *
from axiomathbf.Matrix import Matrix
from IPython.display import display, Math


class Vector(Matrix):
    """The Vector class solves vector related problems, like getting the cross area,
       parallelpiped volume, domain of Vector function, and more.

    :param i: The i component of the unit vector
    :type i: int
    :param j: The j component of the unit vector
    :type j: int
    :param k: The k component of the unit vector
    :type k: int
    """

    def __init__(self, i=0, j=0, k=0):
        super().__init__(i, j, k)
        self.__t = Symbol('t')

    def __str__(self):
        """Prints the vector using the ijk notation"""
        i, j, k = self.matrix
        return '{}i + {}j + {}k'.format(i, j, k)

    def _repr_pretty_(self, p, cycle):
        """Displays the vector using the ijk notation in Latex"""
        i, j, k = self.matrix
        return p.text(self.__str__()) if cycle else display(Math(latex(i) + '\hat{i}+' + latex(j) + '\hat{j}+' + latex(k) + '\hat{k}'))

    def _dunderHelper(self, other, operator):
        """Overrided the Matrix method to return a Vector instead"""
        if isinstance(other, Vector):
            m = eval('[{0}[idx]{1}{2}[idx] for idx in range(3)]'.format(
                self.matrix, operator, other.matrix))
        if isinstance(other, (int, float, Rational, Integer, Pow)):
            m = eval('[unit{0}{1} for unit in self.matrix]'.format(
                operator, other))
        return Vector(m[0], m[1], m[2])

    def normalize(self):
        """Normalizes the Vector"""
        normalized = [unit/self.norm() for unit in self.matrix]
        return Vector(normalized[0], normalized[1], normalized[2])

    def cross(self, other):
        """The cross product operation

        :param other: Another Matrix object
        :type other: Matrix
        :returns: The cross product
        :rtype: Matrix
        """
        i = self._det(other, 1, 2)
        j = -self._det(other, 0, 2)
        k = self._det(other, 0, 1)
        return Vector(i, j, k)

    def __neg__(self):
        m = [-unit for unit in self.matrix]
        return Vector(m[0], m[1], m[2])

    def __abs__(self):
        m = [abs(unit) for unit in self.matrix]
        return Vector(m[0], m[1], m[2])

    def __round__(self, n):
        m = [round(unit, n) for unit in self.matrix]
        return Vector(m[0], m[1], m[2])

    def __floor__(self):
        m = [math.floor(unit) for unit in self.matrix]
        return Vector(m[0], m[1], m[2])

    def __ceil__(self):
        m = [math.ceil(unit) for unit in self.matrix]
        return Vector(m[0], m[1], m[2])

    def getAngle(self, other):
        """Returns the angle between two vectors

        :param other: Another vector
        :type other: Vector
        :returns: The angle between two vectors
        :rtype: sympy.core.numbers
        """
        return acos(self.dot(other) / (self.norm() * other.norm()))

    def getDirCosine(self):
        """Returns Directional Cosine of a vector

        :returns: The directional cosine of a vector
        :rtype: sympy.core.numbers
        """
        return [acos(unit/self.norm()) for unit in self.matrix]

    def getProjection(self, other):
        """Returns the projection of the current vector onto the other.

        :param other: Another Vector
        :type other: Vector
        :returns: Vector projection
        :rtype: Vector
        """
        return other*(self.dot(other)/(other.norm()**2))

    def getVector(self):
        return self.__str__()

    def setVector(self, matrix):
        self.matrix = matrix

    def getCrossArea(self, other):
        """Returns the cross area of two vectors

        :param other: Another vector
        :type other: Vector
        :returns: The cross area
        :rtype: int
        """
        return self.cross(other).norm()

    def getPPVolume(self, v, w):
        """Returns the parallelpiped volume

        :param v: The second Vector
        :type v: Vector
        :param w: The third Vector
        :type w: Vector
        :returns: The parallelpiped volume
        :rtype: int
        """
        return abs(self.dot(v.cross(w)))

    def getPlane(self, point):
        """Returns equation of a plane due to vector and point

        :param point: The point on the plane
        :type point: sympy.geometry.point.Point3D
        :returns: The plane equation
        :rtype: sympy.core.add.Add
        """
        normVect = self.matrix
        return normVect[0] * (self.x - point.x) + normVect[1] * (self.y - point.y) +\
            normVect[2] * (self.z - point.z)

    def compare(self, other):
        """Compares two vectors, checks to see if they are perpendicular,
           parallel, or skew.

        :param other: Another vector
        :type other: Vector
        """
        result = ""
        if self.dot(other) == 0:
            result = "Perpendicular"
        elif self.cross(other).norm() == 0:
            result = "Parallel"
        else:
            result = "Skew"
        return "{} and {}: {}".format(self.getVector(), other, result)

    def getPointVectorLine(self, point):
        """Returns point vector line

        :param point: A point on the line
        :type point: sympy.geometry.point.Point3D
        :returns: The point vector line
        :rtype: str
        """
        x, y, z = point
        v1, v2, v3 = self.matrix
        try:
            x, y, z = latex(x), latex(y), latex(z)
            v1, v2, v3 = latex(v1), latex(v2), latex(v3)
            get_ipython
            display(
                Math('\\vec{\\ell(t)} = \\langle' + '{}, {}, {}'.format(x, y, z) + '\\rangle +t \\langle' + '{}, {}, {}'.format(v1, v2, v3) + '\\rangle'))
        except:
            print('<x,y,z> = <{},{},{}> + <{},{},{}>t'.format(x, y, z, v1, v2, v3))

    def getDomainOf(self):
        """Returns the intersection of the domain of the vector function and
           tuple of the domain for each function

        :returns: The intersection of the domain of the vector function and
           tuple of the domain for each function
        :rtype: tuple
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
        """Derives each of the functions in the vector function

        :returns: Derived vector function
        :rtype: Vector
        """
        i, j, k = [diff(function, self.__t) for function in self.matrix]
        return Vector(i, j, k)

    def integrate(self):
        """Integrates each of the functions in the vector function

        :returns: Integrated vector function
        :rtype: Vector
        """
        i, j, k = [integrate(function, self.__t) for function in self.matrix]
        return Vector(i, j, k)

    def getTangentLine(self, tau):
        """Return the line tangent to the Vector Function

        :param point: The point on Vector Function
        :type point: sympy.geometry.point.Point3D
        :returns: The line tangent equation
        :rtype: str
        """
        t = self.__t
        p = Point(self.matrix[0].subs(t, tau), self.matrix[1].subs(
            t, tau), self.matrix[2].subs(t, tau))

        derived = self.derive()
        v = Vector(derived[0].subs(t, tau), derived[1].subs(
            t, tau), derived[2].subs(t, tau))
        return v.getPointVectorLine(p)


if __name__ == "__main__":
    u = Vector(0, 2, 3)
    v = Vector(3, 4, 2)
    print(u)

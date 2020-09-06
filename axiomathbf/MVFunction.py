"""
Program: MVFunction.py
Purpose: I created the MVFunction module to check my work for finding the
multivarite calculus equation's gradient and other processes quickly
Author: Ao Wang
Date: June 14, 2020
"""

from sympy import *
from IPython.display import display
from .parametric_lines import ParametricLine

x, y, z = symbols("x y z")


class MVFunction():
    """The MVFunction class is used to learn more about Multivariate Functions,
       like finding the gradient, relative extremes, directional derivatives,
       linearization, and much more.

    :param function: The multivariate function
    :type function: sympy.core.add.Add
    :param point: A point on the plane
    :type point: sympy.geometry.point.Point3D
    """

    def __init__(self, function, point=Point(0, 0, 0)):
        self.function = function
        self.point = point

    def getFunction(self):
        return self.function

    def getPoint(self):
        return self.point

    def setFunction(self, function):
        self.function = function

    def setPoint(self, point):
        self.point = point

    def __str__(self):
        """Overloading the str method to print out the function and point for
           the object.

        :returns: The equation and point
        :rtype: str
        """
        return "{} at {}".format(self.function, self.point)

    def insertPoint(self):
        """Substitutes the variables with the point

        :returns: The output of the equation at given point
        :rtype: sympy.core.numbers.Integer
        """
        p1, p2, p3 = self.point
        return self.function.subs([(x, p1), (y, p2), (z, p3)])

    def getGradient(self):
        """Returns the gradient of a function. Very useful helper function.

        :returns: The gradient of a function
        :rtype: Vector
        """
        partialDiffList = []
        for var in [x, y, z]:
            partialDiff = MVFunction(
                diff(self.function, var), self.point).insertPoint()
            partialDiffList.append(partialDiff)
        return Vector(partialDiffList[0], partialDiffList[1], partialDiffList[2])

    def getDirectionalDiff(self, vector):
        """Returns the directional derivative at a point.

        :param vector: The direction
        :type vector: Vector
        :returns: The directional derivative as a point
        :rtype: sympy.core.numbers.Integer
        """
        return self.getGradient().dot(vector / vector.norm())

    def getDirectionalDiffInfo(self, increasing=True):
        """
        :param increasing: Whether the function is increasing or decreasing
        :type increasing: bool
        :returns: More information about directional derivative
        :rtype: tuple of sympy.core.numbers.Integer and Vector
        """
        gradient = self.getGradient()
        maximum = gradient.norm() if increasing else -gradient.norm()
        unitVector = gradient.normalize() if increasing else -gradient.normalize()
        return (maximum, unitVector)

    def getLinearization(self):
        """Returns the linearization equation for local-linear approximation.

        :returns: The linearization equation
        :rtype: sympy.core.add.Add
        """
        p1, p2, p3 = self.point
        gradient = self.getGradient()
        functionAtPoint = self.insertPoint()
        return functionAtPoint + gradient[0] * (x - p1) + gradient[1] * (y - p2) + \
            gradient[2] * (z - p3)

    def getTangentPlane(self):
        """Returns the tangent plane of a function at a point

        :returns: The tangent plane of a function at a point
        :rtype: sympy.core.add.Add
        """
        normalVect = self.getGradient()
        return normalVect.getPlane(self.point)

    def getNormalLine(self):
        """Returns the normal line of a function at a point

        :returns: The normal line of a function at a point
        :rtype: str
        """
        normalVect = self.getGradient()
        return normalVect.getPointVectorLine(self.point)


if __name__ == "__main__":
    x, y, z = symbols("x y z")
    func = 3*x**2-2*y**2+x*z**3

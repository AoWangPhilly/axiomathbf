"""
Program: Matrix.py
Purpose:
Author: Ao Wang
Date: June 13, 2020
"""

from sympy import *
from axiomathbf.Vector import Vector
from IPython.display import display

x, y, z = symbols("x y z")


class MVFunction():
    """The MVFunction class is used to learn more about Multivariate Functions,
       like finding the gradient, relative extremes, directional derivatives,
       linearization, and much more.

    :param function: The multivariate function
    :type function:
    :param point: A point on the plane
    :type point:
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
        :rtype:
        """
        p1, p2, p3 = self.point
        return self.function.subs([(x, p1), (y, p2), (z, p3)])

    def getGradient(self):
        """Returns the gradient of a function. Very useful helper function.

        :returns:
        :rtype:
        """
        partialDiffList = []
        for var in [x, y, z]:
            partialDiff = MVFunction(
                diff(self.function, var), self.point).insertPoint()
            partialDiffList.append(partialDiff)
        return Vector(partialDiffList[0], partialDiffList[1], partialDiffList[2])

    def getDirectionalDiff(self, vector):
        """Returns the directional derivative at a point.

        :param vector:
        :type vector:
        :returns:
        :rtype:
        """
        return self.getGradient().dot(vector / vector.norm())

    def getDirectionalDiffInfo(self, increasing=True):
        """
        :param increasing:
        :type increasing: bool
        :returns:
        :rtype: tuple of
        """
        gradient = self.getGradient()
        maximum = gradient.norm() if increasing else -gradient.norm()
        unitVector = gradient.normalize() if increasing else -gradient.normalize()
        return (maximum, unitVector)

    def getLinearization(self):
        """Returns the linearization equation for local-linear approximation.

        :returns:
        :rtype:
        """
        p1, p2, p3 = self.point
        gradient = self.getGradient()
        functionAtPoint = self.insertPoint()
        return functionAtPoint + gradient[0] * (x - p1) + gradient[1] * (y - p2) + \
            gradient[2] * (z - p3)

    def getTangentPlane(self):
        """

        :returns:
        :rtype:
        """
        normalVect = self.getGradient()
        return normalVect.getPlane(self.point)

    def getNormalLine(self):
        """

        :param point:
        :type point:
        """
        normalVect = self.getGradient()
        return normalVect.getPointVectorLine(self.point)

    def getRelativeExtreme(self):
        """

        :returns:
        :rtype:
        """
        fx, fy = diff(self.function, x), diff(self.function, y)
        x1, y1 = solve(fx), solve(fy)
        points = [[i, j] for i in x1 for j in y1]
        for point in points:
            fxx, fyy, fxy = (
                diff(fx, x).subs([(x, point[0]), (y, point[1])]),
                diff(fy, y).subs([(x, point[0]), (y, point[1])]),
                diff(fx, y).subs([(x, point[0]), (y, point[1])]),
            )
            result = fxx * fyy - fxy ** 2
            if result > 0:
                if fxx > 0:
                    print("Relative minimum: {}".format((point[0], point[1])))
                else:
                    print("Relative minimum: {}".format((point[0], point[1])))
            elif result < 0:
                print("Saddle point: {}".format((point[0], point[1])))
            else:
                print("Inconclusive: {}".format((point[0], point[1])))


if __name__ == "__main__":
    x, y, z = symbols("x y z")
    func = 3*x**2-2*y**2+x*z**3

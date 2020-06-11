"""


"""

from sympy import *
from .Vector import Vector


class MVFunction:
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
        self.x, self.y, self.z = symbols("x y z")

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
        return self.function.subs([(self.x, p1), (self.y, p2), (self.z, p3)])

    def getGradient(self):
        """Returns the gradient of a function. Very useful helper function.

        :returns:
        :rtype:
        """
        partialDiffList = []
        for var in [self.x, self.y, self.z]:
            partialDiff = MVFunction(
                diff(self.function, var), self.point).insertPoint()
            partialDiffList.append(partialDiff)
        return Matrix([partialDiffList])

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
        unitVector = gradient/gradient.norm() if increasing else - \
            (gradient/gradient.norm())
        return (maximum, unitVector)

    def getLinearization(self):
        """Returns the linearization equation for local-linear approximation.

        :returns:
        :rtype:
        """
        p1, p2, p3 = self.point
        gradient = self.getGradient()
        functionAtPoint = self.insertPoint()
        return functionAtPoint + gradient[0] * (self.x - p1) + gradient[1] * (self.y - p1) + \
            gradient[2] * (self.z - p2)

    def getTangentPlane(self, point):
        """

        :returns:
        :rtype:    
        """
        normalVect = Vector().setVector(self.getGradient())
        return normalVect.getPlane(point)

    def getNormalLine(self, point):
        """

        :param point:
        :type point:
        """
        normalVect = Vector().setVector(self.getGradient())
        return normalVect.getPointVectorLine(point)

    def getRelativeExtreme(self):
        """

        :returns:
        :rtype:
        """
        x1, y1 = 0, 0
        fx, fy = diff(self.function, x), diff(self.function, y)
        x1, y1 = solve(fx), solve(fy)
        points = [[i, j] for i in x1 for j in y1]
        for i in points:
            fxx, fyy, fxy = (
                diff(fx, x).replace(x, i[0]),
                diff(fy, y).replace(y, i[1]),
                diff(fx, y).replace(x, i[0]).replace(y, i[1]),
            )
            result = fxx * fyy - fxy ** 2
            if result > 0:
                if fxx > 0:
                    print("Relative minimum: " + str((i[0], i[1])))
                else:
                    print("Relative minimum: " + str((i[0], i[1])))
            elif result < 0:
                print("Saddle point: " + str((i[0], i[1])))
            else:
                print("Inconclusive: " + str((i[0], i[1])))


if __name__ == "__main__":
    x, y, z = symbols("x y z")
    func = 3*x**2-2*y**2+x*z**3

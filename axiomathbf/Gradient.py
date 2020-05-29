from sympy import *


class Gradient:

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
        return "{} at {}".format(self.function, self.point)

    def insertPoint(self):
        p1, p2, p3 = self.point
        return self.function.subs([(self.x, p1), (self.y, p2), (self.z, p3)])

    def getGradient(self):
        """Returns the gradient of a function. Very useful helper function.
        """
        partialDiffList = []
        for var in [self.x, self.y, self.z]:
            partialDiff = Gradient(
                diff(self.function, var), self.point).insertPoint()
            partialDiffList.append(partialDiff)
        return Matrix([partialDiffList])

    def getDirectionalDiff(self, vector):
        """Returns the directional derivative at a point.
        """
        return self.getGradient().dot(vector / vector.norm())

    def getDirectionalDiffInfo(self, increasing=True):
        gradient = self.getGradient()
        maximum = gradient.norm() if increasing else -gradient.norm()
        unitVector = gradient/gradient.norm() if increasing else - \
            (gradient/gradient.norm())
        return (maximum, unitVector)

    def getLinearization(self):
        """Returns the linearization equation for local-linear approximation.
        """
        p1, p2, p3 = self.point
        gradient = self.getGradient()
        functionAtPoint = self.insertPoint()
        return functionAtPoint + gradient[0] * (self.x - p1) + gradient[1] * (self.y - p1) + \
            gradient[2] * (self.z - p2)

    def getTangentPlane(self):
        pass

    def getNormalLine(self):
        pass


if __name__ == "__main__":
    x, y, z = symbols("x y z")
    func = 3*x**2-2*y**2+x*z**3

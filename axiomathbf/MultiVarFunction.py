from sympy import *


class MultiVarFunction:
    variables = symbols("x y z")

    def __init__(self, function, point=Point(0, 0, 0)):
        self.function = function
        self.point = point

    def getFunction(self):
        return self.function

    def setFunction(self, function):
        self.function = function

    def getPoint(self):
        return self.point

    def setPoint(self, point):
        self.point = point

    def __str__(self):
        return "{} at {}".format(self.function, self.point)

    def insertPoint(self):
        p1, p2, p3 = self.point
        x, y, z = MultiVarFunction.variables
        return self.function.subs([(x, p1), (y, p2), (z, p3)])

    def getGradient(self):
        """Returns the gradient of a function. Very useful helper function.
        """
        partialDiffList = []
        for var in MultiVarFunction.variables:
            partialDiff = MultiVarFunction(diff(self.function, var), self.point).insertPoint()
            partialDiffList.append(partialDiff)
        return Matrix([partialDiffList])

    def getDirectionalDiff(self, vector):
        """Returns the directional derivative at a point.
        """
        return self.getGradient().dot(vector / vector.norm())

    def getLinearization(self):
        """Returns the linearization equation for local-linear approximation.
        """
        x, y, z = MultiVarFunction.variables
        p1, p2, p3 = self.point
        gradient = self.getGradient()
        functionAtPoint = self.insertPoint()
        return functionAtPoint + gradient[0] * (x - p1) + gradient[1] * (y - p1) + gradient[2] * (z - p2)

    def getTangentPlane(self):
        pass

    def getNormalLine(self):
        pass

if __name__ == "__main__":
    x, y, z = symbols("x y z")
    func = 3*x**2-2*y**2+x*z**3
    p = Point(-1,2,1)
    vectorFunc = MultiVarFunction(func, p)
    print(vectorFunc.getLinearization())

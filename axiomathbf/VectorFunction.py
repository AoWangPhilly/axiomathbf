from sympy import *
from sympy.vector import CoordSys3D


class VectorFunction:
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
        x, y, z = VectorFunction.variables
        return self.function.replace(x, p1).replace(y, p2).replace(z, p3)

    def getGradient(self):
        """Returns the gradient of a function. Very useful helper function.
        """
        partialDiffList = []
        for var in VectorFunction.variables:
            partialDiffList.append(VectorFunction(
                diff(self.function, var), self.point).insertPoint())
        return Matrix(partialDiffList)

    def getDirectionalDiff(self, vector):
        """Returns the directional derivative at a point.

        Example
        =======
        >>> from axiomathbf.multivariate_calculus import *
        >>> directional_derivative(exp(x)*cos(y*z),Point(1,pi,0),make_vector(-2,1,-3))
        -sqrt(14)*E/7

        :param f (sympy.core.add.Add): A function.
        :param p (sympy.geometry.point.Point3D): A point.
        :param v (sympy.matrices.dense.MutableDenseMatrix): A vector.
        :return ympy.core.mul.Mul: The directional derivative.
        """
        return self.getGradient().dot(vector / vector.norm())


if __name__ == "__main__":
    x, y, z = symbols("x y z")
    vector = VectorFunction(4*x*y*z-y**2*z**3+4*z**3*y, Point(2, 3, 1))
    print(vector.find_gradient())

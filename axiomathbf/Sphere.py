from sympy import Point, Eq, simplify, factor, sqrt, symbols


class Sphere():
    """


    """
    def __init__(self, center=Point(0, 0, 0), radius=1, eq=None):
        self.center = center
        self.radius = radius
        self.eq = eq
        self.__x, self.__y, self.__z = symbols("x y z")

    def __str__(self):
        """

        """
        return str(self.getEquation())

    def __eq__(self, other):
        """

        """
        return Eq(self.getEquation(), other.getEquation())

    def __nq__(self, other):
        """

        """
        return not self.__eq__(other)

    def __completeTheSquare(self, n):
        """

        """
        return (n/2)**2

    def __formatEquation(self):
        """

        """
        self.eq = simplify(factor(self.eq))
        eq = self.eq.as_coefficients_dict()
        center = []

        for squaredVar in [self.__x**2, self.__y**2, self.__z**2]:
            coeff = eq[squaredVar]
            if coeff == 0:
                continue
            if coeff != 1:
                break

        if coeff != 0:
            for key in eq:
                eq[key] /= coeff

        radiusSquared = eq[1]
        for var in [self.__x, self.__y, self.__z]:
            radiusSquared -= self.__completeTheSquare(eq[var])
            center.append(-eq[var]/2)

        center = Point(center)
        return ((self.__x-center.x)**2 + (self.__y-center.y)**2 +
                (self.__z-center.z)**2 + radiusSquared, center, sqrt(abs(radiusSquared)))

    def isPointInSphere(self, point):
        """

        """
        c1, c2, c3 = self.getCenter()
        checkZero = self.getEquation().subs(
            [(self.__x, c1), (self.__y, c2), (self.__z, c3)])
        return checkZero == 0

    def getEquation(self):
        """

        """
        if self.eq:
            return self.__formatEquation()[0]
        return (self.__x-self.center.x)**2 + (self.__y-self.center.y)**2 + \
            (self.__z-self.center.z)**2 - self.radius**2

    def getCenter(self):
        return self.__formatEquation()[1] if self.eq else self.center

    def getRadius(self):
        return self.__formatEquation()[2] if self.eq else self.radius

    def setCenter(self, center):
        self.center = center

    def setRadius(self, radius):
        self.radius = radius

    def setEquation(self, eq):
        self.eq = eq


if __name__ == "__main__":
    x, y, z = symbols("x y z")
    sphere1 = Sphere(eq=4*x**2 + 4*y**2 - 16*x - 24*y + 51)
    sphere2 = Sphere(eq=(x - 2)**2 + (y - 3)**2 - 1/4)
    print(sphere1)
    print(sphere2)

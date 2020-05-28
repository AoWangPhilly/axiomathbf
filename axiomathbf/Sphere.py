from sympy import *


class Sphere():
    def __init__(self, center=Point(0, 0, 0), radius=1, eq=None):
        self.center = center
        self.radius = radius
        self.eq = eq
        self.__x, self.__y, self.__z = symbols("x y z")

    def __str__(self):
        return str(self.getEquation())

    def __completeTheSquare(self, n):
        return (n/2)**2

    def __formatEquation(self):
        eq = self.eq.as_coefficients_dict()
        radiusSquared = eq[1]
        center = []

        for squaredVar in [self.__x**2, self.__y**2, self.__z**2]:
            coeff = eq[squaredVar]
            if coeff != 1:
                break

        for key in eq:
            eq[key] /= coeff

        for var in [self.__x, self.__y, self.__z]:
            radiusSquared -= self.__completeTheSquare(eq[var])
            center.append(sqrt(eq[var]))

        return ((self.__x-center.x)**2 + (self.__y-center.y)**2 +
                (self.__z-center.z)**2 + radiusSquared, Point(center), sqrt(abs(radiusSquared)))

    def isPointInSphere(self, point):
        c1, c2, c3 = self.getCenter()
        checkZero = self.getEquation().subs(
            [(self.__x, c1), (self.__y, c2), (self.__z, c3)])
        return checkZero == 0

    def getEquation(self):
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
    sph = Sphere(eq=100*x**2+100*y**2-100*x+240*y-56)
    print(sph)
    # print(sph.getCenter())
    # print(sph.getRadius())

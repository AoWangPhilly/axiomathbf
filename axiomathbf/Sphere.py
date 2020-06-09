"""
Program: Sphere.py
Purpose: A module used to create or clean Sphere equation
Author: Ao Wang
Date: June 08, 2020
"""

from sympy import Point, Eq, simplify, factor, sqrt, symbols
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import time


class Sphere():
    """The Sphere class is used to create a sphere either from inputting a center or radius,
       or equation. If inputting an equation, it will be formatted bycenter-radius form. 

    :param center: The center of the sphere
    :type center: sympy.geometry.point.Point3D
    :param radius: The radius of the sphere
    :type radius: int
    :param eq: The equation of the sphere
    :type eq: sympy.core.add.Add
    """

    def __init__(self, center=Point(0, 0, 0), radius=1, eq=None):
        self.center = center
        self.radius = radius
        self.eq = eq
        self.__x, self.__y, self.__z = symbols("x y z")

    def __str__(self):
        """Overloads the str method and prints out the equation of the circle. 

        :returns: The sphere equation
        :rtype: str
        """
        return str(self.getEquation())

    def __eq__(self, other):
        """Overloads the eq method and checks if two spheres are equal

        :returns: Whether the spheres are equal
        :rtype: bool
        """
        return Eq(self.getEquation(), other.getEquation())

    def __nq__(self, other):
        """Overloads the eq method and checks if two spheres are not equal

        :returns: Whether the spheres are not equal
        :rtype: bool
        """
        return not self.__eq__(other)

    def __formatEquation(self):
        """Formats the equation to center-radius form

        :returns: The clean center-radius equation
        :type eq: sympy.core.add.Add
        """
        self.eq = factor(self.eq)
        equationDict = self.eq.as_coefficients_dict()
        secondOrder = []
        for var in [x**2, y**2, z**2]:
            if equationDict[var] != 0:
                secondOrder.append(equationDict[var])

        for idx in range(len(secondOrder)-1):
            if secondOrder[idx] != secondOrder[idx+1]:
                raise Exception("Nonsymmetrical, not a sphere!")
        else:
            for key in equationDict:
                equationDict[key] /= secondOrder[0]

        center = Point([equationDict[var]/-2 for var in [x, y, z]])
        radiusSquared = center.x**2 + center.y**2 + \
            center.z**2 - equationDict[1]

        if radiusSquared < 0:
            raise Exception("Radius is negative, not a sphere!")

        return ((self.__x-center.x)**2 + (self.__y-center.y)**2 +
                (self.__z-center.z)**2 + radiusSquared, center, sqrt(abs(radiusSquared)))

    def isPointInSphere(self, point):
        """Checkers whether the point is in the sphere

        :param point: A random point
        :type point: sympy.geometry.point.Point3D
        :returns: Whether the point is in the sphere
        :rtype: bool
        """
        c1, c2, c3 = self.getCenter()
        checkZero = self.getEquation().subs(
            [(self.__x, c1), (self.__y, c2), (self.__z, c3)])
        return checkZero == 0

    def draw(self):
        pass

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
    eq = x**2+z**2-4*x-8*z+13
    start = time.time()
    print(Sphere(eq=eq))

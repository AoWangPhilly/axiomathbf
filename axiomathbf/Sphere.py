"""
Program: Sphere.py
Purpose: A module used to create or clean Sphere equation
Author: Ao Wang
Date: June 08, 2020
"""

from sympy import Point, Eq, simplify, factor, sqrt, symbols
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

x, y, z = symbols("x y z")


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
        self.eq = simplify(factor(self.eq))
        equationDict = self.eq.as_coefficients_dict()
        secondOrder = [equationDict[var] for var in [
            x**2, y**2, z**2] if equationDict[var] != 0]

        for idx in range(len(secondOrder)-1):
            if secondOrder[idx] != secondOrder[idx+1]:
                raise Exception("Not symmetrical, not a sphere!")
        else:
            for key in equationDict:
                equationDict[key] /= secondOrder[0]

        center = Point(
            [equationDict[var]/-2 for var in [x, y, z]])
        radiusSquared = center.x**2 + center.y**2 + \
            center.z**2 - equationDict[1]

        if radiusSquared <= 0:
            raise Exception("Radius is non-positive, not a sphere!")

        return ((x-center.x)**2 + (y-center.y)**2 +
                (z-center.z)**2 + radiusSquared, center, sqrt(abs(radiusSquared)))

    def isPointInSphere(self, point):
        """Checkers whether the point is in the sphere

        :param point: A random point
        :type point: sympy.geometry.point.Point3D
        :returns: Whether the point is in the sphere
        :rtype: bool
        """
        c1, c2, c3 = self.getCenter()
        checkZero = self.getEquation().subs(
            [(x, c1), (y, c2), (z, c3)])
        return checkZero == 0

    def draw(self):
        """Draws the sphere with the appropriate center and radius

        Credit to: https://matplotlib.org/mpl_toolkits/mplot3d/tutorial.html
        """
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        r = float(self.getRadius())
        c = self.getCenter()

        # Make data
        u = np.linspace(0, 2 * np.pi, 100)
        v = np.linspace(0, np.pi, 100)
        x = r * np.outer(np.cos(u), np.sin(v)) + float(c.x)
        y = r * np.outer(np.sin(u), np.sin(v)) + float(c.y)
        z = r * np.outer(np.ones(np.size(u)), np.cos(v)) + float(c.z)

        # Plot the surface
        ax.plot_surface(x, y, z)

        plt.show()

    def getEquation(self):
        if self.eq:
            return self.__formatEquation()[0]
        return (x-self.center.x)**2 + (y-self.center.y)**2 + \
            (z-self.center.z)**2 - self.radius**2

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
    eq = 2*x**2+2*y**2+6*x-8*y+12
    sp = Sphere(eq=eq)
    print(sp)
    sp.draw()

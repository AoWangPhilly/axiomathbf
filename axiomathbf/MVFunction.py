"""
Program: MVFunction.py
Purpose: I created the MVFunction module to check my work for finding the
multivarite calculus equation's gradient and other processes quickly
Author: Ao Wang
Date: June 14, 2020
"""

from .parametric_lines import ParametricLine
from .plane import Plane
import sympy
from sympy import sqrt, sin, E, cos, pi
from sympy.abc import x, y, z
from sympy.vector import CoordSys3D, matrix_to_vector
from environment import isnotebook
from IPython.display import display, Math


class Gradient():
    '''Gradient class that gives the gradient vector, latex display, and gradient at a point

    Attributes
    ==========
        function (sympy.core.add.Add): the function for gradient
        vector (list): the gradient vector
        latex (str): the latex code for gradient vector
    '''

    def __init__(self, function):
        self.function = function
        self.vector = self.__get_gradient()
        self.latex = self.__get_latex

    def __repr__(self):
        if isnotebook():
            display(Math(self.__get_latex().replace('\\', '\\\\')))
            return ''
        return self.__str__

    def __str__(self):
        v1, v2, v3 = self.vector
        return '<{}, {}, {}>'.format(v1, v2, v3)

    def get_function(self):
        return self.function

    def set_function(self, function):
        self.function = function

    def __get_gradient(self):
        '''Helper function to get gradient vector

        Return
        ======
            list: the differientiation of x, y, z for the function
        '''
        return list(sympy.derive_by_array(self.function, (x, y, z)))

    def __get_latex(self):
        '''Returns the latex code for gradient vector

        Return
        ======
            str: the latex code for gradient vector
        '''
        v1, v2, v3 = self.vector
        return sympy.latex('$\\langle{}, {}, {}\\rangle$'.format(v1, v2, v3))

    def at(self, point):
        '''Returns the vector gradient at a certain point

        Parameters
        ==========
            point (list): a 3D point

        Return
        ======
            sympy.Matrix: gradient at a certain point
        '''
        p1, p2, p3 = point
        return sympy.Matrix([elem.subs(([x, p1], [y, p2], [z, p3]))
                             for elem in self.vector])


class DirectionalDerivative(Gradient):
    '''Directional Deriviative class

    Attributes
    ==========
        function:
        unit_vector:
        point:
        value:
        increasing:
        info:

    '''

    def __init__(self, function, point, unit_vector=None):
        super().__init__(function)
        self.point = point
        if unit_vector != None:
            unit_vector = sympy.Matrix(unit_vector)
            self.unit_vector = unit_vector/unit_vector.norm()
            self.value = self.__get_directional_diff()

    def __repr__(self):
        return self.__str__

    def __str__(self):
        return 'Function: {}\nPoint: {}\n'.format(self.function, self.point)

    def get_unit_vector(self):
        return self.unit_vector

    def set_unit_vector(self, unit_vector):
        self.unit_vector = unit_vector

    def get_point(self):
        return self.point

    def set_point(self, point):
        self.point = point

    def __get_directional_diff(self):
        """Returns the directional derivative at a point.

        :param vector: The direction
        :type vector: Vector
        :returns: The directional derivative as a point
        :rtype: sympy.core.numbers.Integer
        """
        return self.at(self.point).dot(self.unit_vector)

    def info(self, increasing=True):
        """
        :param increasing: Whether the function is increasing or decreasing
        :type increasing: bool
        :returns: More information about directional derivative
        :rtype: tuple of sympy.core.numbers.Integer and Vector
        """
        gradient = self.at(self.point)
        maximum = gradient.norm() if increasing else -gradient.norm()
        gradient /= gradient.norm()
        unitVector = gradient if increasing else -gradient
        return (maximum, list(unitVector))


class MVFunction(Gradient):
    def __init__(self, function, point):
        super().__init__(function)
        self.point = point
        p1, p2, p3 = self.point
        self.value = self.function.subs(([x, p1], [y, p2], [z, p3]))

    def __repr__(self):
        return self.__str__

    def __str__(self):
        return '{} at {} is {}'.format(self.function, self.point, self.value)

    def get_point(self):
        return self.point

    def set_point(self, point):
        self.point = point

    def get_value(self):
        return self.value

    def get_linearization(self):
        """Returns the linearization equation for local-linear approximation.

        :returns: The linearization equation
        :rtype: sympy.core.add.Add
        """
        p1, p2, p3 = self.point
        g1, g2, g3 = self.at(self.point)
        function_at_point = self.value
        return function_at_point + g1 * (x - p1) + g2 * (y - p2) + g3 * (z - p3)

    def get_tangent_plane(self):
        """Returns the tangent plane of a function at a point

        :returns: The tangent plane of a function at a point
        :rtype: sympy.core.add.Add
        """
        return Plane(p1=self.point, normal_vector=self.at(self.point))

    def get_normal_line(self):
        """Returns the normal line of a function at a point

        :returns: The normal line of a function at a point
        :rtype: str
        """
        return ParametricLine(point=self.point, vector=self.at(self.point))


if __name__ == "__main__":
    # f1, p1, v1 = x**4-y**4, [0, -2, 0], [sqrt(2)/2, sqrt(2)/2, 0]
    # f2, p2, v2 = y*sin(x), [pi/2, 1, 0], [1, -1, 0]
    # f3, p3, v3 = E**x*cos(y*z), [1, pi, 0], [-2, 1, -3]
    # dd1 = DirectionalDerivative(function=f1, point=p1, unit_vector=v1)
    # dd2 = DirectionalDerivative(function=f2, point=p2, unit_vector=v2)
    # dd3 = DirectionalDerivative(function=f3, point=p3, unit_vector=v3)

    # f4, p4 = 3*x*y-y**2*x**3, [1, -1, 0]
    # f5, p5 = cos(2*x-y**2), [pi/4, 0, 0]
    # f6, p6 = 4*x*y*z-y**2*z**3+4*z**3*y, [2, 3, 1]

    # g1, g2, g3 = Gradient(f4), Gradient(f5), Gradient(f6)

    # f7, p7 = E**(x*y**2), [1, 3, 0]
    # f8, p8 = sqrt(4-x**2-y**2-z**2), [1, -1, 0]

    # print(dd1)
    # print(dd2)
    # print(dd3)

    # print(g1.at(p4))
    # print(g2.at(p5))
    # print(g3.at(p6))

    # dd4, dd5 = DirectionalDerivative(f7, p7), DirectionalDerivative(f8, p8)
    # print(dd4.info())
    # print(dd5.info())

    s1, p1 = sympy.ln(x+y+z) - 2, [-1, E**2, 1]
    s2, p2 = x**2-y**2, [1, 2, 0]

    mv1 = MVFunction(s1, p1)
    mv2 = MVFunction(s2, p2)
    print(mv1.get_tangent_plane())
    print(mv1.get_normal_line())

    print(mv2.get_linearization())

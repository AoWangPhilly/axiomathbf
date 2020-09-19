'''
description: MVFunction.py
author: Ao Wang
date: 09/17/20
'''

from IPython.display import Math, display
from sympy.abc import x, y, z

from axiomathbf.environment import isnotebook

from .gradient import Gradient
from .parametric_lines import ParametricLine
from .plane import Plane


class MVFunction(Gradient):
    def __init__(self, function, point):
        '''MVFunction class that gets tangent plane, normal line, and linearization of a function

        :param function: the multivariable function
        :type function: sympy.core.add.Add
        :param point: a point
        :type point: list of int
        :param value: value of function at a point
        :type value: int
        '''
        super().__init__(function)
        self.point = point
        p1, p2, p3 = self.point
        self.value = self.function.subs(([x, p1], [y, p2], [z, p3]))

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return '{} at {} is {}'.format(self.function, self.point, self.value)

    def get_point(self):
        '''Gets the point class attribute

        :return: the point class attribute
        :rtype: list of ints
        '''
        return self.point

    def set_point(self, point):
        '''Sets the point class attribute

        :param point: the point class attribute
        :type point: list of ints
        '''
        self.point = point

    def get_value(self):
        '''Gets the value class attribute

        :return: the value class attribute
        :rtype: int
        '''
        return self.value

    def get_linearization(self):
        '''Calculates the linearization equation for local-linear approximation.

        :return: the linearization equation 
        :rtype: sympy.core.add.Add
        '''
        p1, p2, p3 = self.point
        g1, g2, g3 = self.at(self.point)
        function_at_point = self.value
        return function_at_point + g1 * (x - p1) + g2 * (y - p2) + g3 * (z - p3)

    def get_tangent_plane(self):
        '''Calculates the tangent plane of a function at a point

        :return: the tangent plane at a point at a function
        :rtype: axiomathbf.plane.Plane
        '''
        return Plane(p1=self.point, normal_vector=self.at(self.point))

    def get_normal_line(self):
        '''Calculates the normal line of a function at a point

        :return: the normal line of a function
        :rtype: axiomathbf.parametric_line.ParametricLine
        '''
        return ParametricLine(point=self.point, vector=self.at(self.point))

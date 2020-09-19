'''
description: directional_derivative.py
author: Ao Wang
date: 09/18/20
'''

from IPython.display import Math, display
from sympy import Matrix

from axiomathbf.environment import isnotebook

from .gradient import Gradient


class DirectionalDerivative(Gradient):
    '''The Directional Deriviative class calculates the its value, provide more info,
    like its maximum/minimum value and in which direction it increases most rapidly.

    :param function: the multivariable function
    :type function: sympy.core.add.Add
    :param point: the point at a function 
    :type point: list of int
    :param unit_vector: the directional vector
    :type unit_vector: list of int
    '''

    def __init__(self, function, point, unit_vector=None):
        super().__init__(function)
        self.point = point
        if unit_vector != None:
            unit_vector = Matrix(unit_vector)
            self.unit_vector = unit_vector/unit_vector.norm()
            self.value = self.__get_directional_diff()

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return 'Function: {}\nPoint: {}\n'.format(self.function, self.point)

    def get_unit_vector(self):
        '''Gets the unit vector class attribute

        :return: the unit vector class attribute
        :rtype: the list of ints
        '''
        return self.unit_vector

    def set_unit_vector(self, unit_vector):
        '''Sets the unit vector class attribute

        :param unit_vector: the unit vector class attribute
        :type unit_vector: the list of ints
        '''
        self.unit_vector = unit_vector

    def get_point(self):
        '''Gets the point class attribute

        :return: the point class attribute
        :rtype: the list of ints
        '''
        return self.point

    def set_point(self, point):
        '''Sets the point class attribute

        :param point: the point class attribute
        :type point: the list of ints
        '''
        self.point = point

    def __get_directional_diff(self):
        '''Calculates the directional derivative at a point.

        :return: the directional derivative at a point
        :rtype: sympy.core.numbers.Integer
        '''
        return self.at(self.point).dot(self.unit_vector)

    def info(self, increasing=True):
        '''Provides more info about the directional derivative 

        :param increasing: whether the function is increasing or decreasing
        :type increasing: bool
        :return: the maximum value of directional derivative and direction vector
        :rtype: tuple of int and list
        '''
        gradient = self.at(self.point)
        maximum = gradient.norm() if increasing else -gradient.norm()
        gradient /= gradient.norm()
        unitVector = gradient if increasing else -gradient
        return (maximum, list(unitVector))

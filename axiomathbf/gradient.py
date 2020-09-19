'''
description: gradient.py
author: Ao Wang
date: 09/18/20
'''

from IPython.display import Math, display
from sympy import Matrix, derive_by_array, latex
from sympy.abc import x, y, z

from axiomathbf.environment import isnotebook


class Gradient():
    '''The Gradient class calculates the gradient vector and the gradient at a point

    :param function: the function for gradient
    :type function: sympy.core.add.Add
    :param vector: the gradient vector
    :type vector: list of int
    :param latex: the latex code for gradient vector
    :type latex: str
    '''

    def __init__(self, function):
        self.function = function
        self.vector = self.__get_gradient()
        self.latex = self.__get_latex

    def __repr__(self):
        if isnotebook():
            display(Math(self.__get_latex()))
            return ''
        return self.__str__()

    def __str__(self):
        v1, v2, v3 = self.vector
        return '<{}, {}, {}>'.format(v1, v2, v3)

    def get_function(self):
        '''Gets the function class attribute

        :return: the function class attribute
        :rtype: sympy.core.add.Add
        '''
        return self.function

    def set_function(self, function):
        '''Sets the function class attribute

        :param function: the function class attribute
        :type function: sympy.geometry.plane.Plane
        '''
        self.function = function

    def __get_gradient(self):
        '''Helper function to get gradient vector

        :return: the differientiation of x, y, z for the function
        :rtype: list of numbers
        '''
        return list(derive_by_array(self.function, (x, y, z)))

    def __get_latex(self):
        '''Formats the latex code for gradient vector

        :return: the latex code for gradient vector
        :rtype: str
        '''
        v1, v2, v3 = self.vector
        return latex('$\\langle{}, {}, {}\\rangle$'.format(v1, v2, v3))

    def at(self, point):
        '''Returns the gradient vector at a certain point

        :param point: a 3D point
        :type point: list of ints
        :return: a gradient at a certain point
        :rtype: sympy.matrices.dense.MutableDenseMatrix
        '''
        p1, p2, p3 = point
        return Matrix([elem.subs(([x, p1], [y, p2], [z, p3]))
                       for elem in self.vector])

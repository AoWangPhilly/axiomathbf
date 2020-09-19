'''
description: vector-value function class
author: ao wang
date: 09/01/2020
'''
from IPython.display import Math, display
from sympy import (E, Intersection, Interval, S, Symbol, cos, diff, integrate,
                   latex, ln, oo, sin, solve, sqrt)
from sympy.abc import t
from sympy.calculus.util import continuous_domain
from sympy.matrices import Matrix
from sympy.vector import CoordSys3D, matrix_to_vector

from axiomathbf.environment import isnotebook

from .parametric_lines import ParametricLine


class VectorFunction():
    '''Vector-Value Function that derives, integrates, and finds the domain of the vector

    :param lst: private list of vectors
    :type lst: lst of ints
    :param vector: matrix object of the vectors
    :type vector: sympy.matrices.dense.MutableDenseMatrix
    '''

    def __init__(self, lst):
        self.__lst = lst
        self.vector = Matrix(lst)

    def __repr__(self):
        if isnotebook():
            display(Math(latex(self.get_vector())))
            return ''
        return self.__str__()

    def __str__(self):
        '''Prints out list'''
        return str(self.__lst).replace('[', '<').replace(']', '>')

    def __eq__(self, other):
        return self.__lst == other.__lst

    def get_vector(self):
        '''Converts Matrix vector into a vector object

        :return: the Vector-Value Function
        :rtype: sympy.vector.vector.VectorAdd
        '''
        C = CoordSys3D('')
        return matrix_to_vector(self.vector, C)

    def derive(self):
        '''Derives each of the functions in the vector function

        :return: the differientation of the Vector-Value Function
        :rtype: axiomathbf.vector_value.VectorFunction
        '''
        return VectorFunction([diff(elem, t) for elem in self.__lst])

    def integrate(self):
        '''Integrates each of the functions in the vector function

        :return: the integrated version of the Vector-Value Function
        :rtype: sympy.vector.vector.VectorAdd
        '''
        return VectorFunction([integrate(elem, t) for elem in self.__lst])

    def get_domain(self):
        '''Returns domain of vector-value function

        :return: the domain of the vector-value function
        :rtype: sympy.sets.sets.Union
        '''

        # Starts domain in all reals
        domain = Interval(-oo, oo)

        # Intersection for each function's domain
        for vector in self.__lst:
            if type(vector) != int:
                domain = Intersection(continuous_domain(
                    vector, t, S.Reals), domain)
        return domain

    def plugin(self, pt):
        '''Returns Vector-Value Function given a point

        :param pt: a point at t
        :type pt: int
        :return: the vector-value function at point t
        :rtype: list of ints
        '''
        return [elem.subs(t, pt) if type(elem) != int else elem for elem in self.__lst]

    def get_tangent_line(self, tau=None, point=None):
        '''Gets the parametric equation of the tan¸gent line to the original function

        :param tau: the time at t
        :type tau: int
        :param point: the point at t
        :type point: list of ints
        :return: the parametic tangent line at t
        :rtype: axiomathbf.vector_value.VectorFunction
        '''
        if tau != None:
            point, vector = self.plugin(tau), self.derive().plugin(tau)
        elif point != None:
            # solves for t with first function
            tau = solve(self.__lst[0], t)[0]
            vector = self.derive().plugin(tau)
        return ParametricLine(point, vector)

    def solve_integration(self, initial, point):
        '''Solve for position function, given a velocity function, point, and start position

        :param point: the point at t
        :type point: list of ints
        :param initial: the initial vector-value position
        :type initial: list of ints
        :return: the position vector-value function
        :rtype: axiomathbf.vector_value.VectorFunction
        '''
        pos = self.integrate()
        plugged = [elem.subs(t, point) for elem in pos.__lst]
        c_lst = [i - p for i, p in zip(initial, plugged)]  # solve for the c's
        return VectorFunction([i+c for i, c in zip(pos.__lst, c_lst)])

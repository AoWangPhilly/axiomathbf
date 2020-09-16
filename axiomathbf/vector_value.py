'''
description: vector-value function class
author: ao wang
date: 09/01/2020
'''
from sympy.calculus.util import continuous_domain
from sympy.matrices import Matrix
from sympy.vector import CoordSys3D, matrix_to_vector
from sympy import E, ln, sqrt, sin, cos, solve
from sympy import latex, diff, integrate, Interval, oo, Intersection, S, Symbol
from sympy.abc import t
from IPython.display import display, Math
from .parametric_lines import ParametricLine
from axiomathbf.environment import isnotebook


class VectorFunction():
    '''Vector-Value Function that derives, integrates, and finds the domain of the vector

    Attributes
    ==========
        lst (list): private variable of vectors
        vector (Matrix): matrix object of the vectors
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
        '''Converts Matrix vector into a vector object'''
        C = CoordSys3D('')
        return matrix_to_vector(self.vector, C)

    def derive(self):
        '''Derives each of the functions in the vector function'''
        return VectorFunction([diff(elem, t) for elem in self.__lst])

    def integrate(self):
        '''Integrates each of the functions in the vector function'''
        return VectorFunction([integrate(elem, t) for elem in self.__lst])

    def get_domain(self):
        '''Returns domain of vector-value function

        Return:
            Union: the domain of the vector-value function
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

        Parameter
        ========
            pt (int): a point at t

        Return
        ======
            VectorFunction: the vector-value function at point t
        '''
        return [elem.subs(t, pt) if type(elem) != int else elem for elem in self.__lst]

    def get_tangent_line(self, tau=None, point=None):
        '''Gets the parametric equation of the tan¸gent line to the original function

        Parameter
        =========
            tau (int): the time at t
            point (list of numbers): the point at t

        Return
        ======
            ParametricLine: the parametic tangent line at t
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

        Parameters
        ==========
            point (list of numbers): the point at t
            initial (list): the initial vector-value position

        Return
        ======
            VectorFunction: the position vector-value function
        '''
        pos = self.integrate()
        plugged = [elem.subs(t, point) for elem in pos.__lst]
        c_lst = [i - p for i, p in zip(initial, plugged)]  # solve for the c's
        return VectorFunction([i+c for i, c in zip(pos.__lst, c_lst)])


if __name__ == '__main__':
    t = Symbol('t')
    v1 = VectorFunction([t**2, sqrt(1-t), -1/t])
    v2 = VectorFunction([ln(t+1), 1/(E**t-2), t])
    v3 = VectorFunction([cos(t), sin(t), 5])
    v4 = VectorFunction([ln(t), t+1, E**t])
    v5 = VectorFunction([sin(t), ln(abs(t)), sqrt(t)])
    for v in (v1, v2, v3, v4, v5):
        print(v.get_domain())

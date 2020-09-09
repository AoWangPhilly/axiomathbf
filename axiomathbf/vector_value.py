'''
description: vector-value function class
author: ao wang
date: 09/01/2020
'''
from sympy.calculus.util import continuous_domain
from sympy.matrices import Matrix
from sympy.vector import CoordSys3D, matrix_to_vector
import sympy
from sympy import E, ln, sqrt, sin, cos
from sympy.abc import t
from .parametric_lines import ParametricLine


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

    def __str__(self):
        '''Prints out list'''
        return str(self.__lst)
    
    def __eq__(self, other):
        return self.__lst == other.__lst

    def get_vector(self):
        '''Converts Matrix vector into a vector object'''
        C = CoordSys3D('')
        return matrix_to_vector(self.vector, C)

    def derive(self):
        '''Derives each of the functions in the vector function'''
        return VectorFunction([sympy.diff(elem, t) for elem in self.__lst])

    def integrate(self):
        '''Integrates each of the functions in the vector function'''
        return VectorFunction([sympy.integrate(elem, t) for elem in self.__lst])

    def get_domain(self):
        '''Returns domain of vector-value function
        
        Return:
            Union: the domain of the vector-value function
        '''

        # Starts domain in all reals
        domain = sympy.Interval(-sympy.oo, sympy.oo)

        # Intersection for each function's domain
        for vector in self.__lst:
            if type(vector) != int:
                domain = sympy.Intersection(continuous_domain(
                    vector, t, sympy.S.Reals), domain)
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
        return [elem.subs(t, pt) for elem in self.__lst]

    # TODO add tau=None, point=None
    def get_tangent_line(self, tau=None, point=None):
        '''Gets the parametric equation of the tangent line to the original function
        
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
            derived = self.derive().__lst
            vector = [elem.subs(t, p) for elem, p in zip(derived, point)]
        return ParametricLine(point, vector)

    # TODO add tau=None, point=None
    def solve_integration(self, initial, tau=None, point=None):
        '''Solve for position function, given a velocity function, point, and start position

        Parameters
        ==========
            tau (int): the time at t
            point (list of numbers): the point at t
            initial (list): the initial vector-value position
        
        Return
        ======
            VectorFunction: the position vector-value function
        '''
        pos = self.integrate()
        if tau != None: plugged = pos.plugin(tau)
        elif point != None: plugged = [elem.subs(t, p) for elem, p in zip(pos.__lst, point)]
        c = initial[0] - plugged[0]
        return VectorFunction([i+c for i in pos.__lst])

if __name__ == '__main__':
    t = sympy.Symbol('t')
    v1 = VectorFunction([t**2, sqrt(1-t), -1/t])
    v2 = VectorFunction([ln(t+1), 1/(E**t-2), t])
    v3 = VectorFunction([cos(t), sin(t), 5])
    v4 = VectorFunction([ln(t), t+1, E**t])
    v5 = VectorFunction([sin(t), ln(abs(t)), sqrt(t)])
    for v in (v1, v2, v3, v4, v5):
        print(v.get_domain())
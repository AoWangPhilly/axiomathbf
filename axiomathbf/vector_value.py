'''
description: vector-value function class
author: ao wang
date: 09/01/2020
'''
from sympy.calculus.util import continuous_domain
from sympy.matrices import Matrix
from sympy.vector import CoordSys3D, matrix_to_vector
import sympy
from parametric_lines import ParametricLine


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

    def getVector(self):
        '''Converts Matrix vector into a vector object'''
        C = CoordSys3D('')
        return matrix_to_vector(self.vector, C)

    def derive(self):
        '''Derives each of the functions in the vector function'''
        return VectorFunction(list(map(sympy.diff, self.__lst)))

    def integrate(self):
        '''Integrates each of the functions in the vector function'''
        return VectorFunction(list(map(sympy.integrate, self.__lst)))

    def getDomain(self):
        '''Returns domain of vector-value function
        
        Return:
            Union: the domain of the vector-value function
        '''

        # Starts domain in all reals
        domain = sympy.Interval(-sympy.oo, sympy.oo)

        # Intersection for each function's domain
        for vector in self.__lst:
            domain = sympy.Intersection(continuous_domain(
                vector, sympy.Symbol('t'), sympy.S.Reals), domain)
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
        t = sympy.Symbol('t')
        return VectorFunction([elem.subs(t, pt) for elem in self.__lst])

    def getTangentLine(self, tau):
        '''Gets the parametric equation of the tangent line to the original function
        
        Parameter
        =========
            tau (int): the point
        
        Return
        ======
            ParametricLine: the parametic tangent line at t
        '''
        point, vector = self.plugin(tau), self.derive().plugin(tau)
        return ParametricLine(point.__lst, vector.__lst)


if __name__ == '__main__':
    t = sympy.Symbol('t')
    v = VectorFunction([sympy.cos(t), sympy.sin(t), t])
    print(v.getTangentLine(sympy.pi/2))    

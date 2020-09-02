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
        t = sympy.Symbol('t')
        return VectorFunction([sympy.diff(elem, t) for elem in self.__lst])

    def integrate(self):
        '''Integrates each of the functions in the vector function'''
        t = sympy.Symbol('t')
        return VectorFunction([sympy.integrate(elem, t) for elem in self.__lst])

    def getDomain(self):
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

    def solveIntegration(self, tau, initial):
        '''Solve for position function, given a velocity function, point, and start position

        Parameters
        ==========
            tau (int): the point
            initial (list): the initial vector-value position
        
        Return
        ======
            VectorFunction: the position vector-value function
        '''
        pos = self.integrate()
        plugged = pos.plugin(tau).__lst
        c = initial[0] - plugged[0]
        return VectorFunction([i+c for i in pos.__lst])

if __name__ == '__main__':
    t = sympy.Symbol('t')
    v = VectorFunction([sympy.cos(t), sympy.sin(t), t])
    print(v.getTangentLine(sympy.pi/2))
    v2 = VectorFunction([4*t, sympy.E**t])
    print(v2.solveIntegration(0, [2,3]).getVector())

    v1 = VectorFunction([t**2, sympy.sqrt(1-t), -1/t])
    v2 = VectorFunction([sympy.ln(t+1), 1/((sympy.E**t)-2), t])
    v3 = VectorFunction([sympy.cos(t), sympy.sin(t), 5])
    print(v1.getDomain())
    print(v2.getDomain())
    print(v3.getDomain())
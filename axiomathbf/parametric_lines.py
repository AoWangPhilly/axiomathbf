'''
description: parametric lines in 3D space
author: ao wang
date: 09/02/2020
'''
import math

import sympy
from IPython.display import Math, display
from sympy.matrices import Matrix
from sympy.vector import CoordSys3D, matrix_to_vector

from axiomathbf.environment import isnotebook


class ParametricLine():
    '''A ParametricLine class that determines if lines are parallel,
       intersecting, or skew, point of intersection, and displaying
       the equations in latex.

    :param point: a point
    :type point: sympy.geometry.point.Point3D
    :param vector: a directonal vector
    :type vector: sympy.matrices.dense.MutableDenseMatrix
    '''

    def __init__(self, point, vector):
        self.point = sympy.Point(point)

        # Simplifies the directional vector
        self.vector = Matrix(vector)/sympy.gcd(list(vector))

    def __repr__(self):
        if isnotebook():
            display(Math(self.get_point_vector()))
            return ''
        return self.__str__()

    def __str__(self):
        x, y, z = self.point
        v1, v2, v3 = self.vector
        return '<x, y, z> = <{}, {}, {}> + <{}, {}, {}>t'.format(x, y, z, v1, v2, v3)

    def __eq__(self, other):
        # Checks equality of two Parametric Lines given they have the same point and same direction vectors
        return self.point == other.point and (self.vector == other.vector or self.vector == -other.vector)

    def get_point(self):
        '''Gets the point class attribute

        :return: the point class attribute
        :rtype: sympy.geometry.point.Point3D
        '''
        return self.point

    def set_point(self, point):
        '''Sets the point class attribute

        :param point: the point class attribute
        :type point: sympy.geometry.point.Point3D
        '''
        self.point = point

    def get_vector(self):
        '''Gets the vector class attribute

        :return: the vector class attribute
        :rtype: sympy.matrices.dense.MutableDenseMatrix
        '''
        return self.vector

    def set_vector(self, vector):
        '''Sets the vector class attribute

        :param vector: the vector class attribute
        :type vector: sympy.matrices.dense.MutableDenseMatrix
        '''
        self.vector = vector

    def compare(self, other):
        '''Compares two lines to see if they're intersecting, parallel, or skew

        :param other: the other line
        :type other: axiomathbf.parametric_line.ParametricLine
        :return: string that shows if intersecting, parallel, or skew
        :rtype: str
        '''
        if self.intersect(other):
            if self.vector.dot(other.vector) == 0:
                symbol = 'Perpendicular'
            else:
                symbol = 'Intersecting'
        elif self.vector.cross(other.vector).norm() == 0:
            symbol = 'Parallel'
        else:
            symbol = 'Skew'
        return symbol

    def distance(self, other):
        '''Calculates the distance between another ParametricLine object or sympy.Point object

        :param other: the other 3D object
        :type other: sympy.geometry.point.Point3D or axiomathbf.parametric_line.ParametricLine
        :return: the distance between the two objects
        :rtype: sympy.core.numbers.Floats
        '''
        if isinstance(other, ParametricLine):
            pq = Matrix(other.point-self.point)
            lines = self.compare(other)
            if lines == 'Skew':
                return abs(pq.dot(other.vector.cross(self.vector)))/(other.vector.cross(self.vector).norm())
            elif lines == 'Parallel':
                v = (pq.dot(self.vector)/(self.vector.norm())**2)*self.vector
                return (pq - v).norm()
            else:
                return 0
        elif isinstance(other, sympy.Point):
            pq = Matrix(other - self.point)
            return pq.cross(self.vector).norm()/self.vector.norm()

    def get_point_vector(self):
        '''Returns latex form of the vector in point vector form

        :return: renders latex of parametric line
        :rtype: str
        '''
        x, y, z = self.point
        v1, v2, v3 = self.vector
        return sympy.latex('$\\vec{\\ell(t)} = \\langle' + '{}, {}, {}'.format(x, y, z)
                           + '\\rangle +t \\langle ' + ' {}, {}, {}'.format(v1, v2, v3) + '\\rangle$')

    def intersect(self, other):
        '''Returns the point of intersection of two lines

        :return: the point of intersection
        :rtype: returns list of ints when intersecting, None if not intersecting
        '''
        x, y = sympy.symbols('x y')
        indices = [(i, j) for i in range(3) for j in range(i+1, 3)]

        solutions = []
        for i in indices:
            first, latter = i
            r1 = [self.vector[first], -other.vector[first],
                  other.point[first]-self.point[first]]
            r2 = [self.vector[latter], -other.vector[latter],
                  other.point[latter]-self.point[latter]]
            if r1 == r2:
                continue
            a = Matrix([r1, r2])
            solutions.append(sympy.solve_linear_system(a, x, y))
        if None not in solutions and solutions.count(solutions[0]) == len(solutions):
            return [pt + v*solutions[0][x] for (pt, v) in zip(self.point, self.vector)]
        return None

'''
description: parametric lines in 3D space
author: ao wang
date: 09/02/2020
'''
import sympy
from sympy.matrices import Matrix
from sympy.vector import CoordSys3D, matrix_to_vector
import math
from environment import isnotebook
from IPython.display import display, Math


class ParametricLine():
    '''A ParametricLine class that determines if lines are parallel,
       intersecting, or skew, point of intersection, and displaying
       the equations in latex.

    Attributes
    ==========
        point (Point): the point of xyz parametric equations
        vector (Matrix): the directional vector of parametric line
    '''

    def __init__(self, point, vector):
        self.point = sympy.Point(point)

        # Simplifies the directional vector
        self.vector = Matrix(vector)/sympy.gcd(list(vector))

    def __repr__(self):
        if isnotebook():
            display(Math(self.get_point_vector().replace('\\', '\\\\')))
            return ''
        return self.__str__

    def __str__(self):
        x, y, z = self.point
        v1, v2, v3 = self.vector
        return '<x, y, z> = <{}, {}, {}> + <{}, {}, {}>t'.format(x, y, z, v1, v2, v3)

    def __eq__(self, other):
        # Checks equality of two Parametric Lines given they have the same point and same direction vectors
        return self.point == other.point and (self.vector == other.vector or self.vector == -other.vector)

    def get_point(self):
        return self.point

    def set_point(self, point):
        self.point = point

    def get_vector(self):
        return self.vector

    def set_vector(self, vector):
        self.vector = vector

    def compare(self, other):
        '''Compares two lines to see if they're intersecting, parallel, or skew

        Parameter
        =========
            other (ParametricLine): the other line

        Return
        ======
            str: string that shows if intersecting, parallel, or skew
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

        Parameter
        =========
            other (sympy.Point or ParametricLine): the other ParametricLine or a sympy.Point

        Return
        ======
            sympy.Number: the distance between the two objects
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

        Return
        ======
            latex: renders latex of parametric line
        '''
        x, y, z = self.point
        v1, v2, v3 = self.vector
        return sympy.latex('$\\vec{\\ell(t)} = \\langle' + '{}, {}, {}'.format(x, y, z)
                           + '\\rangle +t \\langle ' + ' {}, {}, {}'.format(v1, v2, v3) + '\\rangle$')

    def intersect(self, other):
        '''Returns the point of intersection of two lines

        Return
        ======
            list or None: returns list when intersecting, None if not intersecting
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


if __name__ == '__main__':
    # Parallel
    pt1, vec1 = [2, 1, 4], [3, -2, 5]
    pt2, vec2 = [3, -2, -1], [-6, 4, -10]
    line1 = ParametricLine(pt1, vec1)
    line2 = ParametricLine(pt2, vec2)
    print(line1.compare(line2))

    # Skew
    pt3, vec3 = [1, 0, 2], [0, 1, -1]
    pt4, vec4 = [2, 4, 0], [3, -3, 1]
    line3 = ParametricLine(pt3, vec3)
    line4 = ParametricLine(pt4, vec4)
    print(line3.compare(line4))

    # Intersection at (x,y,z) = (3,13,6)
    pt5, vec5 = [1, 14, 5], [-2, 1, -1]
    pt6, vec6 = [0, 4, 3], [1, 3, 1]
    line5 = ParametricLine(pt5, vec5)
    line6 = ParametricLine(pt6, vec6)
    print(line5.compare(line6))
    print(line5.intersect(line6))

    # Skew
    pt7, vec7 = [2, 4, 1], [5, -1, 1]
    pt8, vec8 = [3, 1, 0], [6, -1, 1]
    line7 = ParametricLine(pt7, vec7)
    line8 = ParametricLine(pt8, vec8)
    print(line7.compare(line8))

    # Skew
    pt9, vec9 = [1, 2, -1], [-1, 3, -2]
    pt10, vec10 = [3, 1, 0], [4, -1, 0]
    line9 = ParametricLine(pt9, vec9)
    line10 = ParametricLine(pt10, vec10)
    print(line9.compare(line10))

    # print(ParametricLine([1, 3, 5], [2, 5, 2]).intersect(
    #     ParametricLine([0, 11, 4], [1, -1, 1])))
    l1 = ParametricLine(point=[5, 3, 0], vector=[3, 9, 0])
    l2 = ParametricLine(point=[1, 0, 1], vector=[1, 3, 0])
    print(math.isclose(sympy.sqrt(910)/10, sympy.sqrt(91/10)))

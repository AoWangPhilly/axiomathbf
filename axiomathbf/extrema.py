'''
description: extrema class
author: ao wang
date: 09/12/2020
'''

import sympy
from IPython.display import Math, display
from sympy import E
from sympy.abc import x, y, z


class Extrema():
    '''The Extrema class calculates the critical points of a function, infer if the points are
    relative minimum, maximum, or saddlepoint. It can also find a function's absolute extremas.

    :param function: the multivariable function
    :type function: sympy.core.add.Add
    '''

    def __init__(self, function):
        self.function = function

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(self.function)

    def set_function(self, function):
        '''Sets the function class parameter

        :param function: the multivariable function
        :type function: sympy.core.add.Add
        '''
        self.function = function

    def get_function(self):
        '''Gets the function class parameter

        :return: the function parameter
        :rtype: sympy.core.add.Add
        '''
        return self.function

    def get_critical_points(self):
        '''Finds all critical points of a function

        :return: the critical points
        :rtype: tuples of ints or list of tuples of ints
        '''
        gradient = sympy.derive_by_array(self.function, (x, y))
        stationary_points = sympy.solve(gradient, (x, y))
        if type(stationary_points) == dict:
            return (stationary_points[x], stationary_points[y])
        return stationary_points

    def get_relative(self):
        '''Finds the relative extremas of the function

        :return: determines if point of mini, max, of saddle point
        :rtype: str
        '''
        results = ''
        gradient = sympy.derive_by_array(self.function, (x, y))
        hessian = sympy.Matrix(sympy.derive_by_array(gradient, (x, y)))
        crit_points = sympy.solve(gradient, (x, y))

        if type(crit_points) == dict:
            crit_points = [(crit_points[x], crit_points[y])]
        for point in crit_points:
            hess = hessian.subs({x: point[0], y: point[1]})
            d, fxx = hess.det(), hess[0]
            if d > 0 and fxx > 0:
                results += 'Relative minimum at {}\n'.format(point)
            elif d > 0 and fxx < 0:
                results += 'Relative maximum at {}\n'.format(point)
            elif d < 0:
                results += 'Saddle point at {}\n'.format(point)
            else:
                results += 'Results inconclusive at {}\n'.format(point)
        return results

    def __get_area(self, p1, p2, p3):
        '''Calculates area of triangle given three points

        :param p1: first point
        :type p1: tuple of ints
        :param p2: second point
        :type p2: tuple of ints
        :param p3: third point
        :type p3: tuple of ints
        :return: the area of a triangle
        :rtype: int
        '''
        return abs(p1[0]*(p2[1]-p3[1])+p2[0]*(p3[1]-p1[1])+p3[0]*(p1[1]-p2[1]))

    def __is_inside(self, edge_cases, pt):
        '''Checks to see if a point is inside a triangle

        :param edge_cases: the other points to test out
        :type edge_cases: list of tuples of ints
        :param pt: the point to check
        :type pt: tuple of ints
        :return: whether or not point is in triangle
        :rtype: bool
        '''
        a_total = self.__get_area(edge_cases[0], edge_cases[1], edge_cases[2])
        a1 = self.__get_area(pt, edge_cases[1], edge_cases[2])
        a2 = self.__get_area(edge_cases[0], pt, edge_cases[2])
        a3 = self.__get_area(edge_cases[0], edge_cases[1], pt)
        return a_total == (a1+a2+a3)

    def get_absolute(self, edge_cases):
        '''Calculates the absolute extrema of a function.

        Warning!! Can only check for three edge cases for the closed region (i.e. a triangle border)

        :param edge_cases: the other points to test out
        :type edge_cases: list of tuples of ints
        :return: the absolute extrema
        :rtype: dict of dict of ints
        '''

        # Gets critical points
        points = self.get_critical_points()

        # Get the min and max of the x and y positions from edge cases
        max_y, min_y, max_x, min_x = - \
            float('inf'), float('inf'), -float('inf'), float('inf')
        points = [points]
        for p in edge_cases:
            if p[1] > max_y:
                max_y = p[1]
            if p[1] < min_y:
                min_y = p[1]
            if p[0] > max_x:
                max_x = p[0]
            if p[0] < min_x:
                min_x = p[0]

        if any(points):  # Checks if there are any points to check
            for p in points:
                if p[0] < min_x or p[0] > max_x or p[1] < min_y or p[1] > max_y:
                    points.remove(p)
        else:  # If not, remove the nested empty list
            points.remove([])

        # Loop through possible points for absolute extrema
        for i in range(min_x, max_x+1):
            for j in range(min_y, max_y+1):
                if self.__is_inside(edge_cases=edge_cases, pt=(i, j)):
                    points.append((i, j))

        # Subsitute the values and find the max and min
        maximum, minimum = -float('inf'), float('inf')
        for p in points:
            val = self.function.subs({x: p[0], y: p[1]})
            if val > maximum:
                maximum = val
                max_p = p
            if val < minimum:
                minimum = val
                min_p = p
        return {'max': {'point': max_p, 'value': maximum},
                'min': {'point': min_p, 'value': minimum}}

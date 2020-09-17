'''
description: extrema class
author: ao wang
date: 09/12/2020
'''

import sympy
from sympy import E
from sympy.abc import x, y, z
from IPython.display import display, Math


class Extrema():
    '''Extrema class that can find the critical points of the function, infer if the points are
       relative minimum, maximum, or saddlepoint, and also absolute max/min.

    Attribute
    =========
        function (sympy.core.add.Add): the function
    '''

    def __init__(self, function):
        self.function = function

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(self.function)

    def set_function(self, function):
        self.function = function

    def get_function(self):
        return self.function

    def get_critical_points(self):
        '''Returns all critical points of a function

        Return
        ======
            list of tuples of ints: the critical points
        '''
        gradient = sympy.derive_by_array(self.function, (x, y))
        stationary_points = sympy.solve(gradient, (x, y))
        if type(stationary_points) == dict:
            return (stationary_points[x], stationary_points[y])
        return stationary_points

    def get_relative(self):
        '''Gets the relative extremas of the function

        Return
        ======
            str: determines if point of mini, max, of saddle point

        Warning
        =======
            Only considers triangle border
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
        return abs(p1[0]*(p2[1]-p3[1])+p2[0]*(p3[1]-p1[1])+p3[0]*(p1[1]-p2[1]))

    def __is_inside(self, edge_cases, pt):
        a_total = self.__get_area(edge_cases[0], edge_cases[1], edge_cases[2])
        a1 = self.__get_area(pt, edge_cases[1], edge_cases[2])
        a2 = self.__get_area(edge_cases[0], pt, edge_cases[2])
        a3 = self.__get_area(edge_cases[0], edge_cases[1], pt)
        return a_total == (a1+a2+a3)

    def get_absolute(self, edge_cases):
        '''Gets the absolute extrema of a function

        Parameter
        =========
            edge_cases (list of tuples of ints): the other points to test out

        Return
        ======
            dict: the absolute minimum and maximum
        '''

        # Gets critical points
        points = self.get_critical_points()

        # Get the min and max of the x and y positions from edge cases
        max_y, min_y, max_x, min_x = - \
            float('inf'), float('inf'), -float('inf'), float('inf')
        points = [points]
        for p in edge_cases:
            if p[1] > max_y: max_y = p[1]
            if p[1] < min_y: min_y = p[1]
            if p[0] > max_x: max_x = p[0]
            if p[0] < min_x: min_x = p[0]

        if any(points):  # Checks if there are any points to check
            for p in points:
                if p[0] < min_x or p[0] > max_x or p[1] < min_y or p[1] > max_y:
                    points.remove(p)
        else: # If not, remove the nested empty list
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


if __name__ == '__main__':
    # f1 = Extrema(x**2+y**2-3*x-4*y+6)
    # f2 = Extrema(x**2+4*y**2-4*y-2)
    # f3 = Extrema(4*x**2-3*y**2+8*x-9*y-4)
    # f4 = Extrema(x**3-3*x+y**2-6*y)
    # f5 = Extrema(x**2*y-6*y**2-3*x**2)
    # print(f1.get_critical_points())
    # print(f2.get_critical_points())
    # print(f3.get_critical_points())
    # print(f4.get_relative())
    # print(f5.get_relative())
    f6 = Extrema(5-4*y-2*x)

    print(f6.get_absolute([(3, 0), (0, 1), (1, 2)]))

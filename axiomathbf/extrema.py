'''
description: extrema class
author: ao wang
date: 09/12/2020
'''

import sympy
from sympy.abc import x, y, z
from environment import isnotebook
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
        return stationary_points

    def get_relative(self):
        '''Gets the relative extremas of the function

        Return
        ======
            str: determines if point of mini, max, of saddle point
        '''
        results = ''
        gradient = sympy.derive_by_array(self.function, (x, y))
        hessian = sympy.Matrix(sympy.derive_by_array(gradient, (x, y)))
        crit_points = sympy.solve(gradient, (x, y))

        for point in crit_points:
            hess = hessian.subs({x: point[0], y: point[1]})
            eigenvals = hess.eigenvals()
            if all(ev > 0 for ev in eigenvals):
                results += 'Relative minimum at {}\n'.format(point)
            elif all(ev < 0 for ev in eigenvals):
                results += 'Relative maximum at {}\n'.format(point)
            elif any(ev > 0 for ev in eigenvals) and any(ev < 0 for ev in eigenvals):
                results += 'Saddle point at {}\n'.format(point)
            else:
                results += 'Results inconclusive at {}\n'.format(point)
        return results

    def get_absolute(self, edge_cases=None):
        '''Gets the absolute extrema of a function

        Parameter
        =========
            edge_cases (list of tuples of ints): the other points to test out

        Return
        ======
            dict: the absolute minimum and maximum
        '''

        # Gets critical points and edge cases
        points = self.get_critical_points()
        points.extend(edge_cases)

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
    f6 = Extrema(5 - 4*y - 2*x)
    print(f6.get_absolute([(3, 0), (0, 1), (1, 2)]))

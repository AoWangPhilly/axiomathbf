import sympy
from sympy.abc import x, y, z


class Extrema():
    def __init__(self, function):
        self.function = function

    def set_function(self, function):
        self.function = function

    def get_function(self):
        return self.function

    def get_critical_points(self):
        gradient = sympy.derive_by_array(self.function, (x, y))
        stationary_points = sympy.solve(gradient, (x, y))
        return stationary_points

    def get_relative(self):
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


if __name__ == '__main__':
    # f1 = Extrema(x**2+y**2-3*x-4*y+6)
    # f2 = Extrema(x**2+4*y**2-4*y-2)
    # f3 = Extrema(4*x**2-3*y**2+8*x-9*y-4)
    f4 = Extrema(x**3-3*x+y**2-6*y)
    f5 = Extrema(x**2*y-6*y**2-3*x**2)
    # print(f1.get_critical_points())
    # print(f2.get_critical_points())
    # print(f3.get_critical_points())
    print(f4.get_relative())
    print(f5.get_relative())

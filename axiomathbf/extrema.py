import sympy
from sympy.abc import x, y, z


class Extrema():
    def __init__(self, function):
        self.function = function

    def set_function(self, function):
        self.function = function

    def get_function(self):
        return self.function

    def define_d(self):
        pass

    def get_critical_points(self):
        gradient = sympy.derive_by_array(self.function, (x, y))
        return gradient

    def get_relative(self):
        pass

    def get_absolute(self):
        pass


if __name__ == '__main__':
    # f1 = Extrema(x**2+y**2-3*x-4*y+6)
    # f2 = Extrema(x**2+4*y**2-4*y-2)
    # f3 = Extrema(4*x**2-3*y**2+8*x-9*y-4)
    f4 = Extrema(x**3-3*x+y**2-6*y)
    f5 = Extrema(x**2*y-6*y**2-3*x**2)
    # print(f1.get_critical_points())
    # print(f2.get_critical_points())
    # print(f3.get_critical_points())
    print(f4.get_critical_points())
    print(f5.get_critical_points())

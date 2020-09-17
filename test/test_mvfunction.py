from axiomathbf import MVFunction, Gradient, DirectionalDerivative, Plane, ParametricLine
import pytest
from sympy.abc import x, y, z
from sympy import sin, ln, E, pi, cos, tan, atan, sqrt, Matrix, asin, simplify

# Gradient


def test_str():
    f1 = Gradient(x**3-2*x*y**2)
    f2 = Gradient(3*x**2*y**3)
    sols = ['<3*x**2 - 2*y**2, -4*x*y, 0>',
            '<6*x*y**3, 9*x**2*y**2, 0>']
    for f, sol in zip((f1, f2), sols):
        assert str(f) == sol


def test_gradient_vector():
    f1 = Gradient(x**3-2*x*y**2)
    f2 = Gradient(3*x**2*y**3)
    sols = [[3*x**2-2*y**2, -4*x*y, 0],
            [6*x*y**3, 9*x**2*y**2, 0]]
    for f, sol in zip((f1, f2), sols):
        assert f.vector == sol


def test_at():
    f1, p1 = Gradient(3*x*y-y**2*x**3), [1, -1, 0]
    f2, p2 = Gradient(cos(2*x-y**2)), [pi/4, 0, 0]
    f3, p3 = Gradient(4*x*y*z-y**2*z**3+4*z**3*y), [2, 3, 1]
    sols = [Matrix([-6, 5, 0]), Matrix([-2, 0, 0]), Matrix([12, 6, 33])]
    for f, sol in zip(((f1, p1), (f2, p2), (f3, p3)), sols):
        assert f[0].at(f[1]) == sol

# DirectionalDerivative


def test_directional_diff():
    f1 = DirectionalDerivative(
        function=x**4-y**4, point=[0, -2, 0], unit_vector=[sqrt(2)/2, sqrt(2)/2, 0])
    f2 = DirectionalDerivative(
        function=y*sin(x), point=[pi/2, 1, 0], unit_vector=[1, -1, 0])
    f3 = DirectionalDerivative(
        function=E**x*cos(y*z), point=[1, pi, 0], unit_vector=[-2, 1, -3])
    sols = [32/sqrt(2), -1/sqrt(2), -2*E/(sqrt(14))]
    for f, sol in zip((f1, f2, f3), sols):
        assert f.value == sol


def test_info():
    f1 = DirectionalDerivative(E**(x*y**2), [1, 3, 0])
    f2 = DirectionalDerivative(sqrt(4-x**2-y**2-z**2), [1, -1, 0])
    f3 = DirectionalDerivative(x**3*y*z**2, [2, -1, 1])
    sols = [(3*sqrt(13)*E**(9), [3*sqrt(13)/13, 2*sqrt(13)/13, 0]),
            (1, [-sqrt(2)/2, sqrt(2)/2, 0])]
    for f, sol in zip((f1,f2), sols):
        assert f.info() == sol
    assert f3.info(increasing=False) == (-4*sqrt(29), [3*sqrt(29)/29, -2*sqrt(29)/29, 4*sqrt(29)/29])

# MVFunction


def test_linearization():
    f1 = MVFunction(x**2-y**2, [1, 2, 0])
    f2 = MVFunction((x+y)/(x-y), [2, 1, 0])
    f3 = MVFunction(E**x*sin(y), [ln(3), pi/2, 0])
    f4 = MVFunction(ln(x**2-y**2), [2, sqrt(3), 0])
    f5 = MVFunction(atan(x/y), [1, 1, 0])
    sols = [3+2*x-4*y, 3-2*x+4*y, 3-3*ln(3)+3*x,
            -2+4*x-2*sqrt(3)*y, pi/4+(1/2)*x-(1/2)*y]
    for f, sol in zip((f1, f2, f3, f4, f5), sols):
        assert f.get_linearization().equals(sol)


s1 = MVFunction(ln(x+y+z), [-1, E**2, 1])
s2 = MVFunction(x**2+y**2+z**2-1, [sqrt(3)/3, sqrt(3)/3, sqrt(3)/3])
s3 = MVFunction(x**2-x*y+z**2, [2, 2, 3])


def test_tangent_plane():
    sols = [Plane(eq=x+y+z-E**2), Plane(eq=x+y+z-sqrt(3)), Plane(eq=x-y+3*z-9)]
    for s, sol in zip((s1, s2, s3), sols):
        assert s.get_tangent_plane() == sol


def test_normal_line():
    sols = [ParametricLine(point=[-1, E**2, 1], vector=[1, 1, 1]),
            ParametricLine(point=[sqrt(3)/3, sqrt(3)/3,
                                  sqrt(3)/3], vector=[1, 1, 1]),
            ParametricLine(point=[2, 2, 3], vector=[1, -1, 3])]
    for s, sol in zip((s1, s2, s3), sols):
        assert s.get_normal_line() == sol

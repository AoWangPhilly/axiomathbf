from axiomathbf import MVFunction, Gradient, DirectionalDerivative, Plane, ParametricLine
import pytest
import sympy
from sympy.abc import x, y, z
from sympy import sin, ln, E, pi, cos, tan, atan, sqrt

# Gradient


def test_gradient_vector():
    pass


def test_at():
    pass

# DirectionalDerivative


def test_directional_diff():
    pass


def test_info():
    pass

# MVFunction


def test_linearization():
    f1, p1 = x**2-y**2, [1, 2, 0]
    f2, p2 = (x+y)/(x-y), [2, 1, 0]
    f3, p3 = E**x*sin(y), [ln(3), pi/2, 0]
    f4, p4 = ln(x**2-y**2), [2, sqrt(3), 0]
    f5, p5 = atan(x/y), [1, 1, 0]


def test_tangent_plane():
    pass


def test_normal_line():
    pass

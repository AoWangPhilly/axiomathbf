import pytest
from sympy.abc import x, y, z
from sympy import sin, cos, tan, E, pi, ln, sqrt
from axiomathbf import Extrema

def test_critical_pts():
    g1 = x**2+y**2-3*x-4*y+6
    g2 = x**2+4*y**2-4*y-2
    g3 = 4*x**2-3*y**2+8*x-9*y-4
    g4 = x**3-3*x+y**2-6*y
    g5 = x**2-5*x*y+y**2
    g6 = 3*x+y**2-E**x
    g7 = x**6+y**6
    g8 = x**2*y-6*y**2-3*x**2
    g9 = x**3-3*x*y+(1/2)*y**2
    g10 = (1/3)*x**3-2*x+x**2+2*x*y+y**2


def test_relative():
    f1 = 3*sqrt(x**2+y**2)+6


def test_absolute():
    f1, edge1 = 5-4*y-2*x, [(3, 0), (0, 1), (1, 2)]
    f2, edge2 = x**2-4*x*y+5*y**2-8*y, [(0, 0), (3, 0), (3, 3)]

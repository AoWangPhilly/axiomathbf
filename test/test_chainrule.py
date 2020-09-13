import pytest
from axiomathbf import ChainRule
from sympy.abc import x, y, z, w, r, s, t
from sympy import sin, cos, tan, E, pi, ln
import sympy


def test_equation():
    f, x, y, z = (x, y, z, w), (r, s, t), (r, t), (r, s)
    

def test_solve():
    z1, x1, y1 = 2*x-y, sin(t), 3*t
    z2, x2, y2 = x*sin(y), E**t, pi*t
    z3, x3, y3 = x*y+y**2, t**2, t+1
    z4, x4, y4 = ln(x**2/y), E**t, t**2
    w1, x5, y5, z5 = x**2+y**2+2*z**2, t+1, cos(t), sin(t)

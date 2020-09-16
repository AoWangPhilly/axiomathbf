import pytest
from axiomathbf import ChainRule
from sympy.abc import x, y, z, w, r, s, t
from sympy import sin, cos, tan, E, pi, ln
import sympy


def test_equation():
    c1 = ChainRule(f=(x, y, z, w), x=(r, s, t), y=(r, t), z=(r, s), w=(s, t))
    c2 = ChainRule(z=(x, y), x=(t,), y=(t,))

    d1, d2, d3 = 'df/dr', 'df/ds', 'df/dt'
    sols = ['∂f/∂x * ∂x/∂r + ∂f/∂y * ∂y/∂r + ∂f/∂z * ∂z/∂r',
            '∂f/∂x * ∂x/∂s + ∂f/∂z * ∂z/∂s + ∂f/∂w * ∂w/∂s',
            '∂f/∂x * ∂x/∂t + ∂f/∂y * ∂y/∂t + ∂f/∂w * ∂w/∂t']
    for d, sol in zip((d1, d2, d3), sols):
        assert c1.get_equation(d) == sol
    assert c2.get_equation('dz/dt') == '∂z/∂x * ∂x/∂t + ∂z/∂y * ∂y/∂t'


def test_solve():
    z1, x1, y1 = 2*x-y, sin(t), 3*t
    z2, x2, y2 = x*sin(y), E**t, pi*t
    z3, x3, y3 = x*y+y**2, t**2, t+1
    z4, x4, y4 = ln(x**2/y), E**t, t**2
    w1, x5, y5, z5 = x**2+y**2+2*z**2, t+1, cos(t), sin(t)
    sols = [2*cos(t)-3, E**t*sin(pi*t)+pi*E**t*cos(pi*t), 3*t**2+4*t+2, 2-2/t]
    for f, sol in zip(((z1, x1, y1), (z2, x2, y2), (z3, x3, y3), (z4, x4, y4)), sols):
        assert ChainRule().solve('dz/dt', z=f[0], x=f[1], y=f[2]).equals(sol)

    assert ChainRule().solve('dw/dt', w=w1, x=x5, y=y5, z=z5).equals(2*t+2+2*sin(t)*cos(t))

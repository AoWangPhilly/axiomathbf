import pytest
from sympy.abc import x, y, z
from sympy import sin, cos, tan, E, pi, ln, sqrt, log
from axiomathbf import Extrema

g1 = Extrema(x**2+y**2-3*x-4*y+6)
g2 = Extrema(x**2+4*y**2-4*y-2)
g3 = Extrema(4*x**2-3*y**2+8*x-9*y-4)
g4 = Extrema(x**3-3*x+y**2-6*y)
g5 = Extrema(x**2-5*x*y+y**2)
g6 = Extrema(3*x+y**2-E**x)
g7 = Extrema(x**6+y**6)
g8 = Extrema(x**2*y-6*y**2-3*x**2)
g9 = Extrema(x**3-3*x*y+(1/2)*y**2)
g10 = Extrema((1/3)*x**3-2*x+x**2+2*x*y+y**2)


def test_critical_pts():
    sols = [(3/2, 2), (0, 1/2), (-1, -3/2), [(-1, 3), (1, 3)],
            (0, 0), (log(3), 0), [(0, 0)], [(-6, 3), (0, 0), (6, 3)],
            [(0, 0), (3, 9)]]

    for g, sol in zip((g1, g2, g3, g4, g5, g6, g7, g8, g9), sols):
        assert g.get_critical_points() == sol


def test_relative():
    sols = ['Relative minimum at (3/2, 2)\n',
            'Relative minimum at (0, 1/2)\n',
            'Saddle point at (-1, -3/2)\n',
            'Saddle point at (-1, 3)\nRelative minimum at (1, 3)\n',
            'Saddle point at (0, 0)\n',
            'Saddle point at (log(3), 0)\n',
            'Results inconclusive at (0, 0)\n',
            'Saddle point at (-6, 3)\nRelative maximum at (0, 0)\nSaddle point at (6, 3)\n',
            'Saddle point at (0.0, 0.0)\nRelative minimum at (3.00000000000000, 9.00000000000000)\n',
            'Saddle point at (-1.41421356237310, 1.41421356237310)\nRelative minimum at (1.41421356237310, -1.41421356237310)\n']
    for g, sol in zip((g1, g2, g3, g4, g5, g6, g7, g8, g9, g10), sols):
        assert g.get_relative() == sol


def test_absolute():
    f1, edge1 = Extrema(5-4*y-2*x), [(3, 0), (0, 1), (1, 2)]
    f2, edge2 = Extrema(x**2-4*x*y+5*y**2-8*y), [(0, 0), (3, 0), (3, 3)]
    sols = [{'max': {'point': (0, 1), 'value': 1}, 'min': {'point': (1, 2), 'value': -5}},
            {'max': {'point': (3, 0), 'value': 9}, 'min': {'point': (3, 2), 'value': -11}}]
    for f, sol in zip(((f1, edge1), (f2, edge2)), sols):
        assert f[0].get_absolute(f[1]) == sol

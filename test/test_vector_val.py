from axiomathbf import VectorFunction, ParametricLine
import pytest
from sympy import Symbol, sqrt, ln, E, cos, sin, tan, sec, Union, Interval, oo, Reals, log, pi
from sympy.abc import t


def test_str():
    r1 = VectorFunction([3*t, t**2, t**3+1])
    r2 = VectorFunction([cos(t), sin(t), t])
    r3 = VectorFunction([ln(t), 1, t**2])
    sols = ['<3*t, t**2, t**3 + 1>',
            '<cos(t), sin(t), t>',
            '<log(t), 1, t**2>']
    for r, sol in zip((r1, r2, r3), sols):
        assert str(r) == sol


def test_eq():
    r1 = VectorFunction([6*t, 1/t, 0])
    r2 = VectorFunction([sin(t), t**3, 1-t])
    r3 = VectorFunction([2*t*cos(t), t**2, t-1])
    sols = [VectorFunction([6*t, 1/t, 0]),
            VectorFunction([sin(t), t**3, 1-t]),
            VectorFunction([2*t*cos(t), t**2, t-1])]
    for r, sol in zip((r1, r2, r3), sols):
        assert r == sol


def test_diff():
    v1 = VectorFunction([3*t**2, ln(t), 4])
    v2 = VectorFunction([sin(t), t**3, 1-t])
    v3 = VectorFunction([cos(t), sin(t), t])
    sols = [VectorFunction([6*t, 1/t, 0]),
            VectorFunction([cos(t), 3*t**2, -1]),
            VectorFunction([-sin(t), cos(t), 1])]
    for v, s in zip((v1, v2, v3), sols):
        assert v.derive() == s


def test_integration():
    v1 = VectorFunction([(2*t+1)**5, -1/t, 0])
    v2 = VectorFunction([sin(t), cos(t), tan(t)])
    answers = [VectorFunction([16*t**6/3 + 16*t**5 + 20*t**4 + 40*t**3/3 + 5*t**2 + t, -log(t), 0]),
               VectorFunction([-cos(t), sin(t), -ln(cos(t))])]
    for v, a in zip((v1, v2), answers):
        assert v.integrate() == a


def test_domain():
    v1 = VectorFunction([t**2, sqrt(1-t), -1/t])
    v2 = VectorFunction([ln(t+1), 1/(E**t-2), t])
    v3 = VectorFunction([cos(t), sin(t), 5])
    v4 = VectorFunction([ln(t), t+1, E**t])
    v5 = VectorFunction([sin(t), ln(abs(t)), sqrt(4-t)])
    answers = [Union(Interval.Ropen(-oo, 0), Interval.Lopen(0, 1)),
               Union(Interval.open(-1, log(2)), Interval.open(log(2), oo)),
               Reals,
               Interval.open(0, oo),
               Union(Interval.open(-oo, 0), Interval.Lopen(0, 4))]

    for v, d in zip((v1, v2, v3, v4, v5), answers):
        assert v.get_domain() == d


def test_plugin():
    r1, t1 = VectorFunction([-sin(t), cos(t), 1]), pi/2
    r2, t2 = VectorFunction([6*t, 1/t, 0]), 2
    r3, t3 = VectorFunction([cos(t), sin(t), t]), pi/2
    sols = [[-1, 0, 1], [12, 1/2, 0], [0, 1, pi/2]]
    for r, sol in zip(((r1, t1), (r2, t2), (r3, t3)), sols):
        assert r[0].plugin(r[1]) == sol


def test_line_tangent():
    r1, p1 = VectorFunction([ln(t), 2*sqrt(t), t**2]), [0, 2, 1]
    r2, p2 = VectorFunction([sin(t), cos(t), tan(t)]), pi
    l1 = ParametricLine(point=[0, 2, 1], vector=[1, 1, 2])
    l2 = ParametricLine(point=[0, -1, 0], vector=[-1, 0, 1])
    assert r1.get_tangent_line(point=p1) == l1
    assert r2.get_tangent_line(tau=p2) == l2


def test_solve_integration():
    r1, i1, p1 = VectorFunction([E**-t, 3*t**2, 0]), [2, -8, 0], 0
    r2, i2, p2 = VectorFunction([4*t, E**t, 0]), [2, 3, 0], 0
    sols = [VectorFunction([-E**(-t)+3, t**3-8, 0]),
            VectorFunction([2*t**2+2, E**t+2, 0])]
    assert r1.solve_integration(initial=i1, point=p1) == sols[0]
    assert r2.solve_integration(initial=i2, point=p2) == sols[1]

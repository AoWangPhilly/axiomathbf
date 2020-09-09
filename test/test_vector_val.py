from axiomathbf import VectorFunction
import pytest
from sympy import Symbol, sqrt, ln, E, cos, sin, tan, sec, Union, Interval, oo, Reals, log, pi
from sympy.abc import t


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
        assert v.getDomain() == d


def test_line_tangent():
    r1, p1 = VectorFunction([ln(t), 2*sqrt(t), t**2]), [0, 2, 1]
    r2, p2 = VectorFunction([sin(t), cos(t), tan(t)]), pi
    assert r1.getTangentLine(point=p1) == r2.getTangentLine(tau=p2)


def test_integration():
    v1 = VectorFunction([(2*t+1)**5, -1/t, 0])
    v2 = VectorFunction([sin(t), cos(t), tan(t)])
    v3 = VectorFunction([E**t, E**(2*t), 0])
    answers = [VectorFunction([(1/12)*(2*t+1)**6, - ln(abs(t)), 0]),
               VectorFunction([-cos(t), sin(t), ln(abs(sec(t)))]),
               VectorFunction([2, 4, 0])]
    for v, a in zip((v1, v2, v3), answers):
        pass


def test_diff():
    v1 = VectorFunction([3*t**2, ln(t), 4])
    v2 = VectorFunction([sin(t), t**3, 1-t])
    answers = [VectorFunction([6*t, 1/t, 0]),
               VectorFunction(2*t*cos(t), t**2, t-1)]
    for v, a in zip((v1, v2), answers):
        assert v.derive() == a

def test_solve_integration():
    pass
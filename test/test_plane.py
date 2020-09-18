from axiomathbf import Plane, ParametricLine
import sympy
from sympy import sqrt, acos, Point, pi, asin
from sympy.abc import x, y, z
import pytest


def test_str():
    p1, n1 = [1, 2, 1], [-7, -8, -10]
    p2, p3, p4 = [1, 2, 1], [3, -1, 2], [-1, 0, 4]

    plane1 = Plane(p1=p1, normal_vector=n1)
    plane2 = Plane(p1=p2, p2=p3, p3=p4)
    sols = [Plane(eq=-7*(x-1)-8*(y-2)-10*(z-1)),
            Plane(eq=-7*(x-1)-8*(y-2)-10*(z-1))]

    for plane, sol in zip((plane1, plane2), sols):
        assert str(plane) == str(sol)


def test_eq():
    p1 = Plane(eq=3*x-y+2*z+1)
    p2 = Plane(p1=[-3, 2, 5], normal_vector=[3, -1, 2])

    p3 = Plane(p1=[1, 2, 3], normal_vector=[4, -2, 6])
    p4 = Plane(eq=4*(x-1)-2*(y-2)+6*(z-3))

    p5 = Plane(p1=[1, 2, 3], p2=[2, -1, 5], p3=[-1, 3, 3])
    p6 = Plane(eq=-2*(x-1)-4*(y-2)-5*(z-3))

    for p in ((p1, p2), (p3, p4), (p5, p6)):
        assert (p[0] == p[1]) == True


def test_angle():
    p1, p2 = Plane(eq=3*x-2*y+5*z), Plane(eq=-x-y+2*z-3)

    p3, p4 = Plane(eq=2*x-3*y+4*z-5), Plane(eq=3*x+5*y-2*z-7)

    p5, l1 = Plane(
        eq=2*x-y+z-4), ParametricLine(point=[1, 2, -1], vector=[1, -1, 1])
    sols = [acos(9/(sqrt(38*6))), acos(-17/sqrt(1102)), asin(4/sqrt(18))]
    for p, sol in zip(((p1, p2), (p3, p4), (p5, l1)), sols):
        assert p[0].angle(p[1]) == sol


def test_compare():
    p1, p2 = Plane(eq=5*x-3*y+4*z+1), Plane(eq=2*x-2*y-4*z-9)
    p3, p4 = Plane(eq=3*x-2*y+z+3), Plane(eq=5*x+y-6*z-8)
    p5, p6 = Plane(eq=3*x-2*y+z+3), Plane(eq=-6*x+4*y-2*z-1)

    p7 = Plane(eq=5*x-3*y+4*z+1)
    l1 = ParametricLine(point=[2, 3, 5], vector=[2, -2, -4])
    p8 = Plane(eq=5*x-3*y+4*z+1)
    l2 = ParametricLine(point=[2, 3, 5], vector=[5/2, -3/2, 2])
    sols = ['Perpendicular', 'Neither parallel nor perpendicular',
            'Parallel', 'Parallel', 'Perpendicular']
    for t, sol in zip(((p1, p2), (p3, p4), (p5, p6), (p7, l1), (p8, l2)), sols):
        assert t[0].compare(t[1]) == sol


def test_distance():
    plane1, p1 = Plane(eq=x+2*y+3*z-5), Point([2, -1, 4])
    plane2, plane3 = Plane(eq=2*x-4*y+5*z+2), Plane(eq=x-2*y+(5/2)*z-5)
    plane4, line1 = Plane(
        eq=2*x+3*y+4*z-12), ParametricLine(point=[2, 3, 3], vector=[-1, 2, 4])
    sols = [7/sympy.sqrt(14), 12/sympy.sqrt(45), 13/sqrt(29)]
    for p, sol in zip(((plane1, p1), (plane2, plane3), (plane4, line1)), sols):
        assert p[0].distance(p[1]) == sol


def test_intersect():
    p1, p2 = Plane(eq=x+y+z-7), Plane(eq=2*x+4*z-6)
    p3, p4 = Plane(eq=x+y+z+1), Plane(eq=x+2*y+3*z+4)
    sols = [ParametricLine(point=[3, 4, 0], vector=[-2, 1, 1]),
            ParametricLine(point=[2, -3, 0], vector=[1, -2, 1])]
    for p, sol in zip(((p1, p2), (p3, p4)), sols):
        assert p[0].intersect(p[1]) == sol

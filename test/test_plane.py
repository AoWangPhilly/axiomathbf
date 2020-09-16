from axiomathbf import Plane
from axiomathbf import ParametricLine
import sympy
from sympy.abc import x, y, z
import pytest


def test_str():
    p1, n1 = [1, 2, 3], [4, -2, 6]
    p2, p3, p4 = [1, 2, 3], [2, -1, 5], [-1, 3, 3]
    plane1 = Plane(p1=p1, normal_vector=n1)
    plane2 = Plane(p1=p1, p2=p2, p3=p3)
    sols = [Plane(eq=4*(x-1)-2*(y-2)+6(z-3)),
            Plane(eq=-2*(x-1)-4*(y-2)-5*(z-3))]

    for plane, sol in zip((plane1, plane2), sols):
        assert plane == sol


def test_angle():
    p1 = Plane(eq=3*x-2*y+5*z)
    p2 = Plane(eq=-x-y+2*z-3)
    sols = [sympy.acos(9/(sympy.sqrt(38*6)))]


def test_compare():
    p1, p2 = Plane(eq=5*x-3*y+4*z+1), Plane(eq=2*x-2*y-4*z-9)
    p3, p4 = Plane(eq=3*x-2*y+z+3), Plane(eq=5*x+y-6*z-8)
    p5, p6 = Plane(eq=3*x-2*y+z+3), Plane(eq=-6*x+4*y-2*z-1)

    p7 = Plane(eq=5*x-3*y+4*z+1)
    l1 = ParametricLine(point=[2, 3, 5], vector=[2, -2, -4])
    p8 = Plane(eq=5*x-3*y+4*z+1)
    l2 = ParametricLine(point=[2, 3, 5], vector=[5/2, -3/2, 2])
    sols = ["Perpendicular", ' Neither', 'Parallel', 'Perpendicular']
    for t, sol in zip(((p1, p2), (p3, p4), (p5, p6), (p7, l1), (p8, l2)), sols):
        assert t[0].compare(t[1]) == sol


def test_distance():
    plane1, p1 = Plane(eq=x+2*y+3*z-5), [2, -1, 4]
    plane2, plane3 = Plane(eq=2*x-4*y+5*z+2), Plane(eq=x-2*y+(5/2)*z-5)
    sols = [7/sympy.sqrt(14), 12/sympy.sqrt(45)]


def test_intersect():
    p1, p2 = Plane(eq=x+y+z-7), Plane(eq=2*x+4*z-6)
    sols = [ParametricLine(point=[3, 4, 0], vector=[-2, 1, 1])]

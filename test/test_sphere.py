import pytest
from axiomathbf.Sphere import *
from sympy import symbols, Point

# export PYTHONPATH=/path/to/my/library:$PYTHONPATH
x, y, z = symbols("x y z")


def test_format_equation1():
    eq1 = 4*x**2 + 4*y**2 - 16*x - 24*y + 51
    eq2 = z**2 + (x - 2)**2 + (y - 3)**2 - 1/4
    assert Sphere(eq=eq1) == Sphere(eq=eq2)


def test_format_equation2():
    eq1 = x**2+y**2-4*x+12*y-8
    eq2 = z**2 + (x - 2)**2 + (y + 6)**2 - 48
    assert Sphere(eq=eq1) == Sphere(eq=eq2)


def test_format_equation3():
    eq1 = x**2+y**2+6*x-12*y+20
    eq2 = z**2 + (x + 3)**2 + (y - 6)**2 - 25
    assert Sphere(eq=eq1) == Sphere(eq=eq2)


def test_format_equation4():
    eq1 = x**2+y**2+4*x+6*y-36
    eq2 = z**2 + (x + 2)**2 + (y + 3)**2 - 49
    assert Sphere(eq=eq1) == Sphere(eq=eq2)


def test_format_equation5():
    eq1 = x**2+y**2-12*x+8*y+3
    eq2 = z**2 + (x - 6)**2 + (y + 4)**2 - 49
    assert Sphere(eq=eq1) == Sphere(eq=eq2)


def test_get_center1():
    assert Sphere(eq=x**2+y**2+4*x+6*y-36).getCenter() == Point(-2, -3, 0)


def test_get_radius1():
    assert Sphere(eq=x**2+y**2-10*x+8*y-23).getRadius() == 8


def test_get_radius_and_center1():
    sph = Sphere(eq=x**2+y**2+14*x-2*y+1)
    c, r = sph.getCenter(), sph.getRadius()
    assert c == Point(-7, 1, 0) and r == 7


def test_get_radius_and_center2():
    sph = Sphere(eq=x**2+y**2-10*x+8*y-8)
    c, r = sph.getCenter(), sph.getRadius()
    assert c == Point(5, -4, 0) and r == 7

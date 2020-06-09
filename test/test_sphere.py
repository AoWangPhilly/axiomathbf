import pytest
from axiomathbf.Sphere import Sphere
from sympy import symbols

x,y,z = symbols("x y z")

def test_format_equation1():
    sphere1 = Sphere(eq=4*x**2 + 4*y**2 - 16*x - 24*y + 51)
    sphere2 = Sphere(eq=z**2 + (x - 2)**2 + (y - 3)**2 - 1/4)
    assert sphere1 == sphere2

def test_format_equation2():
    pass

def test_format_equation3():
    pass

def test_format_equation4():
    pass

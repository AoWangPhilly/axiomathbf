import pytest
from axiomathbf.Sphere import Sphere
from sympy import symbols

x,y,z = symbols("x y z")

def test_format_equation():
    sphere = Sphere(eq=4*x**2 + 4*y**2 - 16*x - 24*y + 51)
    assert str(sphere.getEquation()) == str(z**2 + (x + 2)**2 + (y + 3)**2 - 1/4)
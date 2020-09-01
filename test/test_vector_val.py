from axiomathbf.vector_value import VectorFunction
import pytest
import sympy

def test_domain():
    t = sympy.Symbol('t')
    v1 = [t**2, sympy.sqrt(1-t), -1/t]
    v2 = [sympy.ln(t+1), 1/(sympy.E^t-2), t]
    v3 = [sympy.cos(t), sympy.sin(t), 5]
    v4 = [sympy.ln(t), t+1, sympy.E^t]
    
def test_diff():
    pass

def test_integrate():
    pass
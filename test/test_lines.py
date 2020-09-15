from axiomathbf import ParametricLine
import sympy
from math import isclose


def test_compare():
    l1 = ParametricLine(point=[2, 1, 4], vector=[3, -2, 5])
    l2 = ParametricLine(point=[3, -2, -1], vector=[-6, 4, -10])

    l3 = ParametricLine(point=[1, 0, 2], vector=[0, 1, -1])
    l4 = ParametricLine(point=[2, 4, 0], vector=[3, -3, 1])

    l5 = ParametricLine(point=[1, 14, 5], vector=[-2, 1, -1])
    l6 = ParametricLine(point=[0, 4, 3], vector=[1, 3, 1])

    l7 = ParametricLine(point=[2, 4, 1], vector=[5, -1, 1])
    l8 = ParametricLine(point=[3, 1, 0], vector=[6, -1, 1])

    sols = ['Parallel', 'Skew', 'Perpendicular', 'Skew']
    for lines, sol in zip(((l1, l2), (l3, l4), (l5, l6), (l7, l8)), sols):
        assert lines[0].compare(lines[1]) == sol


def test_str():
    l1 = ParametricLine(point=[1, 3, 4], vector=[-3, -2, 3])
    l2 = ParametricLine(point=[4, -2, 0], vector=[-1, 5, -1])
    l3 = ParametricLine(point=[3, 1, 2], vector=[-2, 1, 1])
    sols = ['<x, y, z> = <1, 3, 4> + <-3, -2, 3>t',
            '<x, y, z> = <4, -2, 0> + <-1, 5, -1>t',
            '<x, y, z> = <3, 1, 2> + <-2, 1, 1>t']
    for line, sol in zip((l1, l2, l3), sols):
        assert str(line) == sol


def test_equal():
    l1 = ParametricLine(point=[3, 1, 2], vector=[-2, 1, 1])
    l2 = ParametricLine(point=[3, 1, 2], vector=[4, -2, -2])

    l3 = ParametricLine(point=[1, 3, 4], vector=[-3, -2, 3])
    l4 = ParametricLine(point=[1, 3, 4], vector=[-3, -2, 3])

    l5 = ParametricLine(point=[1, 2, -1], vector=[-1, 3, -2])
    l6 = ParametricLine(point=[3, 1, 0], vector=[4, -1, 1])
    sols = [True, True, False]
    for lines, sol in zip(((l1, l2), (l3, l4), (l5, l6)), sols):
        assert (lines[0] == lines[1]) == sol


def test_distance():
    l1 = ParametricLine(point=[5, 3, 0], vector=[3, 9, 0])
    l2 = ParametricLine(point=[1, 0, 1], vector=[1, 3, 0])

    l3, p1 = ParametricLine(
        point=[2, -4, 0], vector=[3, 1, -2]), sympy.Point([1, -6, 2])

    sols = [sympy.sqrt(91/10), sympy.sqrt(45/14)]
    for i, sol in zip(((l1, l2), (l3, p1)), sols):
        assert isclose(i[0].distance(i[1]), sol) == True


def test_intersect():
    l1 = ParametricLine(point=[1, 3, 5], vector=[2, 5, 2])
    l2 = ParametricLine(point=[0, 11, 4], vector=[1, -1, 1])
    
    l3 = ParametricLine(point=[2, 3, 1], vector=[4, 0, -1])
    l4 = ParametricLine(point=[2, 3, 1], vector=[2, 2, 1])
    sols = [[3, 8, 7], [2, 3, 1]]
    for i, sol in zip(((l1, l2), (l3, l4)), sols):
        assert i[0].intersect(i[1]) == sol

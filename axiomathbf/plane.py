'''
description: plane class
author: ao wang
date: 09/06/2020
'''

import sympy
from .parametric_lines import ParametricLine
from sympy.abc import x, y, z, t
from sympy import sqrt

class Plane():
    '''The plane class that can initalize with 3 points, a point and a normal vector, or equation

    Attributes
    ==========
        p1 (sympy.Point): the first point
        p2 (sympy.Point): the second point
        p3 (sympy.Point): the first point
        normal_vector (list): the normal vector
        eq (sympy.Add): the Plane equation
    '''

    def __init__(self, p1=None, p2=None, p3=None, normal_vector=None, eq=None):
        if p1 and p2 and p3:
            plane = sympy.Plane(p1, p2, p3)
        elif p1 and normal_vector:
            plane = sympy.Plane(p1, normal_vector=normal_vector)
        elif eq:
            x, y, z = sympy.symbols('x y z')

            eq = sympy.Poly(eq)
            # gets all the coeffients of each variable
            norm_vect = eq.coeffs()[:3]
            pointEq = sympy.solve(eq, x, y, z)[0]  # solves x,y,z to 0

            # Finds a point on the plane
            point = sympy.Point(
                [point.subs([(x, 0), (y, 0), (z, 0)]) for point in pointEq])
            plane = sympy.Plane(point, normal_vector=norm_vect)
        self.plane = plane

    def getPlane(self):
        return self.plane

    def setPlane(self, plane):
        self.plane = plane

    def angle(self, other):
        '''Finds the angle between a Plane and a Plane or a Plane and a ParametricLine

        Argument
        ========
            other (Plane or ParametricLine):
        

        Return
        ======


        '''
        if isinstance(other, Plane):
            return self.plane.angle_between(other.plane)
        elif isinstance(other, ParametricLine):
            l, m, n = other.vector
            a, b, c = self.plane.normal_vector
            return sympy.asin(sympy.abs(a*l + b*m + c*n)/(sympy.sqrt(a**2+b**2+c**2)*sympy.sqrt(l**2+m**2+n**2)))

    def compare(self, other):
        '''Returns whether a Plane or ParametricLine are parallel, perpendicular, or neither

        Arguments
        =========
            others

        Return
        ======
        
        '''
        if isinstance(other, Plane):
            if other.plane.is_perpendicular(self.plane):
                return 'Perpendicular'
            elif other.plane.is_parallel(self.plane):
                return 'Parallel'
            else:
                return 'Neither parallel or perpendicular'
        # check for parametric line too
        elif isinstance(other, ParametricLine):
            if sympy.Matrix(other.plane.normal_vector).dot(other.vector) == 0:
                return 'Parallel'
            elif (sympy.Matrix(other.plane.normal_vector).cross(other.vector)).norm() == 0:
                return 'Perpendicular'
            else:
                return 'Neither parallel or perpendicular'

    def distance(self, other):
        '''Returns the distance between Planes, Lines, and Points

        Arguments
        =========
            others

        Return
        ======
        
        '''
        selfEq = self.plane.equation.coeffs()
        a, b, c, d1 = selfEq
        if isinstance(other, Plane):
            otherEq = other.plane.equation.coeffs()
            d2 = otherEq[3]
            return abs(d2-d1)/(sqrt(a**2+b**2+c**2))
        elif isinstance(other, ParametricLine):
            p1, p2, p3 = other.getPoint()
            return abs(a*p1+b*p2+c*p3+d1)/(sqrt(a**2+b**2+c**2))
        elif isinstance(other, sympy.Point):
            p1, p2, p3 = other
            return abs(a*p1+b*p2+c*p3+d1)/(sqrt(a**2+b**2+c**2))

    def intersect(self, other):
        '''Returns where line or plane intersects


        Arguments
        =========
            others

        Return
        ======
        

        '''
        if isinstance(other, Plane):
            # Find directional vector
            d = sympy.Matrix(self.getPlane().normal_vector).cross(
                sympy.Matrix(other.getPlane().normal_vector))
            selfEq = sympy.Poly(self.plane.equation())
            otherEq = sympy.Poly(other.plane.equation())
            if len(selfEq.free_symbols) == 3 and len(otherEq.free_symbols) == 3:
                coeffSelf, coeffOther = selfEq.coeffs(), otherEq.coeffs()
                x1, y1, _, c1 = coeffSelf
                x2, y2, _, c2 = coeffOther
                a = sympy.Matrix([[x1, y1],
                                  [x2, y2]])
                b = sympy.Matrix([-c1, -c2])
                point = list(a.inv()*b)
                point.append(0)
                return ParametricLine(point=point, vector=d)
        elif isinstance(other, ParametricLine):
            lineEq = [
                pt + vec*t for (pt, vec) in zip(other.getPoint(), other.getVector())]
            xLine, yLine, zLine = lineEq
            tIntersect = sympy.solve(
                self.plane.equation(xLine, yLine, zLine), t)
            if tIntersect:
                return sympy.Point([elem.subs(t, tIntersect[0]) for elem in lineEq])


if __name__ == '__main__':
    x, y, z = sympy.symbols('x y z')
    # p1 = Plane(eq=5*x-3*y+4*z+1)
    # p2 = Plane(eq=2*x-2*y-4*z-9)
    # print(p1.plane.equation())
    # print(p2.plane.equation())
    # p3 = Plane(eq=x+y+z-7)
    # p4 = Plane(eq=2*x+4*z-6)
    # print(p3.intersect(p4))
    plane = Plane(eq=2*x+y-4*z-4)
    line = ParametricLine(point=[0, 2, 0], vector=[1, 3, 1])
    print(plane.intersect(line))

    p1 = Plane(eq=x-5*y+3*z-11)
    p2 = Plane(eq=-3*x+2*y-2*z+7)
    print(p1.intersect(p2))

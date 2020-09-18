'''
description: plane class
author: ao wang
date: 09/06/2020
'''

import sympy
from .parametric_lines import ParametricLine
from sympy.abc import x, y, z, t
from sympy import sqrt, asin, Matrix
from axiomathbf.environment import isnotebook
from IPython.display import display, Math


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
            # gets all the coeffients of each variable
            coeff_dict = eq.as_coefficients_dict()
            point_eq = sympy.solve(eq, x, y, z)[0]  # solves x, y, z to 0

            # Finds a point on the plane
            point = sympy.Point(
                [point.subs([(x, 0), (y, 0), (z, 0)]) for point in point_eq])
            plane = sympy.Plane(point, normal_vector=[coeff_dict.get(
                x, 0), coeff_dict.get(y, 0), coeff_dict.get(z, 0)])

        gcd = sympy.gcd(plane.normal_vector)
        plane = sympy.Plane(
            p1=plane.p1, normal_vector=[elem/gcd for elem in plane.normal_vector])
        self.plane = plane

    def __repr__(self):
        if isnotebook():
            display(Math(sympy.latex(self.plane.equation())))
            return ''
        return self.__str__()

    def __str__(self):
        return str(self.plane.equation())

    def __eq__(self, other):
        return self.plane.equation().equals(other.plane.equation())

    def get_plane(self):
        return self.plane

    def set_plane(self, plane):
        self.plane = plane

    def angle(self, other):
        '''Finds the angle between a Plane and a Plane or a Plane and a ParametricLine

        Argument
        ========
            other (Plane, ParametricLine): another 3D object

        Return
        ======
            sympy.Numbers: the angle between planes or a parametric line
        '''
        if isinstance(other, Plane):
            return self.plane.angle_between(other.plane)
        elif isinstance(other, ParametricLine):
            norm_vect, line_dir = Matrix(self.plane.normal_vector), other.vector
            return abs(asin(line_dir.dot(norm_vect)/(line_dir.norm()*norm_vect.norm())))

    def compare(self, other):
        '''Returns whether a Plane or ParametricLine are parallel, perpendicular, or neither

        Arguments
        =========
            other (Plane or ParametricLine): another 3D object

        Return
        ======
            str: whether the objects are perpendicular, parallel, or neither
        '''
        if isinstance(other, Plane):
            if other.plane.is_perpendicular(self.plane):
                return 'Perpendicular'
            elif other.plane.is_parallel(self.plane):
                return 'Parallel'
            else:
                return 'Neither parallel nor perpendicular'
        elif isinstance(other, ParametricLine):
            if sympy.Matrix(self.plane.normal_vector).dot(other.vector) == 0:
                return 'Parallel'
            elif (sympy.Matrix(self.plane.normal_vector).cross(other.vector)).norm() == 0:
                return 'Perpendicular'
            else:
                return 'Neither parallel nor perpendicular'

    def distance(self, other):
        '''Returns the distance between Planes, Lines, and Points

        Arguments
        =========
            other (Plane, ParametricLine, Point): another 3D object

        Return
        ======
            sympy.Numbers: returns distance between 3D objects
        '''

        if isinstance(other, Plane):
            return self.plane.distance(other.plane)
        elif isinstance(other, sympy.Point):
            return self.plane.distance(other)
        elif isinstance(other, ParametricLine):
            pq, norm_vect = Matrix(other.point-self.plane.p1), Matrix(self.plane.normal_vector)
            return abs(pq.dot(norm_vect))/norm_vect.norm()

    def intersect(self, other):
        '''Returns where line or plane intersects


        Arguments
        =========
            other (Plane or ParametricLine): another 3D object

        Return
        ======
            sympy.Point or ParametricLine: returns the point intersection of plane and
            line or paramatric line of intersection betweeen two planes

        '''
        if isinstance(other, Plane):
            line = other.plane.intersection(self.plane)[0]
            return ParametricLine(point=line.p1, vector=list(line.p1-line.p2))
        elif isinstance(other, ParametricLine):
            line_eq = [
                pt + vec*t for (pt, vec) in zip(other.get_point(), other.get_vector())]
            x_line, y_line, z_line = line_eq
            t_intersect = sympy.solve(
                self.plane.equation(x_line, y_line, z_line), t)
            if t_intersect:
                return sympy.Point([elem.subs(t, t_intersect[0]) for elem in line_eq])


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

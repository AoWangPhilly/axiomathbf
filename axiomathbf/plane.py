'''
description: plane class
author: ao wang
date: 09/06/2020
'''

import sympy
from IPython.display import Math, display
from sympy import Matrix, asin, sqrt
from sympy.abc import t, x, y, z

from axiomathbf.environment import isnotebook

from .parametric_lines import ParametricLine


class Plane():
    '''The plane class that can initalize with 3 points, a point and a normal vector, or equation.
    The class can also compare planes and lines to test if they are parallel, perpendicular, or skew,
    find points of intersection, and angle and distance between two 3D objects.

    :param p1: the first point
    :type p1: sympy.geometry.point.Point3D
    :param p2: the second point
    :type p2: sympy.geometry.point.Point3D
    :param p3: the third point
    :type p3: sympy.geometry.point.Point3D
    :param normal_vector: the normal vector
    :type normal_vector: list of ints
    :param eq: the plane equation
    :type eq: sympy.core.add.Add
    :param plane: the sympy plane object
    :type plane: sympy.geometry.plane.Plane
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
        '''Gets the plane class attribute

        :return: the plane class attribute
        :rtype: sympy.geometry.plane.Plane
        '''
        return self.plane

    def set_plane(self, plane):
        '''Sets the plane class attribute

        :param plane: the sympy plane object
        :type plane: sympy.geometry.plane.Plane
        '''
        self.plane = plane

    def angle(self, other):
        '''Calculates the angle between 3D objects (Plane, ParametricLine)

        :param other: another 3D object
        :type other: Plane or ParametricLine
        :return: the angle between two 3D objects
        :rtype: sympy.core.numbers.Floats
        '''
        if isinstance(other, Plane):
            return self.plane.angle_between(other.plane)
        elif isinstance(other, ParametricLine):
            norm_vect, line_dir = Matrix(
                self.plane.normal_vector), other.vector
            return abs(asin(line_dir.dot(norm_vect)/(line_dir.norm()*norm_vect.norm())))

    def compare(self, other):
        '''Finds whether a Plane or ParametricLine are parallel, perpendicular, or neither

        :param other: another 3D object
        :type other: Plane or ParametricLine
        :return: whether the objects are perpendicular, parallel, or neither
        :rtype: str
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

        :param other: another 3D object
        :type other: Plane, ParametricLine, or sympy.geometry.point.Point3D
        :return: the distance between 3D objects
        :rtype: sympy.core.numbers.Floats
        '''
        if isinstance(other, Plane):
            return self.plane.distance(other.plane)
        elif isinstance(other, sympy.Point):
            return self.plane.distance(other)
        elif isinstance(other, ParametricLine):
            pq, norm_vect = Matrix(
                other.point-self.plane.p1), Matrix(self.plane.normal_vector)
            return abs(pq.dot(norm_vect))/norm_vect.norm()

    def intersect(self, other):
        '''Calculates where the line or plane intersects

        :param other: another 3D object
        :type other: Plane or ParametricLine
        :return: returns the point intersection of plane and line or paramatric line of intersection betweeen two planes
        :rtype: sympy.geometry.point.Point3D or ParametricLine
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

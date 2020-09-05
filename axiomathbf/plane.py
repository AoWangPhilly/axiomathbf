'''

'''
import sympy
from parametric_lines import ParametricLine
from sympy.abc import x, y, z, t


class Plane():
    '''

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

    def compare(self, other):
        '''

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
            pass

    def intersect(self, other):
        '''


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
            return None
        elif isinstance(other, ParametricLine):
            lineEq = [
                pt + vec*t for (pt, vec) in zip(other.getPoint(), other.getVector())]
            xLine, yLine, zLine = lineEq
            tIntersect = sympy.solve(
                self.plane.equation(xLine, yLine, zLine), t)
            if tIntersect:
                return sympy.Point([elem.subs(t, tIntersect[0]) for elem in lineEq])
            else:
                return 'No intersection!'


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

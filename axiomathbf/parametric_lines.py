import sympy
from sympy.matrices import Matrix
from sympy.vector import CoordSys3D, matrix_to_vector


class ParametricLine():
    def __init__(self, point, vector):
        C = CoordSys3D('')

        self.point = sympy.Point(point)
        self.vector = Matrix(vector)

    def __str__(self):
        x, y, z = self.point
        v1, v2, v3 = self.vector
        return '<x, y, z> = <{}, {}, {}> + <{}, {}, {}>t'.format(x, y, z, v1, v2, v3)

    def getPoint(self):
        return self.point
    
    def setPoint(self, point):
        self.point = point

    def getVector(self):
        return self.vector

    def setVector(self, vector):
        self.vector = vector
        
    def compare(self, other):
        if isinstance(other, ParametricLine):
            if self.vector.dot(other.vector) == 0:
                symbol = 'Perpendicular'
            elif self.vector.cross(other.vector).norm() == 0:
                symbol = 'Parallel'
            else:
                symbol = 'Skew'
            return symbol


    def getPointVector(self):
        x, y, z = self.point
        v1, v2, v3 = self.vector
        return sympy.latex('$\\vec{\\ell(t)} = \\langle' + '{}, {}, {}'.format(x, y, z)
                           + '\\rangle +t \\langle ' + ' {}, {}, {}'.format(v1, v2, v3) + '\\rangle$')

    def intersect(self, other):
        x, y = sympy.symbols('x y')
        solutions = []
        for i in range(2):
            r1 = [self.vector[i], -other.vector[i], other.point[i]-self.point[i]]
            r2 = [self.vector[i+1], -other.vector[i+1], other.point[i+1]-self.point[i+1]]
            if r1 == r2: continue
            a = Matrix([r1, r2])
            solutions.append(sympy.solve_linear_system(a, x, y))

        a = Matrix([[self.vector[0], -other.vector[0], other.point[0]-self.point[0]],
                    [self.vector[2], -other.vector[2], other.point[2]-self.point[2]]])
        solutions.append(sympy.solve_linear_system(a, x, y))
        print(solutions)
        if solutions.count(solutions[0]) == 3:
            return list(solutions[0])
        return None


if __name__ == '__main__':
    # # Parallel
    pt1, vec1 = [5,-1,9], [-1,3,-1]
    pt2, vec2 = [3, -2, -1], [-6, 4, -10]
    # line1 = ParametricLine(pt1, vec1)
    # line2 = ParametricLine(pt2, vec2)
    l1 = sympy.Line(pt1, vec1)
    l2 = sympy.Line(pt2, vec2)
    print(l1.arbitrary_point())
    # # Skew
    # pt3, vec3 = [1, 0, 2], [0, 1, -1]
    # pt4, vec4 = [2, 4, 0], [3, -3, 1]
    # line3 = ParametricLine(pt3, vec3)
    # line4 = ParametricLine(pt4, vec4)

    # # Intersection at (x,y,z) = (3,13,6)
    # pt5, vec5 = [1, 14, 5], [-2, 1, -1]
    # pt6, vec6 = [0, 4, 3], [1, 3, 1]
    # line5 = ParametricLine(pt5, vec5)
    # line6 = ParametricLine(pt6, vec6)

    # # Skew
    # pt7, vec7 = [2, 4, 1], [5, -1, 1]
    # pt8, vec8 = [3, 1, 0], [6, -1, 1]
    # line7 = ParametricLine(pt7, vec7)
    # line8 = ParametricLine(pt8, vec8)

    # # Skew
    # pt9, vec9 = [1, 2, -1], [-1, 3, -2]
    # pt10, vec10 = [3, 1, 0], [4, -1, 0]
    # line9 = ParametricLine(pt9, vec9)
    # line10 = ParametricLine(pt10, vec10)

    # print(ParametricLine([1, 3, 5], [2, 5, 2]).intersect(
    #     ParametricLine([0, 11, 4], [1, -1, 1])))
    # print(line1.compare(line2))
    # print(line3.compare(line4))
    # print(line5.compare(line6))
    # print(line7.compare(line8))
    # print(line9.compare(line10))

import math


class Matrix():
    def __init__(self, i=0, j=0, k=0):
        self.matrix = [i, j, k]

    def dot(self, other):
        return sum([self.matrix[idx]*other[idx] for idx in range(3)])

    def cross(self, other):
        i = self.matrix[1]*other[2] - self.matrix[2]*other[1]
        j = -(self.matrix[0]*other[2] - self.matrix[2]*other[0])
        k = self.matrix[0]*other[1] - self.matrix[1]*other[0]
        return Matrix(i, j, k)

    def _det(self):
        pass

    def _vstack(self, other):
        pass

    def _section2by2(self):
        pass

    def norm(self):
        return math.sqrt(sum([unit**2 for unit in self.matrix]))

    def normalize(self):
        normalized = [unit/norm for unit in self.matrix]
        return Matrix(normalized[0], normalized[1], normalized[2])

    def getMatrix(self):
        return self.matrix

    def setMatrix(self, matrix):
        self.matrix = matrix

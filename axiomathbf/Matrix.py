import math


class Matrix():
    def __init__(self, i=0, j=0, k=0):
        self.matrix = [i, j, k]

    def __str__(self):
        return str(self.getMatrix())

    def __add__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            m = [unit+other for unit in self.matrix]
        if isinstance(other, Matrix):
            m = [self.matrix[idx]+other[idx] for idx in range(3)]
        return Matrix(m[0], m[1], m[2])

    def __sub__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            m = [unit-other for unit in self.matrix]
        if isinstance(other, Matrix):
            m = [self.matrix[idx]-other[idx] for idx in range(3)]
        return Matrix(m[0], m[1], m[2])

    def __floordiv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            m = [unit//other for unit in self.matrix]
        if isinstance(other, Matrix):
            m = [self.matrix[idx]//other[idx] for idx in range(3)]
        return Matrix(m[0], m[1], m[2])

    def __truediv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            m = [unit/other for unit in self.matrix]
        if isinstance(other, Matrix):
            m = [self.matrix[idx]/other[idx] for idx in range(3)]
        return Matrix(m[0], m[1], m[2])

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            m = [unit*other for unit in self.matrix]
        if isinstance(other, Matrix):
            m = [self.matrix[idx]*other[idx] for idx in range(3)]
        return Matrix(m[0], m[1], m[2])
    
    def __mod__(self, other):
        if isinstance(other, int):
            m = [unit%other for unit in self.matrix]
        if isinstance(other, Matrix):
            m = [self.matrix[idx]%other[idx] for idx in range(3)]
        return Matrix(m[0], m[1], m[2])

    def __getitem__(self, index):
        return self.matrix[index]

    def __len__(self):
        return len(self.matrix)

    def dot(self, other):
        return sum([self.matrix[idx]*other[idx] for idx in range(3)])

    def cross(self, other):
        i = self. _det(other, 1, 2)
        j = -self. _det(other, 0, 2)
        k = self. _det(other, 0, 1)
        return Matrix(i, j, k)

    def _det(self, other, col1, col2):
        sqrMatrix = self._section2by2(other, col1, col2)
        return sqrMatrix[0][0]*sqrMatrix[1][1] - sqrMatrix[0][1]*sqrMatrix[1][0]

    def _vstack(self, other):
        return [self.matrix, other]

    def _section2by2(self, other, col1, col2):
        twoByTwo = []
        vstack = self._vstack(other)
        for row in vstack:
            twoByTwo.append([row[col1], row[col2]])
        return twoByTwo

    def norm(self):
        return math.sqrt(sum([unit**2 for unit in self.matrix]))

    def normalize(self):
        normalized = [unit/norm for unit in self.matrix]
        return Matrix(normalized[0], normalized[1], normalized[2])

    def getMatrix(self):
        return self.matrix

    def setMatrix(self, matrix):
        self.matrix = matrix


if __name__ == "__main__":
    u = Matrix(1, 2, 3)
    v = Matrix(4, 5, 6)
    print(u%2)

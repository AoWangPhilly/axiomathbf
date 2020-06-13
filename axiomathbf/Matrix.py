import math
from sympy import simplify, diff, latex, sqrt, Rational
from IPython.display import display, Math


class MatrixBase():
    def __init__(self, i=0, j=0, k=0):
        self.matrix = [i, j, k]

    def __str__(self):
        return str(self.getMatrixBase())

    def _repr_pretty_(self, p, cycle):
        i, j, k = self.matrix
        return p.text(self.__str__()) if cycle else display(Math('\\left[\\begin{matrix}' + '{}\\\\{}\\\\{}\\end'.format(i, j, k) + '{matrix}\\right]'))

    def _dunderHelper(self, other, operator):
        if isinstance(other, MatrixBase):
            m = eval('[{0}[idx]{1}{2}[idx] for idx in range(3)]'.format(
                self.matrix, operator, other))
        if isinstance(other, (int, float)):
            m = eval('[unit{0}{1} for unit in self.matrix]'.format(
                operator, other))
        return MatrixBase(m[0], m[1], m[2])

    def __add__(self, other):
        return self._dunderHelper(other, '+')

    def __sub__(self, other):
        return self._dunderHelper(other, '-')

    def __floordiv__(self, other):
        return self._dunderHelper(other, '//')

    def __truediv__(self, other):
        return self._dunderHelper(other, '/')

    def __mul__(self, other):
        return self._dunderHelper(other, '*')

    def __mod__(self, other):
        return self._dunderHelper(other, '%')

    def __getitem__(self, index):
        return self.matrix[index]

    def __len__(self):
        return len(self.matrix)

    def dot(self, other):
        return sum([self.matrix[idx]*other[idx] for idx in range(3)])

    def cross(self, other):
        i = self._det(other, 1, 2)
        j = -self._det(other, 0, 2)
        k = self._det(other, 0, 1)
        return MatrixBase(i, j, k)

    def _det(self, other, col1, col2):
        sqrMatrixBase = self._section2by2(other, col1, col2)
        return sqrMatrixBase[0][0]*sqrMatrixBase[1][1] - sqrMatrixBase[0][1]*sqrMatrixBase[1][0]

    def _vstack(self, other):
        return [self.matrix, other]

    def _section2by2(self, other, col1, col2):
        return [[row[col1], row[col2]] for row in self._vstack(other)]

    def norm(self):
        return sqrt(sum([unit**2 for unit in self.matrix]))

    def normalize(self):
        normalized = [unit/self.norm() for unit in self.matrix]
        return MatrixBase(normalized[0], normalized[1], normalized[2])

    def getJacobian(self, respect):
        matrix = []
        for i in self.matrix:
            arr = []
            for j in respect:
                arr.append(diff(i, j))
                matrix.append(arr)
        return simplify(MatrixBase(matrix).det())

    def getMatrixBase(self):
        return self.matrix

    def setMatrixBase(self, matrix):
        self.matrix = matrix


if __name__ == "__main__":
    u = MatrixBase(1, 2, 3)
    v = MatrixBase(4, 5, 6)
    u += 2
    print(u+v)

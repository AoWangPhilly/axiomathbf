"""
Program: Matrix.py
Purpose: A module to solve simple Matrix related problems, mainly used for the Vector class. I also had trouble inheriting 
from Sympy's MatrixBase class for the Vector class, so I decided to create my own, plus it'd be great to practice my OOP skills. 
Author: Ao Wang
Date: June 13, 2020
"""

import math
from sympy import simplify, diff, latex, sqrt, Rational, Integer, Pow
from IPython.display import display, Math


class Matrix():
    """The Matrix class creates a 1 by 3 matrix object that displays in Latex on Jupyter Notebook and array in print. 
       It also does simple matrix operations, like dot and cross product, normalization, and addition with matrices 
       and integers. 

    :param i: The i component of the unit vector
    :type i: int
    :param j: The j component of the unit vector
    :type j: int
    :param k: The k component of the unit vector
    :type k: int
    """

    def __init__(self, i=0, j=0, k=0):
        self.matrix = [i, j, k]

    def __str__(self):
        """Overriding the str method to show the Matrix when printing

        :returns: The string representation of the Matrix
        :rtype: str
        """
        return str(self.getMatrix())

    def _repr_pretty_(self, p, cycle):
        """Displays the matrix in Latex in Jupyter notebook

        Note:
        To learn more about _repr_pretty_ go to https://ipython.readthedocs.io/en/stable/api/generated/IPython.lib.pretty.html
        """
        i, j, k = self.matrix
        return p.text(self.__str__()) if cycle else display(Math('\\left[\\begin{matrix}' + '{}\\\\{}\\\\{}\\end'.format(i, j, k) + '{matrix}\\right]'))

    def _dunderHelper(self, other, operator):
        """A helper function to make the magic/dunder methods more concise

        :param other: The other object 
        :type other: The integer or Matrix object
        :param operator: The math operator
        :type operator: str
        :returns: The Matrix object
        :rtype: Matrix
        """
        if isinstance(other, Matrix):
            m = eval('[{0}[idx]{1}{2}[idx] for idx in range(3)]'.format(
                self.matrix, operator, other.matrix))
        if isinstance(other, (int, float, Rational, Integer, Pow)):
            m = eval('[unit{0}{1} for unit in self.matrix]'.format(
                operator, other))
        return Matrix(m[0], m[1], m[2])

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

    def __pow__(self, other):
        return self._dunderHelper(other, '**')

    def __radd__(self, other):
        return self._dunderHelper(other, '+')

    def __rsub__(self, other):
        return self._dunderHelper(other, '-')

    def __rfloordiv__(self, other):
        return self._dunderHelper(other, '//')

    def __rtruediv__(self, other):
        return self._dunderHelper(other, '/')

    def __rmul__(self, other):
        return self._dunderHelper(other, '*')

    def __rmod__(self, other):
        return self._dunderHelper(other, '%')

    def __rpow__(self, other):
        return self._dunderHelper(other, '**')

    def __getitem__(self, index):
        return self.matrix[index]

    def __len__(self):
        return len(self.matrix)

    def __neg__(self):
        m = [-unit for unit in self.matrix]
        return Matrix(m[0], m[1], m[2])

    def __abs__(self):
        m = [abs(unit) for unit in self.matrix]
        return Matrix(m[0], m[1], m[2])

    def __round__(self, n):
        m = [round(unit, n) for unit in self.matrix]
        return Matrix(m[0], m[1], m[2])

    def __floor__(self):
        m = [math.floor(unit) for unit in self.matrix]
        return Matrix(m[0], m[1], m[2])

    def __ceil__(self):
        m = [math.ceil(unit) for unit in self.matrix]
        return Matrix(m[0], m[1], m[2])

    def dot(self, other):
        """The dot product operation 

        :param other: Another Matrix object
        :type other: Matrix
        :returns: The dot product
        :rtype: int
        """
        return sum([self.matrix[idx]*other[idx] for idx in range(3)])

    def cross(self, other):
        """The cross product operation

        :param other: Another Matrix object
        :type other: Matrix
        :returns: The cross product
        :rtype: Matrix
        """
        i = self._det(other, 1, 2)
        j = -self._det(other, 0, 2)
        k = self._det(other, 0, 1)
        return Matrix(i, j, k)

    def _det(self, other, col1, col2):
        """Finds the determinant of a two by two matrix for the cross product

        :param other: Another list
        :type other: list
        :param col1: The first column to pull
        :type col1: int
        :param col2: The second column to pull
        :type col2: int
        :returns: The determinant
        :rtype: int
        """
        sqrMatrix = self._section2by2(other, col1, col2)
        return sqrMatrix[0][0]*sqrMatrix[1][1] - sqrMatrix[0][1]*sqrMatrix[1][0]

    def _vstack(self, other):
        """Vertically stacks two lists, used as a helper method for the section2by2 method

        :param other: Another list
        :type other: list
        :returns: Vertically stacked list
        :rtype: list
        """

        return [self.matrix, other]

    def _section2by2(self, other, col1, col2):
        """Creates a 2 by 2 two dimensional array, and a helper method for the det method

        :param other: Another list
        :type other: list
        :param col1: The first column to pull
        :type col1: int
        :param col2: The second column to pull
        :type col2: int
        :returns: The two by two array
        :rtype: list
        """
        return [[row[col1], row[col2]] for row in self._vstack(other)]

    def norm(self):
        """Returns the norm of the Matrix

        :returns: The norm of the Matrix
        :rtype: int
        """
        return sqrt(sum([unit**2 for unit in self.matrix]))

    def normalize(self):
        """Normalizes the Matrix

        :returns: The normalized Matrix
        :rtype: Matrix
        """
        normalized = [unit/self.norm() for unit in self.matrix]
        return Matrix(normalized[0], normalized[1], normalized[2])

    def getMatrix(self):
        return self.matrix

    def setMatrix(self, matrix):
        self.matrix = matrix


if __name__ == "__main__":
    u = Matrix(1, 2, 3)
    v = Matrix(4, 5, 6)
    u += 2
    print(u+v)
    print(u.cross(v))

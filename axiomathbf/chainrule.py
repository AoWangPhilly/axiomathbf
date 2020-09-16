'''
description: chain rule class
author: ao wang
date: 09/12/2020
'''

import sympy
from sympy.abc import x, y, z, w, r, s, t
from IPython.display import display, Math
import re


class ChainRule():
    '''Chain rule class that shows the equation and format for deriving chain rule

    Attributes
    ==========
        kwargs: the function example of tuples

    Example
    =======
        c1 = ChainRule(f=(x, y, z, w), x=(r, s, t), y=(r, t), z=(r, s), w=(s, t))
    '''

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(self.__dict__)

    def __make_diff(self, top, bot):
        '''Helper method that returns the partial derivative symbol

        Return
        ======
            str: returns the string format for partial derivative
        '''
        return '∂{}/∂{}'.format(top, bot)

    def get_equation(self, diff):
        '''Gets the equation with partial derivatives

        Parameter
        =========
            diff (str): the derivative, i.e. dz/dt

        Return
        ======
            str: the chain rule formula
        '''
        diff = diff.split('/')
        root, leaf = diff[0][1], diff[1][1]
        eq = []
        for branch in self.__dict__[root]:
            for var in self.__dict__[str(branch)]:
                if str(var) == leaf:
                    eq.append([self.__make_diff(root, branch),
                               self.__make_diff(branch, var)])
        return ' + '.join([' * '.join(i) for i in eq])

    def get_latex_equation(self, diff):
        '''Gets the equation with partial derivatives

        Parameter
        =========
            diff (str): the derivative, i.e. dz/dt

        Return
        ======
            str: the chain rule formula in latex code
        '''
        match = '∂.\/∂.'
        eq = self.get_equation(diff)
        partials = re.findall(match, eq)
        for p in partials:
            diff = p.split('/')
            root, leaf = diff[0][1], diff[1][1]
            eq = eq.replace(p, ('\\frac{' + '\\partial {}'.format(
                root) + '}{' + '\\partial {}'.format(leaf) + '}'))

        eq = eq.replace(' * ', '')
        return sympy.latex('${}$'.format(eq))

    def solve(self, diff, **kwargs):
        '''Finds the differientation given the functions and apply chain rule

        Parameters
        ==========
            diff (str): the derivative, i.e. dz/dt
            kwargs: the list of functions

        Return
        ======
            sympy.core.add.Add: the chainrule equation

        Example
        =======
            c3 = ChainRule()
            print(c3.solve('dz/dt', z=2*x-y, x=sympy.sin(t), y=3*t))
        '''
        diff = diff.split('/')
        root, leaf = diff[0][1], diff[1][1]
        top = kwargs[root]
        kwargs.pop(root, None)
        top = top.subs(kwargs)
        return sympy.diff(top, sympy.Symbol(leaf))


if __name__ == '__main__':
    c1 = ChainRule(f=(x, y, z, w), x=(r, s, t), y=(r, t), z=(r, s), w=(s, t))
    print(c1)
    # ∂f/∂x * ∂x/∂r + ∂f/∂y * ∂y/∂r + ∂f/∂z * ∂z/∂r
    print(c1.get_equation('df/dr'))
    # ∂f/∂x * ∂x/∂s + ∂f/∂z * ∂z/∂s + ∂f/∂w * ∂w/∂s
    print(c1.get_equation('df/ds'))
    # ∂f/∂x * ∂x/∂t + ∂f/∂y * ∂y/∂t + ∂f/∂w * ∂w/∂t
    print(c1.get_equation('df/dt'))

    c2 = ChainRule(z=(x, y), x=(t,), y=(t,))
    print(c2)
    print(c2.get_equation('dz/dt'))  # ∂z/∂x * ∂x/∂t + ∂z/∂y * ∂y/∂t
    # sympy.preview(c1.get_latex_equation('df/dr'),
    #               viewer='file', filename='oo1.png')
    # sympy.preview(c2.get_latex_equation('dz/dt'),
    #               viewer='file', filename='oo2.png')

    c3 = ChainRule()
    print(c3.solve('dz/dt', z=2*x-y, x=sympy.sin(t), y=3*t))

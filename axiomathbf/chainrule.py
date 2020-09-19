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
    '''The class is able to compute chain rule based on find the partial derivatives
    given the multivariable functions and also explicitly defined functions.
    
    Here's an example: c1 = ChainRule(f=(x, y, z, w), x=(r, s, t), y=(r, t), z=(r, s), w=(s, t)).

    :param kwargs: the explicit defned functions
    :type kwargs: tuples of sympy.core.symbol.Symbol
    '''

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(self.__dict__)

    def __make_diff(self, top, bot):
        '''Helper method that returns the partial derivative symbol

        :param top: the numerator of the partial derivative
        :type top: str
        :param bot: the denominator of the partial derivative
        :return: the string format for partial derivative
        :rtype: str
        '''
        return '∂{}/∂{}'.format(top, bot)

    def get_equation(self, diff):
        '''Calculates the formula for chain rule given the explicit functions 
        and differientiation

        :param diff: the derivative, i.e. dz/dt
        :type diff: str
        :return: the chain rule formula
        :rtype: str
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
        '''Calculates the formula for chain rule given the explicit functions 
        and differientiation and formats for LaTeX

        :param diff: the derivative, i.e. dz/dt
        :type diff: str
        :return: the chain rule formula in LaTeX
        :rtype: str
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
        '''Calculates the chain rule given the differientation and sympy functions
        Here's an example: c1 = ChainRule(); print(c1.solve('dz/dt', z=2*x-y, x=sympy.sin(t), y=3*t))

        :param diff: the derivative, i.e. dz/dt
        :type diff: str
        :param kwargs: multivariate functions (sympy.core.add.Add)
        :type kwargs: sympy.core.add.Add
        :return: the chainrule equation
        :rtype: sympy.core.add.Add
        '''
        diff = diff.split('/')
        root, leaf = diff[0][1], diff[1][1]
        top = kwargs[root]
        kwargs.pop(root, None)
        top = top.subs(kwargs)
        return sympy.diff(top, sympy.Symbol(leaf))


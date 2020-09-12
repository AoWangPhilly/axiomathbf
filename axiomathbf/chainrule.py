import sympy
from sympy.abc import x, y, z, w, r, s, t


class ChainRule():
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __str__(self):
        return str(self.__dict__)

    def __make_diff(self, top, bot):
        return '∂{}/∂{}'.format(top, bot)

    def get_equation(self, diff):
        diff = diff.split('/')
        root, leaf = diff[0][1], diff[1][1]
        eq = []
        for branch in self.__dict__[root]:
            for var in self.__dict__[str(branch)]:
                if str(var) == leaf:
                    eq.append([self.__make_diff(root, branch), self.__make_diff(branch, var)])
        return ' + '.join([' * '.join(i) for i in eq])

    def get_latex_equation(self, diff):
        pass

    def get_latex_tree(self):
        pass


if __name__ == '__main__':
    c1 = ChainRule(f=(x, y, z, w), x=(r, s, t), y=(r, t), z=(r, s), w=(s, t))
    print(c1)
    print(c1.get_equation('df/dr')) # ∂f/∂x * ∂x/∂r + ∂f/∂y * ∂y/∂r + ∂f/∂z * ∂z/∂r
    print(c1.get_equation('df/ds')) # ∂f/∂x * ∂x/∂s + ∂f/∂z * ∂z/∂s + ∂f/∂w * ∂w/∂s
    print(c1.get_equation('df/dt')) # ∂f/∂x * ∂x/∂t + ∂f/∂y * ∂y/∂t + ∂f/∂w * ∂w/∂t

    c2 = ChainRule(z=(x,y), x=(t,), y=(t,))
    print(c2)
    print(c2.get_equation('dz/dt')) # ∂z/∂x * ∂x/∂t + ∂z/∂y * ∂y/∂t

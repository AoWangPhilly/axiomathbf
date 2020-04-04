from sympy import *
from sympy.vector import CoordSys3D
from sympy.geometry import Point
from sympy.calculus.util import continuous_domain
from sympy.parsing.sympy_parser import parse_expr
import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

"""Multivariate Calculus Homework Problem Aid
The module is used to aid students in Multivariate Calculus (Math 200). However, the module should not be used as a crutch.
Many functions were created to solve problems from the Early Transcendental (Anton, Bivens, Davis) textbook. Additionally, the
module used many of the sympy and matplotlib, along with the numpy libraries to solve problems from chapter 11 to 14. """
x, y, z = symbols("x y z")


# 11.1
def simplify_sphere(f, info=False):
    """Returns the general equation of the sphere (x-a)**2 + (y-b)**2 + (z-c)**2 - r**2 = 0. 
       
    Example
    ========
    >>> from axiomathbf.multivariate_calculus import *
    >>> simplify_sphere(x ** 2 + y ** 2 + z ** 2 - 2 * x - 4 * y + 8 * z + 17) 
    (x - 1.0)**2 + (y - 2.0)**2 + (z + 4.0)**2 - 4.0
    :param f (sympy.core.add.Add): The unclean sphere function.
    :param info=False (bool): Prints the center and radius of the sphere if True.
    :return sympy.core.add.Add: The function of the sphere formula format.
    """
    f = simplify(f)
    f = str(f).replace(" ", "")
    var = ["x", "y", "z"]
    var_const = []
    constant = (
        int(f[f.find("z**2") + 5:])
        if f.find("z", f.find("z**2") + 1) == -1
        else int(f[f.find("z", f.find("z**2") + 1) + 1:])
    )
    for i in var:
        var_const.append(
            0
            if f.find(i, f.find(i + "**2") + 3) == -1
            else int(f[f.find(i + "**2") + 4: f.find(i, f.find(i + "**2") + 3) - 1])
        )
    for i in range(3):
        constant -= (var_const[i] / 2) ** 2
    eq = "(x+{})**2+(y+{})**2+(z+{})**2+{}".format(
        var_const[0] / 2, var_const[1] / 2, var_const[2] / 2, constant
    )
    if info:
        print("Center: " + str([(-1 * i / 2) for i in var_const]))
        print("Radius: " + str(sqrt(constant * -1)))
    return parse_expr(eq, evaluate=False)


# 11.2
def make_vector(x, y, z=0):
    """The method can create up to 3 dimensional vectors.
    
    Example
    =======
    >>> from axiomathbf.multivariate_calculus import *
    >>> make_vector(1,2,3)
    Matrix([[1, 2, 3]])
    :param x (int): The x coordinate.
    :param y (int): The y coordinate.
    :param z (int): The z coordinate.
    :return sympy.matrices.dense.MutableDenseMatrix: A matrix object.
    """
    return Matrix([[x, y, z]])


def point_to_point_vector(p1, p2):
    """Creates a vector from two separate points.
    
    Example
    =======
    >>> from axiomathbf.multivariate_calculus import *
    >>> point_to_point_vector(Point(2,3,6), Point(3,2,4))
    Matrix([[1, -1, -2]])
    :param p1 (sympy.geometry.point.Point3D): The first point.
    :param p2 (sympy.geometry.point.Point3D): The second point.
    :return sympy.matrices.dense.MutableDenseMatrix: A matrix object.
    """
    vec = p2-p1
    return r'\langle {},{},{}\rangle'.format(vec.x, vec.y, vec.z)


# 11.3
def angle_between_vectors(u, v):
    """Returns the angle between two vectors.
    
    Example
    =======
    >>> from axiomathbf.multivariate_calculus import * 
    >>> angle_between_vectors(make_vector(1,2,3), make_vector(5,3,2))
    acos(17*sqrt(133)/266)
    :param u (sympy.matrices.dense.MutableDenseMatrix): The first vector.
    :param v (sympy.matrices.dense.MutableDenseMatrix): The second vector.
    :return acos: The angle between the two vectors.
    """
    return latex(acos(u.dot(v) / (u.norm() * v.norm())))


def directional_cosine(v):
    """Returns the cosines of angles that the vector forms with the coordinate axes.
    
    Example
    =======
    >>> from axiomathbf.multivariate_calculus import *
    >>> directional_cosine(make_vector(1,2,3))
    {'α': acos(sqrt(14)/14), 'β': acos(sqrt(14)/7), 'γ': acos(3*sqrt(14)/14)}
    :param v (sympy.matrices.dense.MutableDenseMatrix): A vector.
    :return dict: A dictionary of the alpha, beta, gamma angles.
    """
    direction_cos = {}
    for index, angle in enumerate(("α", "β", "γ")):
        direction_cos[angle] = acos(v[index] / v.norm())
    return direction_cos


def projection(u, v):
    """Returns the vector projection of the vector u on v.
    
    Example
    =======
    >>> from axiomathbf.multivariate_calculus import *
    >>> projection(make_vector(1,2,3), make_vector(-2,4,-1))
    Matrix([[-2/7, 4/7, -1/7]])
    
    :param u (sympy.matrices.dense.MutableDenseMatrix): The first vector.
    :param v (sympy.matrices.dense.MutableDenseMatrix): The second vector.
    :return sympy.matrices.dense.MutableDenseMatrix: The projection vector of u onto v.
    """
    return (u.dot(v) / v.norm() ** 2) * v


def distance_from_point_to_line(pt, line1, line2):
    """Returns the distance between a point to line.
    
    Example
    =======
    >>> from axiomathbf.multivariate_calculus import *
    >>> distance_from_point_to_line(Point(5,3,0), Point(1,0,1), Point(2,3,1))
    sqrt(910)/10
    
    :param pt (sympy.geometry.point.Point3D): The point away from the line.
    :param line1 (sympy.geometry.point.Point3D): The first point on the line.
    :param line2 (sympy.geometry.point.Point3D): The second point on the line.
    :return sympy.core.mul.Mul: The distance between the point to line.
    
    Notes
    =====
    Other methods to find the distance can be found:
    https://www.qc.edu.hk/math/Advanced%20Level/Point_to_line.htm
    """
    ptline1 = point_to_point_vector(pt, line1)
    line1line2 = point_to_point_vector(line1, line2)
    ptline1_on_line1line2 = projection(ptline1, line1line2)
    return (ptline1 - ptline1_on_line1line2).norm()


# 11.4
def cross_area(u, v):
    """Returns the area formed by two vectors.
    
    Example
    =======
    >>> from axiomathbf.multivariate_calculus import *
    >>> cross_area(make_vector(3,4,0), make_vector(-1, 3, -2))
    sqrt(269)

    :param u (sympy.matrices.dense.MutableDenseMatrix): The first vector.
    :param v (sympy.matrices.dense.MutableDenseMatrix): The second vector.
    :return sympy.core.power.Pow: The area formed by the two vectors.
    """
    return u.cross(v).norm()


def parallelpiped_volume(u, v, w):
    """Returns the volume of a parallelpiped.
    
    Example
    =======
    >>> from axiomathbf.multivariate_calculus import *
    >>> parallelpiped_volume(make_vector(1,2,3), make_vector(3,4,0), make_vector(-1, 3, -2))
    43

    :param u (sympy.matrices.dense.MutableDenseMatrix): The first vector.
    :param v (sympy.matrices.dense.MutableDenseMatrix): The second vector.
    :param w (sympy.matrices.dense.MutableDenseMatrix): The third vector.
    :return sympy.core.numbers.Integer: The volume of the parallelpiped.
    """
    return abs(u.dot(v.cross(w)))


# 11.5
def point_vector_line(p, v):
    """Returns a parametric line given a point and a vector.
    
    Example
    =======
    >>> from axiomathbf.multivariate_calculus import*
    >>> point_vector_line(Point(1,0,-1), make_vector(1,-2,0))
    <x,y,z> = <1,0,-1> + <1,-2,0>t

    :param p (sympy.geometry.point.Point3D): A point.
    :param v (sympy.matrices.dense.MutableDenseMatrix): A vector.
    :return str: The parametric line.
    """
    return "<x,y,z> = <{},{},{}> + <{},{},{}>t".format(p.x, p.y, p.z, v[0], v[1], v[2])


def point_to_point_line(p1, p2):
    """Returns a parametric line given two points.
    
    Example
    =======
    >>> from axiomathbf.multivariate_calculus import*
    >>> point_to_point_line(Point(3,-6,6), Point(2,0,7))
    <x,y,z> = <3,-6,6> + <-1,6,1>t

    :param p1 (sympy.geometry.point.Point3D): The first point.
    :param p2 (sympy.geometry.point.Point3D): The second point.
    :return str: The parametric line.
    """
    v = point_to_point_vector(p1, p2)
    return point_vector_line(p1, v)


def compare_lines(g1, g2):
    """Compares two lines to determine whether they are perpendicular, parallel, or skew.
    
    Example
    =======
    >>> from axiomathbf.multivariate_calculus import *
    >>> compare_lines(make_vector(3,-2,5), make_vector(-6,4,-10))
    Matrix([[3, -2, 5]]) and Matrix([[-6, 4, -10]]): Parallel
    
    :param g1 (sympy.matrices.dense.MutableDenseMatrix): The first vector of the line.
    :param g2 (sympy.matrices.dense.MutableDenseMatrix): The second vector of the line.
    :return str: The result of comparing the two lines.
    
    Notes
    =====
    The function can also be used to determine if two planes are perpendicular, parallel, or skew.
    """
    result = ""
    if g1.dot(g2) == 0:
        result = "Perpendicular"
    elif g1.cross(g2).norm() == 0:
        result = "Parallel"
    else:
        result = "Skew"
    return str(g1) + " and " + str(g2) + ": " + result


# 11.6
def make_plane(p, n):
    """Forming a plane from a line and a normal vector.
    
    Example
    =======
    >>> from axiomathbf.multivariate_calculus import *
    >>> make_plane(Point(1,2,3), make_vector(4,-2,6))
    4*x - 2*y + 6*z - 18
    
    :param p (sympy.geometry.point.Point3D): A point the plane passes through.
    :param n (sympy.matrices.dense.MutableDenseMatrix): A normal vector.
    :return sympy.core.add.Add: The plane function simplfied.
    """
    return n[0] * (x - p.x) + n[1] * (y - p.y) + n[2] * (z - p.z)


def three_point_plane(p1, p2, p3):
    """Forming a plane from three points.
    
    Example
    =======
    >>> from axiomathbf.multivariate_calculus import *
    >>> three_point_plane(Point(1,2,3), Point(2,-1,5), Point(-1,3,3))
    -2*x - 4*y - 5*z + 25
    
    :param p1 (sympy.geometry.point.Point3D): The first point.
    :param p2 (sympy.geometry.point.Point3D): The second point.
    :param p3 (sympy.geometry.point.Point3D): The third point.
    :return sympy.core.add.Add: The plane function simplfied.
    """
    p1p2 = point_to_point_vector(p1, p2)
    p1p3 = point_to_point_vector(p1, p3)
    ortho = p1p2.cross(p1p3)
    return make_plane(p1, ortho)


def distance_from_point_to_plane(p, g, c):
    """Returns the distance from a point and a plane.
    
    Example
    =======
    >>> from axiomathbf.multivariate_calculus import *
    >>> distance_from_point_to_plane(Point(2,-1,4), make_vector(1,2,3), -5)
    sqrt(14)/2
    
    :param p (sympy.geometry.point.Point3D): The point away from the plane.
    :param g (sympy.matrices.dense.MutableDenseMatrix): The vector of the plane.
    :param c (int): The constant of the plane.
    :return sympy.core.mul.Mul: The distance of the point to the plane.
        
    Notes
    =====
    The constant is in the form of the plane given: Ax + By + Cz - D = 0.
    Additionally, there are definitely other formulas that give the distance 
    from a point to plane. 
    """
    return abs(p.x * g[0] + p.y * g[1] + p.z * g[2] + c) / g.norm()


# 11.7
def draw_ellipsoid():
    """Draws an ellipsoid. 
    
    Example
    =======
    >>> from axiomathbf.multivariate_calculus import *
    >>> draw_ellipoid()
    **Displays image

    Note
    ====
    Formula: x**2/a**2 + y**2/b**2 + z**2/c**2 = 1
    Best to use Jupyter Notebook to display the image.
    The method uses spherical coordinates to form the image. 
    """
    fig = plt.figure(figsize=plt.figaspect(1))
    ax = plt.axes(projection="3d")
    theta = np.linspace(0, 2 * np.pi, 100)
    phi = np.linspace(0, np.pi, 100)
    T, P = np.meshgrid(theta, phi)
    Z = np.cos(P)
    X, Y = np.sin(P) * np.cos(T), np.sin(P) * np.sin(T)
    ax.plot_surface(X, Y, Z, cmap=plt.cm.YlGnBu_r)
    plt.title("Ellipsoid")
    plt.show()


def draw_elliptic_cone():
    """ Draws an elliptic cone.

    Example
    =======
    >>> from axiomathbf.multivariate_calculus import *
    >>> draw_elliptic_cone()
    **Displays image
      
    Note
    ====
    Formula: z**2 - x**2/a**2 - y**2/b**2 = 0
    Best to use Jupyter Notebook to display the image.
    """
    fig = plt.figure(figsize=plt.figaspect(1))
    ax = plt.axes(projection="3d")
    x, y = np.linspace(-1, 1, 100), np.linspace(-1, 1, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.sqrt(X ** 2 + Y ** 2)
    ax.plot_surface(X, Y, Z, cmap=plt.cm.YlGnBu_r)
    ax.plot_surface(X, Y, -Z, cmap=plt.cm.YlGnBu_r)
    plt.title("Elliptic Cone")
    plt.show()


def draw_hyperboloid_one_sheet():
    """Draws a hyperboloid of one sheet. 
    
    Example
    =======
    >>> from axiomathbf.multivariate_calculus import *
    >>> draw_hyperboloid_one_sheet()
    **Displays image    

    Note
    ====
    Formula: x**2/a**2 + y**2/b**2 - z**2/c**2 = 1
    Best to use Jupyter Notebook to display the image.
    Credit: https://stackoverflow.com/questions/8062248/plotting-a-hyperboloid
    """
    fig = plt.figure(figsize=plt.figaspect(1))
    ax = fig.add_subplot(projection="3d")
    u = np.linspace(-1, 1, 100)
    theta = np.linspace(0, 2 * np.pi, 100)
    u, T = np.meshgrid(u, theta)
    x = np.cosh(u) * np.cos(T)
    y = np.cosh(u) * np.sin(T)
    z = np.sinh(u)
    ax.plot_surface(x, y, z, cmap=plt.cm.YlGnBu_r)
    plt.title("Hyperboloid of One Sheet")
    plt.show()


def draw_elliptic_paraboloid():
    """Draws an elliptic paraboloid. 

    Example
    =======
    >>> from axiomathbf.multivariate_calculus import *
    >>> draw_elliptic_paraboloid()
    **Displays image        
    
    Note
    ====
    Formula:  z = x**2/a**2 + y**2/b**2
    Best to use Jupyter Notebook to display the image.
    """
    fig = plt.figure(figsize=plt.figaspect(1))
    ax = plt.axes(projection="3d")
    x, y = np.linspace(-1, 1, 100), np.linspace(-1, 1, 100)
    X, Y = np.meshgrid(x, y)
    Z = X ** 2 + Y ** 2
    ax.plot_surface(X, Y, Z, cmap=plt.cm.YlGnBu_r)
    plt.title("Elliptic Paraboloid")
    plt.show()


def draw_hyperboloid_two_sheet():
    """Draws a hyperboloid of two sheets. 
    
    Example
    =======
    >>> from axiomathbf.multivariate_calculus import *
    >>> draw_hyperboloid_two_sheet()
    **Displays image        
    
    
    Note
    ====
    Formula: z**2/c**2 - x**2/a**2 - y**2/b**2 = 1
    Best to use Jupyter Notebook to display the image.
    """
    fig = plt.figure(figsize=plt.figaspect(1))
    ax = plt.axes(projection="3d")
    x, y = np.linspace(-1, 1, 100), np.linspace(-1, 1, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.sqrt(1 + X ** 2 + Y ** 2)
    ax.plot_surface(X, Y, Z, cmap=plt.cm.YlGnBu_r)
    ax.plot_surface(X, Y, -Z, cmap=plt.cm.YlGnBu_r)
    plt.title("Hyperboloid of Two Sheet")
    plt.show()


def draw_hyperbolic_paraboloid():
    """Draws a hyperbolic paraboloid. 
    
    Example
    =======
    >>> from axiomathbf.multivariate_calculus import *
    >>> draw_hyperboloid_two_sheet()
    **Displays image        

    Note
    ====
    Formula: z = y**2/b**2 - x**2/a**2
    Best to use Jupyter Notebook to display the image.
    """
    fig = plt.figure(figsize=plt.figaspect(1))
    ax = plt.axes(projection="3d")
    x, y = np.linspace(-1, 1, 100), np.linspace(-1, 1, 100)
    X, Y = np.meshgrid(x, y)
    Z = X ** 2 - Y ** 2
    ax.plot_surface(X, Y, Z, cmap=plt.cm.YlGnBu_r)
    plt.title("Hyperbolic Paraboloid")
    plt.show()


# 11.8
def convert_rect_to_cylinder(p):
    """Converts rectangular coordinates to cylinderical.
    
    Example
    =======
    >>> from axiomathbf.multivariate_calculus import *
    >>> convert_rect_to_cylinder(Point(1,-sqrt(3),-2))
    Point3D(2, 5*pi/3, -2)
    
    :param p (sympy.geometry.point.Point3D): A point in rectangular.
    :return (sympy.geometry.point.Point3D): A point transformed to cylindrical (r, theta, z).
    """
    x, y, z = p
    return Point(
        sqrt(x ** 2 + y ** 2),
        atan(y / x) if atan(y / x) > 0 else atan(y / x) + 2 * pi,
        z,
    )


def convert_rect_to_sphere(p):
    """Converts rectangular coordinates to spherical.
    
    Example
    =======
    >>> from axiomathbf.multivariate_calculus import *
    >>> convert_rect_to_sphere(Point(1,-sqrt(3),-2))
    Point3D(2*sqrt(2), 5*pi/3, 3*pi/4)  
    
    :param p (sympy.geometry.point.Point3D): A point in rectangular.
    :return (sympy.geometry.point.Point3D): A point tranformed to spherical (rho, theta, phi).
    """
    x, y, z = p
    return Point(
        sqrt(x ** 2 + y ** 2 + z ** 2),
        atan(y / x) if atan(y / x) > 0 else atan(y / x) + 2 * pi,
        acos(z / sqrt(x ** 2 + y ** 2 + z ** 2))
        if acos(z / sqrt(x ** 2 + y ** 2 + z ** 2)) > 0
        else acos(z / sqrt(x ** 2 + y ** 2 + z ** 2)) + pi,
    )


def convert_cylinder_to_rect(p):
    """Converts cylinderical coordinates to rectangular.

    Example
    =======
    >>> from axiomathbf.multivariate_calculus import *
    >>> convert_cylinder_to_rect(Point(2,pi/2,1))
    Point3D(0, 2, 1)  
    
    :param p (sympy.geometry.point.Point3D): A point in cylinderical.
    :return (sympy.geometry.point.Point3D): A point tranformed to rectangular (x,y,z).
    """
    r, Ѳ, z = p
    return Point(r * cos(Ѳ), r * sin(Ѳ), z)


def convert_sphere_to_rect(p):
    """Converts spherical coordinates to rectangular.

    Example
    =======
    >>> from axiomathbf.multivariate_calculus import *
    >>> convert_sphere_to_rect(Point(sqrt(5),pi/2,acos(1/sqrt(5)))
    Point3D(0, 2, 1)  
    
    Args:
        p (sympy.geometry.point.Point3D): A point in spherical.
    
    Returns:
        (sympy.geometry.point.Point3D): A point tranformed to rectangular (x,y,z).
    """
    ρ, φ, Ѳ = p
    return Point(ρ * sin(φ) * cos(Ѳ), ρ * cos(φ), ρ * sin(φ) * sin(Ѳ))


# 12.1
def find_domain_of_vector_function(v, s=False):
    """Finds and returns the domain of the vector function.
    
    Example
    =======
    >>> from axiomathbf.multivariate_calculus import *
    >>> find_domain_of_vector_function(make_vector(x**2,sqrt(1-x),-1/x))
    Union(Interval.open(-oo, 0), Interval.Lopen(0, 1))
    
    :param v (sympy.matrices.dense.MutableDenseMatrix): The vector-valued function.
    :return sympy.sets.sets.Union: The domain of the vector-valued function.
    """
    domain = Interval(-oo, oo)
    for i in range(len(v)):
        if s:
            print("{}: {}".format(v[i], continuous_domain(v[i], x, S.Reals)))
        domain = Intersection(continuous_domain(v[i], x, S.Reals), domain)
    return domain


# 12.2
def tangent_line(u, p=0, t=False):
    """Returns the parametric line tangent to the curve.
    
    Example
    =======
    >>> from axiomathbf.multivariate_calculus import *
    >>> tangent_line(make_vector(ln(x),2*sqrt(x),x**2),Point(0,2,1))
    <x,y,z> = <0,2,1> + <1,1,2>t
    
    :param u (sympy.matrices.dense.MutableDenseMatrix): The vector-valued function.
    :param p=0 (int) or (sympy.geometry.point.Point3D): A point at the curve.
    :param t=False (bool): Determine whether it is a point or when t = #.
    :return str: A parametric line tanget to the curve at a point.
    """
    solution = 0
    if not t:
        solutions = []
        solution_count = {}
        for i in range(len(u)):
            solutions.append(solve(u[i] - p[i]))

        for i in range(len(solutions)):
            for j in range(len(solutions[i])):
                if solutions[i][j] not in solution_count:
                    solution_count[solutions[i][j]] = 1
                else:
                    solution_count[solutions[i][j]] += 1

        for i in solution_count:
            if solution_count[i] == 3:
                solution = i
                break
    else:
        solution = p
        p = Point(
            u[0].replace(x, solution),
            u[1].replace(x, solution),
            u[2].replace(x, solution),
        )

    derivative = derive_vector_function(u).replace(x, solution)
    return point_vector_line(p, derivative)


def derive_vector_function(u):
    """Returns a derived vector-valued function.
    
    Example
    =======
    >>> from axiomathbf.multivariate_calculus import *
    >>> derive_vector_function(make_vector(exp(x),sin(x),23*x**4))
    Matrix([[exp(x), cos(x), 92*x**3]])
    
    :param u (sympy.matrices.dense.MutableDenseMatrix): A vector-valued function.
    :return (sympy.matrices.dense.MutableDenseMatrix): A derived vector-valued function.
    """
    derivative = []
    for i in range(len(u)):
        derivative.append(diff(u[i], x))
    return Matrix([derivative])


def integrate_vector_function(u):
    """Returns a integrated vector-valued function.
    
    Example
    =======
    >>> from axiomathbf.multivariate_calculus import *
    >>> integrate_vector_function(make_vector(exp(x),sin(x),23*x**4))
    Matrix([[exp(x), -cos(x), 23*x**5/5]])
    
    :param u (sympy.matrices.dense.MutableDenseMatrix): A vector-valued function.
    :return (sympy.matrices.dense.MutableDenseMatrix): An integrated vector-valued function.
    """
    integration = []
    for i in range(len(u)):
        integration.append(integrate(u[i], x))
    return Matrix([integration])


# 13.1
def graph_contour(f, xrange, yrange):
    """Creates a contour plot of a function.
    
    Example
    =======
    >>> from axiomathbf.multivariate_calculus import *
    >>> graph_contour("np.cos(Y)", [-3, 3], [-3, 3])
    ** Image of the contour plot
    
    :param f (str): The function.
    :param xrange (List): The x-axis boundaries.
    :param yrange (List): The y-axis boundaries.
    """
    ax = plt.axes()
    x, y = (
        np.linspace(xrange[0], xrange[1], 100),
        np.linspace(yrange[0], yrange[1], 100),
    )
    X, Y = np.meshgrid(x, y)
    Z = eval(f)
    plt.contourf(X, Y, Z, 20, cmap="viridis")
    plt.colorbar()
    plt.show()


def graph_model(f, xrange, yrange):
    """Creates a 3D plot of a function.
    
    Example
    =======
    >>> from axiomathbf.multivariate_calculus import *
    >>> graph_model("np.cos(Y)", [-3, 3], [-3, 3])
    ** Image of the function model in 3D
    
    :param f (str): The function.
    :param xrange (List): The x-axis boundaries.
    :param yrange (List): The y-axis boundaries.
    """
    ax = plt.axes(projection="3d")
    x, y = (
        np.linspace(xrange[0], xrange[1], 100),
        np.linspace(yrange[0], yrange[1], 100),
    )
    X, Y = np.meshgrid(x, y)
    Z = eval(f)
    ax.contour3D(X, Y, Z, 50, cmap="viridis")
    plt.show()


# https://www.science-emergence.com/Articles/How-to-put-the-origin-in-the-center-of-the-figure-with-matplotlib-/
def draw_boundaries(xrange, yrange, xbound, ybound):
    """Draws out the boundaries for a double integral.
    
    Example
    =======
    >>> from axiomathbf.multivariate_calculus import *
    >>> draw_boundaries([-1, 1], [-1, 1], ["1", "0"], ["x**2", "-x"])
    ** Image of the boundaries on the two axes
    
    :param xrange (List of int): The x-coordinate range.
    :param yrange (List of int): The y-coordinate range.
    :param xbound (List of str): The boundaries for x, whether it is a constant or a function.
    :param ybound (List of str): The boundaries for y, whether it is a constant or a function.
    """
    fig = plt.figure()
    ax = plt.axes()
    x = np.linspace(xrange[0], xrange[1], 100)
    y = np.linspace(yrange[0], yrange[1], 100)
    ax.grid(True)
    ax.spines["left"].set_position("zero")
    ax.spines["right"].set_color("none")
    ax.spines["bottom"].set_position("zero")
    ax.spines["top"].set_color("none")
    for i in xbound:
        ax.plot(
            eval(i) if type(eval(i)) == np.ndarray else np.full(y.size, eval(i)), y,
        )
    for i in ybound:
        ax.plot(
            x, eval(i) if type(eval(i)) == np.ndarray else np.full(x.size, eval(i)),
        )
    plt.show()


# 13.4
def find_linearization(f, p, s=False):
    """Returns the linearization equation for local-linear approximation.
    
    Example
    =======
    >>> from axiomathbf.multivariate_calculus import *
    >>> find_linearization(3*x**2-2*y**2+x*z**3, Point(-1,2,1))
    -5*x - 8*y - 3*z + 8
    
    :param f (sympy.core.add.Add): A function.
    :param p (sympy.geometry.point.Point3D): A point.
    :param s=False (bool): Determines whether the user wants to see the work of partial derivatives.
    :return sympy.core.add.Add: The linearization equation.
    """
    g = find_gradient(f, p, s)
    f_at_p = f.replace(x, p[0]).replace(y, p[1]).replace(z, p[2])
    return f_at_p + g[0] * (x - p[0]) + g[1] * (y - p[1]) + g[2] * (z - p[2])


# 13.5
def chain_rule(f, xf, yf, zf, respect, s=False):
    """Returns the derived function using chain rule.
    
    Example
    =======
    >>> from axiomathbf.multivariate_calculus import *
    >>> s, t = symbols("s t")
    >>> chain_rule(x*y*sin(z**2),s-t,s**2,t**2,s)
    s**2*sin(t**4) + 2*s*(s - t)*sin(t**4)
    
    :param f (sympy.core.add.Add): The main function.
    :param xf (sympy.core.add.Add): The x-function.
    :param yf (sympy.core.add.Add): The y-function.
    :param zf (sympy.core.add.Add): The z-function.
    :param respect (sympy.core.symbol.Symbol): The variable deriving respect to.
    :return (sympy.core.add.Add): The derived function.
    """
    dfdX = []
    dXdr = [diff(xf, respect), diff(yf, respect), diff(zf, respect)]
    result = 0
    for res in [x, y, z]:
        dfdX.append(diff(f, res))
        if s:
            display(Derivative(f, res))
            display(diff(f, res))
    if s:
        display(Derivative(xf, respect), diff(xf, respect))
        display(Derivative(yf, respect), diff(yf, respect))
        display(Derivative(zf, respect), diff(zf, respect))
    for i in range(3):
        result += dfdX[i].replace(x, xf).replace(y, yf).replace(z, zf) * dXdr[i]
    return result


# 13.6
def find_gradient(f, p, s=False):
    """Returns the gradient of a function. Very useful helper function.
    
    Example
    =======
    >>> from axiomathbf.multivariate_calculus import *
    >>> find_gradient(4*x*y*z-y**2*z**3+4*z**3*y,Point(2,3,1))
    Matrix([[12, 6, 33]])
    
    :param f (sympy.core.add.Add): The function.
    :param p (sympy.geometry.point.Point3D): A point.
    :param s=False (bool): Determines whether the user wants to see the partial derivative work.
    :return (sympy.matrices.dense.MutableDenseMatrix): The gradient vector.
    """
    fx, fy, fz = "", "", ""
    res = [x, y, z]
    partial = [fx, fy, fz]
    for i in range(3):
        partial[i] = diff(f, res[i]).replace(x, p[0]).replace(y, p[1]).replace(z, p[2])
        if s:
            print("Respect to: " + str(res[i]))
            display(diff(f, res[i]))
    return make_vector(partial[0], partial[1], partial[2])


def directional_derivative(f, p, v, s=False):
    """Returns the directional derivative at a point.
    
    Example
    =======
    >>> from axiomathbf.multivariate_calculus import *
    >>> directional_derivative(exp(x)*cos(y*z),Point(1,pi,0),make_vector(-2,1,-3))
    -sqrt(14)*E/7
    
    :param f (sympy.core.add.Add): A function.
    :param p (sympy.geometry.point.Point3D): A point.
    :param v (sympy.matrices.dense.MutableDenseMatrix): A vector.
    :return ympy.core.mul.Mul: The directional derivative.
    """
    return find_gradient(f, p, s).dot(v / v.norm())


def directional_derivative_info(f, p, increasing=True):
    """Returns more information about directional derivative.
    
    Example
    =======
    >>> from axiomathbf.multivariate_calculus import *
    >>> directional_derivative_info(exp(x*y**2),Point(1,3,0))
    (3*sqrt(13)*exp(9), Matrix([[3*sqrt(13)/13, 2*sqrt(13)/13, 0]]))
    
    :param f (sympy.core.add.Add): A function.
    :param p (sympy.geometry.point.Point3D): A point.
    :param increasing=True (bool): Determines whether to make the maximum and unit vector negative.
    :return tuple: The first index is the maximum value of the directional derivative, the second
               was the unit vector for the direction.
    """
    g = find_gradient(f, p)
    maximum = g.norm() if increasing else -g.norm()
    unit_vector = g / g.norm() if increasing else -(g / g.norm())
    return (maximum, unit_vector)


# 13.7
def tangent_plane(f, p, s=False):
    """Returns the tangent plane formula.
    
    Example
    =======
    >>> from axiomathbf.multivariate_calculus import *
    >>> tangent_plane(ln(x+y+z),Point(-1,exp(2),1))
    (x + 1)*exp(-2) + (y - exp(2))*exp(-2) + (z - 1)*exp(-2)
    
    :param f (sympy.core.add.Add): A function.
    :param p (sympy.geometry.point.Point3D): A point.
    :param s=False (bool): Determines whether the user wants to see the partial derivative work.
    :return (sympy.core.add.Add): A tangent plane.
    """
    g = find_gradient(f, p, s)
    return make_plane(p, g)


def normal_lines(f, p, s=False):
    """Returns the normal line formula.
    
    Example
    =======
    >>> from axiomathbf.multivariate_calculus import *
    >>> normal_lines(ln(x+y+z),Point(-1,exp(2),1))
    <x,y,z> = <-1,exp(2),1> + <exp(-2),exp(-2),exp(-2)>t
    
    :param f (sympy.core.add.Add): A function.
    :param p (sympy.geometry.point.Point3D): A point.
    :param s=False (bool): Determines whether the user wants to see the partial derivative work.
    :return (sympy.core.add.Add): A normal line.
    """
    g = find_gradient(f, p, s)
    return point_vector_line(p, g)


# 13.8
def find_relative_extreme(f):
    """Prints out all the relative extrema.
    
    Example
    =======
    >>> from axiomathbf.multivariate_calculus import *
    >>> find_relative_extreme(x**3-3*x+y**2-6*y)
    Saddle point: (-1, 3)
    Relative minimum: (1, 3)
    
    :param f (sympy.core.add.Add): A function.
    """
    x1, y1 = 0, 0
    fx, fy = diff(f, x), diff(f, y)
    x1, y1 = solve(fx), solve(fy)
    points = [[i, j] for i in x1 for j in y1]
    for i in points:
        fxx, fyy, fxy = (
            diff(fx, x).replace(x, i[0]),
            diff(fy, y).replace(y, i[1]),
            diff(fx, y).replace(x, i[0]).replace(y, i[1]),
        )
        result = fxx * fyy - fxy ** 2
        if result > 0:
            if fxx > 0:
                print("Relative minimum: " + str((i[0], i[1])))
            else:
                print("Relative minimum: " + str((i[0], i[1])))
        elif result < 0:
            print("Saddle point: " + str((i[0], i[1])))
        else:
            print("Inconclusive: " + str((i[0], i[1])))


# 14.7
def find_jacobian(func, res):
    """Returns the Jacobian constant. 
    
    Example
    =======
    >>> from axiomathbf.multivariate_calculus import *
    >>> ρ, φ, Ѳ = symbols("ρ φ Ѳ")
    >>> find_jacobian([ρ*sin(φ)*cos(Ѳ),ρ*sin(φ)*sin(Ѳ),ρ*cos(φ)],[ρ, φ, Ѳ])
    ρ**2*sin(φ)
    
    :param func (list): The list of x,y,z functions.
    :param res (list): The list of partial derivative respects.
    :return sympy.core.mul.Mul: The Jacobian.
    """
    matrix = []
    for i in func:
        arr = []
        for j in res:
            arr.append(diff(i, j))
        matrix.append(arr)
    return simplify(Matrix(matrix).det())

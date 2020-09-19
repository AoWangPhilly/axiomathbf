<p align="center">
  <img src="https://github.com/AoWangPhilly/axiomathbf/blob/master/axiomathbflogo.png?raw=true"/>
</p>

Axiomathbf is a Mathematical Aid package for Multivariate Calculus, used mainly for Jupyter Notebook due to outputs mainly are in Latex. But users can solve Multivariate Calculus problems using any Python environment. Axiomathbf can find the relative and absolute extrema of a function to calculating the gradient and directional derivative of a function.

I decided to create Axiomathbf when I began Math 200 at Drexel University in the winter. As a freshman, I wanted to implement what I learned from my CS courses. And math was what started my CS journey when I first programmed my TI-84.

## Table of Content

* [Technologies Used](#tech)
* [Installation](#install)
* [How Does it Work?](#how)
* [User Manual](#user)
* [Further Goals](#goals)
* [License](#license)

## <div id="tech"> Technologies Used </div>

* Python
* [Sympy](https://www.sympy.org/en/index.html) - A computer algebra system written in pure Python
* [Jupyter Notebook](https://jupyter.org/) - an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and narrative text

##  <div id="install"> Installation </div>

``` bash
git clone git@github.com:ow-wow-wang/axiomathbf.git
```

``` bash
pip install -r requirements.txt
```

##  <div id="how"> How Does it Work? </div>

* For each module, I created a class related to the topic of the chapters, like creating the VectorFunction class to solve vector-related problems in chapters 11-12 in the Calculus Early Transcendentals textbook, which talk about Three-Dimensions Space, Vectors, and Vector-Valued Functions.
* I mainly used Sympy to derive, integrate, and other operations to solve these problems
* I also used OOP-design, as it allows me to write more clean code

##  <div id="user"> Documentation </div>

Find the documentation at [https://aowangphilly.github.io/axiomathbf](https://aowangphilly.github.io/axiomathbf/) to learn how to use Axiomathbf

##  <div id="goals"> Further Goals </div>

* I hope to create a Flask web application, so people who aren't familiar with programming can still solve MV problems
* I also want to create an mobile app that solves Linear Algebra problems using Sympy and OpenCV

##  <div id="license">  License </div>

  + [MIT](https://choosealicense.com/licenses/mit/)

# axiomathbf
Axiomathbf is a Mathematical Aid package for Multivariate Calculus, used mainly for Jupyter Notebook since the outputs are mostly in Latex. But users can solve Multivariate Calculus problems from dot products and projections to finding the gradient and directional derivative of a function. 

I decided to start the project when I began taking Math 200 at Drexel University around December. I wanted to combine what I learned in my CS courses. And math is what started my CS journey when I first programmed my TI-84. 

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
* NumPy
* [Jupyter Notebook](https://jupyter.org/) - an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and narrative text

##  <div id="install"> Installation </div>

``` bash
git clone git@github.com:ow-wow-wang/axiomathbf.git
```

``` bash
pip install -r requirements.txt
```

##  <div id="how"> How Does it Work? </div>

* For each module, I created a class related to the topic of the chapters, like creating the Vector class to solve vector-related problems in chapters 11-12 in the Calculus Early Transcendentals textbook, which talk about Three-Dimensions Space, Vectors, and Vector-Valued Functions.
* I mainly used Sympy to derive, integrate, and other operations to solve these problems
* I also used OOP-design, as it allows me to write more clean code

##  <div id="user"> User Manual </div>

There are multiple Jupyter Notebooks to explain each portion of the code [here](https://github.com/ow-wow-wang/axiomathbf/tree/master/notebooks)

##  <div id="goals"> Further Goals </div>

* I hope to create a Flask web application, so people who aren't familiar with programming can still solve MV problems
* I also want to create an mobile app that solves Linear Algebra problems using Sympy and OpenCV

##  <div id="license">  License </div>

  + [MIT](https://choosealicense.com/licenses/mit/)

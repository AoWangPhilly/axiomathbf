from setuptools import setup

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()
setup(
    name='axiomathbf',         # How you named your package folder (MyLib)
    packages=['axiomathbf'],   # Chose the same as "name"
    version='0.0.4',      # Start with a small number and increase it with every change you make
    # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    license='MIT',
    # Give a short description about your library
    description='Multivariable Calculus Aid',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Ao Wang',                   # Type in your name
    author_email='aw3338@drexel.edu',      # Type in your E-Mail
    # Provide either the link to your github or to your website
    url='https://github.com/AoWangPhilly',
    # Keywords that define your package best
    keywords=['Python', 'Multivariable Calculus', 'Sympy', 'Latex'],
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Development Status :: 3 - Alpha',
        # Define that your audience are developers
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',   # Again, pick a license
        # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
)

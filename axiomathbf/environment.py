from IPython import get_ipython


def isnotebook():
    '''Checks to see if the Python environment is in Jupyter Notebook or not.

    Credit: https://stackoverflow.com/questions/15411967/how-can-i-check-if-code-is-executed-in-the-ipython-notebook/54967911#54967911

    :return: whether or not the working environment is in Jupyter Notebook
    :rtype: bool
    '''
    try:
        shell = get_ipython().__class__.__name__
        if shell == 'ZMQInteractiveShell':
            return True   # Jupyter notebook or qtconsole
        elif shell == 'TerminalInteractiveShell':
            return False  # Terminal running IPython
        else:
            return False  # Other type (?)
    except NameError:
        return False      # Probably standard Python interpreter

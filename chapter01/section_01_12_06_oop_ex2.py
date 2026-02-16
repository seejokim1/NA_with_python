# ==========================================================
# (Section 1.12.6) OOP Example 2
# File: chapter01/section_01_12_06_oop_ex2.py
# Description:
#   Object-Oriented Programming example:
#   Define a function and its derivative,
#   then visualize both using matplotlib.
# ==========================================================

import numpy as np
import matplotlib.pyplot as plt


# ----------------------------------------------------------
# Class Definition
# ----------------------------------------------------------
class Function:
    """
    Function class:
    Stores a function and its derivative,
    and provides evaluation and visualization methods.
    """

    def __init__(self, func, d_func):
        """
        Constructor
        Parameters:
            func   : function f(x)
            d_func : derivative f'(x)
        """
        self.func = func
        self.d_func = d_func

    def evaluate(self, x):
        """Return function value f(x)"""
        return self.func(x)

    def derivative(self, x):
        """Return derivative value f'(x)"""
        return self.d_func(x)

    def visualize(self, x_range):
        """
        Visualize function and derivative
        Parameters:
            x_range : tuple (xmin, xmax)
        """
        x = np.linspace(x_range[0], x_range[1], 500)

        y = self.evaluate(x)
        y_prime = self.derivative(x)

        plt.figure(figsize=(10, 6))

        plt.plot(x, y,
                 label='f(x) = x^2',
                 linewidth=2)

        plt.plot(x, y_prime,
                 label="f'(x) = 2x",
                 linestyle='--',
                 linewidth=2)

        plt.axhline(0, color='black', linewidth=0.8)

        plt.title('Function and its Derivative')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.grid(True)

        plt.show()


# ----------------------------------------------------------
# Main Execution
# ----------------------------------------------------------
if __name__ == "__main__":

    # Define function and derivative
    f = lambda x: x**2
    df = lambda x: 2*x

    # Create object
    quadratic_function = Function(f, df)

    # Visualize
    quadratic_function.visualize((-10, 10))

"""
Class for computing bound state and free state atomic wave functions
"""

from .constants import *
from .math_helper import *
from math import factorial


def r_sto(r, z, n):
    # Radial wave function R_STO
    # 2105.05253
    return power(A0, -1.5) * power(2*z, n+0.5) * power(r/A0, n-1) * exp(-z*r/A0) / sqrt(factorial(2*n))



def coeff_jlnk():
    pass


def z_jlk():
    pass


def n_jlk():
    pass



def y_lm():
    # Spherical Harmonics of Condon-Shortley convention
    pass




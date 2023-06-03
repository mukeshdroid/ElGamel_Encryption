# generates the key
import random
from .lib import order, euler_totitent, nDigitPrimeGen, primitive_root


import sympy




def keyGen(n):
    q = nDigitPrimeGen(n)
    g = primitive_root(q)
    x = random.randint(2, q-1)
    h = pow(g, x, q)
    return ((q, g, h, x), (q, g, h))

import sys
import math
from matplotlib import pyplot as pl

def f1(x):
    return x**2+1

def f2(x):
    return x**3+3

x=range(-20,20)

pl.figure("Función x^2+1")
pl.plot(x, [f1(i) for i in x])
pl.show()
pl.figure("Función x^3+1")
pl.plot(x, [f2(i) for i in x])
pl.show()
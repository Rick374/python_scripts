import pylab as pl

def f1(x):
    return x^2+1

def f2(x):
    return x^3+3

x=range(-20,20)

pl.plot(x, [f1(i) for i in x])

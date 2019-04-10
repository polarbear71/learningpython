#! usr/bin/env python

import numpy as np
import scipy as sp
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy.misc
import scipy.integrate

def f(x):
    return x**3 - 30*np.sin(x)**2 - 4
def df(x): 
    return sp.misc.derivative(f, x)
@np.vectorize
def F(x):
    return sp.integrate.quad(f, 0, x)[0]

X = np.linspace(-4, 5, 400)
Y = f(X)
Y1 = df(X)
Y2 = F(X)
plt.plot(X, Y, linewidth=4, label="f")
plt.plot(X, Y1, linewidth=2, linestyle="dashed", label="f'")
plt.plot(X, Y2, linewidth=2, linestyle="dotted", label="F")
plt.legend(loc="upper left")
plt.show()

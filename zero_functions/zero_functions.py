import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'figure.autolayout': True})


def f(x): return 4*np.sin(x) - np.tan(2*x)


def df(x): return 4*np.cos(x) - 2 / np.cos(2*x)**2


# Find the zeros between 0 and pi/2 of the function f(x) = 4sin(x) - tan(2x) using bisection method

x1 = 0.2
x2 = 0.7
error = 1e-15
n_stepsB = 0

while (x2 - x1) / 2 > error:
    xb = (x1 + x2) / 2
    if f(xb)*f(x1) > 0:
        x1 = xb
    else:
        x2 = xb
    n_stepsB += 1
x0B = (x1 + x2) / 2

# Find the zeros between 0 and pi/2 of the function f(x) = 4sin(x) - tan(2x) using Newton-Raphson method

x = 0.5
delX = 1e10
n_stepsNR = 0
while abs(delX) > error:
    n_stepsNR += 1
    delX = - f(x) / df(x)
    x += delX
    print(n_stepsNR, x, delX)

x0NR = x

# Graphics
x = np.arange(0, 4, 0.01)

# Bisection graphic
plt.subplot(2, 1, 1)
plt.plot(x, 4*np.sin(x), '-b', label='4sin(x)')
plt.plot(x, np.tan(2*x), '-r', label='tan(2x)')
plt.plot(x, f(x), '-g', label='f(x) = 4sin(x) - tan(2x)')
plt.plot(x0B, 4 * np.sin(x0B), 'o', color='grey', label='Point where 4sin(x)=tan(2x)')
plt.plot(x0B, f(x0B), 'o', color='black', label='Zero of f(x)')
plt.axvline(x=x0B, ymin=0.5, ymax=(4.5 + 4 * np.sin(x0B)) / 9, color='black', label=f'y = x0 = {x0B}')
plt.ylim(-4.5, 4.5)
plt.legend()
plt.grid()
plt.title(f'Bisection Method, number of steps = {n_stepsB}')

# Newton-Raphson graphic
plt.subplot(2, 1, 2)
plt.plot(x, 4*np.sin(x), '-b', label='4sin(x)')
plt.plot(x, np.tan(2*x), '-r', label='tan(2x)')
plt.plot(x, f(x), '-g', label='f(x) = 4sin(x) - tan(2x)')
plt.plot(x0NR, 4 * np.sin(x0NR), 'o', color='grey', label='Point where 4sin(x)=tan(2x)')
plt.plot(x0NR, f(x0NR), 'o', color='black', label='Zero of f(x)')
plt.axvline(x=x0NR, ymin=0.5, ymax=(4.5 + 4 * np.sin(x0NR)) / 9, color='black', label=f'y = x0 = {x0NR}')
plt.ylim(-4.5, 4.5)
plt.legend()
plt.grid()
plt.title(f'Newton-Raphson Method, number of steps = {n_stepsNR}')

plt.savefig("zero_functions.png")

plt.show()

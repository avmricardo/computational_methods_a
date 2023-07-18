import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize

'''
Quantum mechanics potential well problem:
V(x) = "0" if |x|<a else "V_0", a>0
'''

# Constants

h = 7.63  # m_e . eV . A^2 = h_bar^2
a = 4  # angstroms
V_0 = 16  # eV
r = np.sqrt(2 / h)  # = sqrt(2m/h_bar^2)
# m = m_e

E = np.linspace(0.001, 16, 200)


def alpha(e):
    return r*np.sqrt(e)


def d_alpha(e):
    return r / (2 * np.sqrt(e))


def beta(e):
    return r*np.sqrt(V_0 - e)


def d_beta(e):
    return - r / (2 * np.sqrt(V_0 - e))


def even_func(e):
    return alpha(e)*np.tan(alpha(e) * a)


def d_even_func(e):
    return d_alpha(e)*np.tan(alpha(e) * a) + a*alpha(e)*d_alpha(e) / np.cos(alpha(e) * a)**2


def odd_func(e):
    return alpha(e) / np.tan(alpha(e) * a)


def d_odd_func(e):
    return d_alpha(e) / np.tan(alpha(e) * a) - a*alpha(e)*d_alpha(e) / np.sin(alpha(e) * a)**2


'''
Wave function and its derivative continuity conditions:
Even symmetry: alpha*tan(alpha*a) = beta
Odd symmetry: alpha*cot(alpha*a) = - beta
'''

# Calculating the energy


def cond_even(e):
    return even_func(e) - beta(e)


def d_cond_even(e):
    return d_even_func(e) - d_beta(e)


def cond_odd(e):
    return odd_func(e) + beta(e)


def d_cond_odd(e):
    return d_odd_func(e) + d_beta(e)


# Using the bisection method
x1 = 15
x2 = 15.5
error = 1e-15
n_stepsB = 0

while (x2 - x1) / 2 > error:
    xb = (x1 + x2) / 2
    if cond_odd(xb)*cond_odd(x1) > 0:
        x1 = xb
    else:
        x2 = xb
    n_stepsB += 1

x0_B = (x1 + x2) / 2

even_roots_bisection = np.array([0.4667, 4.1606, 11.2245])
odd_roots_bisection = np.array([1.8607, 7.3190, 15.4286])

print(f'Bisection method: 49 steps for intervals of length 1 and error {error}.')
print(f'Even roots: {even_roots_bisection}')
print(f'Odd roots: {odd_roots_bisection}')

# Using Newton-Raphson method
x = 7
delX = 1e10
n_stepsNR = 0
while abs(delX) > error:
    n_stepsNR += 1
    delX = - cond_odd(x) / d_cond_odd(x)
    x += delX

even_roots_nr = {0.4667: 7, 4.1606: 6, 11.2245: 5}

# The Newton-Raphson method does not work for the root next to E=15 in the cond_odd, so I used the scipy.optimize.newton

scipy.optimize.newton(cond_odd, 15)  # which is equal to 15.4286

odd_roots_nr = {1.8607: 8, 7.3190: 6, 15.4286: 'scipy.optimize.newton'}

print(f'Newton-Raphson method with error = {error}:')
print(f'Even roots | steps:')
for i in even_roots_nr:
    print(f'{i}, {even_roots_nr[i]}')
print('Odd roots | steps:')
for i in odd_roots_nr:
    print(f'{i}, {odd_roots_nr[i]}')

# Plotting the continuity conditions
plt.subplot(2, 1, 1)
plt.plot(E, beta(E), 'r--', label=r'$\beta$')
plt.plot(E, even_func(E), 'r', label=r'$\alpha \tan(\alpha a)$')
plt.scatter(even_roots_bisection, beta(even_roots_bisection), color='red', label=r'$\alpha \tan(\alpha a) = \beta$')
plt.plot(E, - beta(E), 'b--', label=r'$-\beta$')
plt.plot(E, odd_func(E), 'b', label=r'$\alpha \cot(\alpha a)$')
plt.scatter(odd_roots_bisection, -beta(odd_roots_bisection), color='blue', label=r'$\alpha \cot(\alpha a) = -\beta$')
plt.xlabel('Energy (eV)')
plt.ylabel(r'$\AA^{-1}$')
plt.xlim(0, 16)
plt.ylim(-3, 3)
plt.legend()
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(E, cond_even(E), 'r', label=r'$f(E) = \alpha(E) \tan(\alpha(E) a) - \beta(E)$')
plt.scatter(even_roots_bisection, np.zeros_like(even_roots_bisection), color='red', marker='o', label='Roots of $f(E)$')
plt.plot(E, cond_odd(E), 'b', label=r'$g(E) = \alpha(E) \cot(\alpha(E) a) + \beta(E)$')
plt.scatter(odd_roots_bisection, np.zeros_like(odd_roots_bisection), color='blue', marker='o', label='Roots of $g(E)$')
plt.xlabel('Energy (eV)')
plt.ylabel(r'$\AA^{-1}$')
plt.xlim(0, 16)
plt.ylim(-3, 3)
plt.legend()
plt.grid()

plt.savefig("potential_well/potential_well.png")

plt.show()

import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'figure.autolayout': True})

N = 10

iN = np.arange(N)

km = 1  # k sobre m

# Construção da matriz evolução temporal
A = np.zeros([N, N])
A[iN, iN] = 2 * km
A[iN[1:], iN[:-1]] = -km
A[iN[:-1], iN[1:]] = -km

# Condição de contorno extremidades livres
# A[0, 0] = A[-1, -1] = km

# Condição de contorno periódica
A[0, -1] = A[-1, 0] = km

# Impureza na rede (massa 5 mais pesada)
A[N//2, :] /= 5

# Cálculo de ordenamento dos autovetores e autovalores
lamb, X = np.linalg.eig(A)
lamb[lamb < 0] = 0
asort = np.argsort(lamb)
lamb = lamb[asort]
X = X[:, asort]
omega = np.sqrt(lamb)

fig = plt.figure()
# Gráfico das frequências (energia = hf)
graf1 = fig.add_subplot(2, 1, 1)
plt.ylabel('Omega')
plt.xlabel('Número do autovalor')
plt.plot(iN, omega, 'o')

# Gráfico dos modos normais
graf2 = fig.add_subplot(2, 1, 2)
for i in iN:
    plt.plot(iN, iN * 0 + 2*i, '-', color='gray')
    plt.plot(iN, X[:, i] + 2*i, 'o-')

plt.savefig("autovalores_autovetores/autovalores_autovetores.png")

plt.show()

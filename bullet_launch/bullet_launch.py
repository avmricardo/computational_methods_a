import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'figure.autolayout': True})

c = 1
m = 1
g = 10
delt = 0.001

v_wind = np.array([10, 0], dtype='float64')
v_bullet = np.array([50, 50], dtype='float64')
r0 = np.array([0, 0], dtype='float64')


def f(X):
    v_r = X[2:] - v_wind
    mod_vr = (v_r**2).sum()**0.5
    return np.array([X[2], X[3], -c * mod_vr * v_r[0] / m, -c * mod_vr * v_r[1] / m - g])


t = 0
X = np.concatenate([r0, v_bullet])
trajectory = np.concatenate([[t], X])
while X[1] >= 0:
    X += f(X)*delt
    t += delt
    trajectory = np.vstack([trajectory, np.concatenate([[t], X])])


t = trajectory[:, 0]
x = trajectory[:, 1]
y = trajectory[:, 2]
v_x = trajectory[:, 3]
v_y = trajectory[:, 4]

plt.subplot(2, 3, 1)
plt.plot(t, x)
plt.xlabel('Tempo (s)')
plt.ylabel('Posição X')

plt.subplot(2, 3, 2)
plt.plot(t, y)
plt.xlabel('Tempo (s)')
plt.ylabel('Posição Y')

plt.subplot(2, 3, 3)
plt.plot(t, v_x)
plt.xlabel('Tempo (s)')
plt.ylabel('Velocidade em X')

plt.subplot(2, 3, 4)
plt.plot(t, v_y)
plt.xlabel('Tempo (s)')
plt.ylabel('Velocidade em Y')

plt.subplot(2, 3, 5)
plt.plot(x, y)
plt.xlabel('Posição X')
plt.ylabel('Posição Y')

plt.savefig("bullet_launch/bullet_launch.png")

plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do movimento
periodo = 1
amp = 0.2
tau = 3*periodo  # x = amp * cos(2*t*pi/periodo)*exp(-t/tau)
erro = 0.05
omega = 2*np.pi / periodo

# Curvas teóricas
t_teo = np.linspace(0, 3 * periodo, 301)
x_teo = amp * np.cos(2 * t_teo * np.pi / periodo) * np.exp(-t_teo / tau)

# Pontos experimentais
t_exp = np.arange(0, 3*periodo, 0.1)
x_exp = amp * np.cos(2 * t_exp * np.pi / periodo) * np.exp(-t_exp / tau)
x_exp += np.random.uniform(-0.05, 0.05, len(x_exp))

# Velocidade teórica
v_teo = -amp*(omega*np.sin(omega*t_teo) - np.cos(omega*t_teo) / tau)*np.exp( -t_teo / tau )

# Velocidade experimental
v_exp = (x_exp[1:] - x_exp[:-1]) / (t_exp[1:] - t_exp[:-1])
tv_exp = (t_exp[:-1] + t_exp[1:]) / 2

# Gráfico teórico
plt.title('Pêndulo Amortecido')
plt.plot(t_teo, x_teo, '-b', label='$x_{teo}$')
plt.plot(t_exp, x_exp, 'or', label='Experimental')
plt.errorbar(t_exp, x_exp, erro, fmt='or', label='$x_{exp}$')
plt.xlabel('Tempo (s)')
plt.ylabel('Posição (m)', color='r')
plt.legend(loc='upper right')
plt.twinx()
plt.plot()
plt.ylim(-1.5*amp, 1.5*amp)
plt.plot()

plt.savefig("oscilador_amortecido/oscilador_amortecido.png")

plt.show()

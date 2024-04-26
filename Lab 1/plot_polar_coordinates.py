import numpy as np
import matplotlib.pyplot as plt


def strophoid(phi, a):
    return a * (1 + np.sin(phi)) / np.cos(phi)


phi = np.linspace(0, 2 * np.pi, 1000)
a = 1
p = strophoid(phi, a)

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(phi, p, 'r-', label=r'$\rho = \frac{1 + \sin(\phi)}{\cos(\phi)}$')

ax.text(0, a, r'$\rho = \frac{1 + \sin(\phi)}{\cos(\phi)}$', fontsize=12, va='bottom')

ax.set_rmax(10)
ax.set_rticks(np.arange(0, 10, 1))
ax.set_rlabel_position(-22.5)
ax.grid(True)
ax.set_title('Polar Plot', va='bottom')
ax.legend()

plt.show()

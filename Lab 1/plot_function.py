import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 1000)

y = (2 + np.sin(x) ** 3) / (1 + x ** 2)


def z1_func(x):
    return np.where(x <= 0, 5 * x ** 2 / (1 + x ** 2), np.nan)


z1 = z1_func(x)


def z2_func(x):
    return np.where(x > 0, np.sqrt(1 + (2 * x / (1 + x ** 2))), np.nan)


z2 = z2_func(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, 'r-', label=r'$y = \frac{2 + \sin^3(x)}{1 + x^2}$')
plt.plot(x, z1, 'b--', label=r'$z_1 = \frac{5x^2}{1 + x^2},$ if $x \leq 0$')
plt.plot(x, z2, 'g-.', label=r'$z_2 = \sqrt{1 + \left(\frac{2x}{1 + x^2}\right)},$ if $x > 0$')
plt.xlabel('x')
plt.ylabel('y, z')
plt.title('Графіки функцій')
plt.grid(True)
plt.legend()
plt.show()

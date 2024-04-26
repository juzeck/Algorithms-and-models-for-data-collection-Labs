import matplotlib.pyplot as plt
import numpy as np


def hyperboloid(x, y, a, b, c):
    return (x ** 2 / a ** 2) + (y ** 2 / b ** 2) - (c ** 2)


fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

a, b, c = 2, 3, 4

x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)
Z = hyperboloid(X, Y, a, b, c)

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Second-Order Surface')

# Вивід самої функції на графіку
ax.text2D(0.05, 0.95, r'$\frac{x^2}{a^2} + \frac{y^2}{b^2} - \frac{z^2}{c^2} = -1$', transform=ax.transAxes,
          fontsize=12)

plt.show()

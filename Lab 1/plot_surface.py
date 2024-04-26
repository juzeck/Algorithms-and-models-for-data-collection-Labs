import matplotlib.pyplot as plt
import numpy as np


def my_function(x, y):
    return 10 * x ** 3 * np.sin(y) ** 2 - 2 * x ** 2 * y ** 3


fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)
Z = my_function(X, Y)

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Графік поверхні та функція')

ax.text2D(0.05, 0.95, r'$z = 10X^3\sin^2(y)-2x^2y^3$', transform=ax.transAxes, fontsize=12)

plt.show()

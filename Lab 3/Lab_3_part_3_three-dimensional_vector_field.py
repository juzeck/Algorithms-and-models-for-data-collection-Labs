import matplotlib.pyplot as plt
import numpy as np


def calculate_vector_field(x, y, z):
    with np.errstate(divide='ignore', invalid='ignore'):
        Fx = y - np.where(x == 0, np.nan, z / x ** 2)
        Fy = x + (1 / z)
        Fz = np.where(x == 0, np.nan, 1 / x) - np.where(z == 0, np.nan, y / z ** 2)
    return Fx, Fy, Fz


def plot_vector_field(x, y, z, Fx, Fy, Fz):
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.quiver(x, y, z, Fx, Fy, Fz, length=1, normalize=True, color='black')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_title('F = (y - (z / x^2), x + (1 / z), (1 / x) - (y / z^2))')
    plt.show()


# Створення сітки даних
x_range = np.linspace(-3, 6, 10)
y_range = np.linspace(-3, 6, 10)
z_range = np.linspace(-3, 6, 3)
X, Y, Z = np.meshgrid(x_range, y_range, z_range)

# Обчислення векторного поля
Fx, Fy, Fz = calculate_vector_field(X, Y, Z)

# Візуалізація векторного поля
plot_vector_field(X, Y, Z, Fx, Fy, Fz)

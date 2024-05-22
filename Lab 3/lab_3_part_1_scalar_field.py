import numpy as np
import matplotlib.pyplot as plt

# Задаємо діапазони значень x та y
x = np.linspace(-3, 6, 100)
y = np.linspace(-3, 6, 100)

# Створюємо сітку точок для побудови візуалізації
X, Y = np.meshgrid(x, y)

# Обчислюємо значення скалярного поля
u = -2 * np.log(X**2 + 5) - 4*X*Y

# Візуалізуємо скалярне поле за допомогою пкалорграми
fig, ax = plt.subplots(figsize=(8, 6))
cp = ax.contourf(X, Y, u, cmap='viridis')
fig.colorbar(cp)
ax.set_title('Візуалізація скалярного поля')
ax.set_xlabel('x')
ax.set_ylabel('y')

# Обчислюємо градієнт скалярного поля
du_dx = -4*X/((X**2)+5) - 4*Y
du_dy = -4*X

# Створюємо векторне поле з компонентів градієнта
U = du_dx
V = du_dy

# Візуалізуємо градієнт як векторне поле
fig, ax = plt.subplots(figsize=(8, 6))
q = ax.quiver(X, Y, U, V)
ax.set_title('Візуалізація градієнта скалярного поля')
ax.set_xlabel('x')
ax.set_ylabel('y')

plt.show()
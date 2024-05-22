import numpy as np
import matplotlib.pyplot as plt

# Визначаємо функції компонентів векторного поля
def u(x, y):
    return x + 2*y**2

def v(x, y):
    return y + 2*x**2

# Задаємо діапазони значень x та y
x = np.linspace(-3, 6, 20)
y = np.linspace(-3, 6, 20)

# Створюємо сітку точок для побудови візуалізації
X, Y = np.meshgrid(x, y)

# Обчислюємо компоненти векторного поля
U = u(X, Y)
V = v(X, Y)

# Візуалізація векторного поля за допомогою стрілок
fig, ax = plt.subplots(figsize=(8, 6))
q = ax.quiver(X, Y, U, V)
ax.set_title('Візуалізація векторного поля (стрілки)')
ax.set_xlabel('x')
ax.set_ylabel('y')

# Візуалізація векторного поля за допомогою ліній струму
fig, ax = plt.subplots(figsize=(8, 6))
strm = ax.streamplot(X, Y, U, V, density=1.5, arrowstyle='->')
ax.set_title('Візуалізація векторного поля (лінії струму)')
ax.set_xlabel('x')
ax.set_ylabel('y')

plt.show()
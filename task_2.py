import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt

# Визначення функції, що інтегрується
def f(x):
    return x ** 2

# Аналітичне обчислення інтеграла
integral_value, _ = quad(f, 0, 2)

# Метод Монте-Карло
N = 10000  # Кількість випробувань
x_random = np.random.uniform(0, 2, N)
y_random = np.random.uniform(0, f(2), N)
points_under_curve = np.sum(y_random < f(x_random))
monte_carlo_integral = (2 * f(2)) * (points_under_curve / N)

# Виведення результатів
print(f"Аналітичне обчислення інтеграла: {integral_value}")
print(f"Метод Монте-Карло: {monte_carlo_integral}")

# Візуалізація
x = np.linspace(-0.5, 2.5, 400)
y = f(x)
fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)
ix = np.linspace(0, 2)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=0, color='gray', linestyle='--')
ax.axvline(x=2, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від 0 до 2')
plt.grid()
plt.show()

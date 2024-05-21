import numpy as np
from scipy.integrate import quad

def monte_carlo_integration(f, a, b, n):
    # Генеруємо n випадкових точок в інтервалі [a, b]
    x_random = np.random.uniform(a, b, n)
    
    # Обчислюємо значення функції f(x) для кожної випадкової точки
    f_values = f(x_random)
    
    # Обчислюємо середнє значення f(x)
    mean_f_value = np.mean(f_values)
    
    # Множимо середнє значення на довжину інтервалу [a, b]
    integral = (b - a) * mean_f_value
    
    return integral

# Функція, яку будемо інтегрувати
def f(x):
    return np.sin(x)

# Межі інтеграції
a = 0
b = np.pi

# Кількість випадкових точок
n = 100000

# Обчислення інтегралу методом Монте-Карло
integral_mc = monte_carlo_integration(f, a, b, n)
print(f"Наближене значення інтегралу методом Монте-Карло: {integral_mc}")

# Обчислення інтегралу за допомогою функції quad
integral_quad, quad_error = quad(f, a, b)
print(f"Значення інтегралу за допомогою функції quad: {integral_quad}")
print(f"Оцінка абсолютної похибки функції quad: {quad_error}")

# Аналітичне значення інтегралу
integral_analytical = 2
print(f"Аналітичне значення інтегралу: {integral_analytical}")


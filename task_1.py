from pulp import *

# Оголошення проблеми
problem = LpProblem("Оптимізація_виробництва_напоїв", LpMaximize)

# Оголошення змінних
lemonade = LpVariable("Лимонад", 0, None, LpInteger)
fruit_juice = LpVariable("Фруктовий_сік", 0, None, LpInteger)

# Цільова функція
problem += lemonade + fruit_juice, "Загальне_виробництво"

# Обмеження
problem += 2 * lemonade + 1 * fruit_juice <= 100, "Обмеження_води"
problem += 1 * lemonade <= 50, "Обмеження_цукру"
problem += 1 * lemonade <= 30, "Обмеження_лимонного_соку"
problem += 2 * fruit_juice <= 40, "Обмеження_фруктового_пюре"

# Вирішення проблеми
problem.solve()

# Виведення результатів
print("Одиниць виробництва Лимонаду:", lemonade.varValue)
print("Одиниць виробництва Фруктового соку:", fruit_juice.varValue)
print("Максимальне загальне виробництво:", lemonade.varValue + fruit_juice.varValue)
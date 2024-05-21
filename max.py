import pulp

# Створення проблеми лінійного програмування
problem = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

# Змінні для кількості виробленого Лимонаду і Фруктового соку
lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')
fruit_juice = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Integer')

# Функція цільової оптимізації (максимізація загальної кількості вироблених продуктів)
problem += lemonade + fruit_juice, "Total_Products"

# Обмеження на ресурси
problem += 2 * lemonade + 1 * fruit_juice <= 100, "Water_Constraint"
problem += 1 * lemonade <= 50, "Sugar_Constraint"
problem += 1 * lemonade <= 30, "Lemon_Juice_Constraint"
problem += 2 * fruit_juice <= 40, "Fruit_Puree_Constraint"

# Рішення проблеми
problem.solve()

# Вивід результатів
print(f"Status: {pulp.LpStatus[problem.status]}")
print(f"Лимонад: {lemonade.varValue}")
print(f"Фруктовий сік: {fruit_juice.varValue}")

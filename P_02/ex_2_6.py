"""
Приклад 2.6. Скласти програму для знаходження найбільшого з трьох значень, введених з клавіатури.
"""

x = float(input("x = "))
y = float(input("y = "))
z = float(input("z = "))
# Визначаємо більше серед чисел x та y
if x < y:
    max = y
else:
    max = x
# Визначаємо більше серед чисел max(x,y) та z.
if max < z:
    max = z
print("max(", x, y, z, ")= ", max)





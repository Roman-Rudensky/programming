"""
Приклад 1.1. Знайти суму цифр двозначного числа.
Розв’язок. Нехай x – задане двозначне число, наприклад 25.
Сума цифр цього числа є сумою першої та другої цифр цього числа: 2 + 5 = 7.
Першу цифру цього числа можна знайти як ділення числа x націло на 10.
Друга ж цифра цього числа є остачею від ділення числа x на 10.
"""

x = int(input("Введіть двозначне число "))
first = x // 10  # first - перша цифра числа
second = x % 10  # second - друга цифра числа
suma = first + second
print("Сума цифр числа %d = %d" % (x, suma))

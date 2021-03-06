"""
Приклад 3.4. Написати програму для обчислення найбільшого спільного дільника двох цілих чисел за допомогою алгоритма Евкліда.

"""

N = int(input("Введіть перше число "))
M = int(input("Введіть друге число "))

# Запам'ятовуємо вхідні змінні
U = N
V = M
# Модифікуємо змінні U та V так, щоб в
# U було більше число, а у V - менше
if U < V:
    P = U
    U = V
    V = P
# Запускаємо алгорим Евкліда
while V > 0:
    P = V
    V = U % V
    U = P
# Виводимо результат на екран
print("НСД(%d, %d) = %d" % (N, M, U))






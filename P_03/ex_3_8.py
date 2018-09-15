"""
Приклад 3.8. Нехай задано натуральне число n>=1 і послідовність чисел a_1,…,a_n.
Знайти max(a_1,…,a_n ).

"""
N = int(input("N = "))
# Зчитуємо 1-й член послідовності
a = float(input("Задайте член послідовності = "))

max = a               # Вважаємо, що він є найбільшим
for i in range(1, N): # Цикл виконається рівно N-1 раз
    a = float(input("Уведіть член послідовності"))
    # У змінну max записуємо більше з числем max і
    # поточного члена зчитаного з клавіатури
    max = a if a > max else max

print("Найбільшим є число", max)

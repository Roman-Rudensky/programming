"""
Приклад 3.5. Знайти суму парних чисел з діапазону від 1 до N.

"""

N = int(input("N = "))
suma = 0
for i in range(2, N + 1, 2):
    suma += i
print("Сума парних чисел від 1 до %d є %d" % (N, suma))







"""
Приклад 3.9. Написати програму для обчислення подвійного факторіала натурального числа n : y=n!!
"""

n = int(input("n = "))

p = 1
for k in range(n, 0, -2):
    p = p * k

print("%d!! = %d" % (n, p))


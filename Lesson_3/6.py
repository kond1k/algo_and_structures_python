"""
6.	В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""
import random

z = []
for i in range(15):
    z.append(random.randint(1, 100))

max_i = 0
min_i = 0
for i in range(len(z)):
    if z[i] > z[max_i]:
        max_i = i
    if z[i] < z[min_i]:
        min_i = i
if min_i >= max_i:
    s = -1
else:
    s = 1
print(z)
print(min_i, max_i)
print(sum(z[min_i:max_i - 1:s]))

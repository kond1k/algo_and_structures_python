# 3.	В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.
import random

z = []
for i in range(15):
    z.append(random.randint(1, 100))

max_e = z[0]
min_e = z[0]
max_i = 0
min_i = 0
for i in range(len(z)):
    if z[i] > max_e:
        max_e = z[i]
        max_i = i
    if z[i] < min_e:
        min_e = z[i]
        min_i = i
# это алгоритм нахождения макс и мин, чтобы не захломлять код в дальнейшем я использую встроенные функции max и min
print(z)
z[max_i], z[min_i] = z[min_i], z[max_i]
print(z)

# 9.	Найти максимальный элемент среди минимальных элементов столбцов матрицы.
import random

z = []
for i in range(4):
    z.append([])
    for j in range(4):
        z[i].append(random.randint(1, 100))

y = []
x = []
for i in range(len(z)):
    y.append([])
    for j in range(len(z)):
        y[i].append(z[j][i])
    x.append(min(y[i]))

print(max(x))

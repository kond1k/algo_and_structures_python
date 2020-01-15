# 5.	В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.

import random

z = []
for i in range(15):
    z.append(random.randint(-100, 100))

print(max([i for i in z if i < 0]))

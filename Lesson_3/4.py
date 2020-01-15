# 4.	Определить, какое число в массиве встречается чаще всего.
import random

z = []
for i in range(200):
    z.append(random.randint(1, 10))
m = {}
for i in z:
    if i in m.keys():
        m[i] += 1
    else:
        m[i] = 1

print(m)
print([i for i, j in m.items() if max(m.values()) == j])

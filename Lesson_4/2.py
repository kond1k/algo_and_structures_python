from timeit import Timer

"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
"""


def without_er(n):
    num_f = 2
    count = 1
    while True:
        check = 2
        simple = True
        num_f += 1
        while check < num_f:
            if num_f % check == 0:
                simple = False
            check += 1
        if simple:
            count += 1
            if count == n:
                return num_f


def with_er(n):
    a = [0] * 1000
    for i in range(1000):
        a[i] = i
    a[1] = 0
    m = 2
    while m < 1000:
        if a[m] != 0:
            j = m * 2
            while j < 1000:
                a[j] = 0
                j = j + m
        m += 1

    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])

    del a
    return b[n - 1]


t1 = Timer("without_er(99)", "from __main__ import without_er")
print("without ", t1.timeit(number=300), "milliseconds")

t2 = Timer("with_er(99)", "from __main__ import with_er")
print("with ", t1.timeit(number=300), "milliseconds")

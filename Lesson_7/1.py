"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""

import timeit
import random


def bubble_sort(my_list):
    n = 1
    while n < len(my_list):
        for i in range(len(my_list) - n):
            if my_list[i] < my_list[i + 1]:
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
        n += 1
    return my_list


def bubble_sort_mod(my_list):
    n = 1
    while n < len(my_list):
        count = 0
        for i in range(len(my_list) - n):
            if my_list[i] < my_list[i + 1]:
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
            else:
                count += 1
        n += 1
        if count == len(my_list) - 1:
            break
    return my_list


orig_list = [random.randint(-100, 100) for _ in range(100)]
print(orig_list)
# замеры 100 обычная сортировка
print(timeit.timeit("bubble_sort(orig_list)",
                    setup="from __main__ import bubble_sort, orig_list", number=1000))
print(orig_list)

orig_list = [random.randint(-100, 100) for _ in range(100)]
print(orig_list)
# замеры 100 модифицированная сортировка
print(timeit.timeit("bubble_sort_mod(orig_list)",
                    setup="from __main__ import bubble_sort_mod, orig_list", number=1000))
print(orig_list)
# Модифицированный вариант работает в десятки раз быстрее

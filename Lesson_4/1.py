from timeit import Timer

"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""

""" 
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.

"""


def from_end_to_start_rek(num):
    if num / 10 < 1:
        return num
    return num % 10 * (10 ** (len(str(num)) - 1)) + from_end_to_start_rek(num // 10)


def from_end_to_start_cycle(num):
    z = ''
    while num:
        z += str(num % 10)
        num //= 10
    return z


t1 = Timer("from_end_to_start_rek(1234567)", "from __main__ import from_end_to_start_rek")
print("rek ", t1.timeit(number=1000000), "milliseconds")

t2 = Timer("from_end_to_start_cycle(1234567)", "from __main__ import from_end_to_start_cycle")
print("cycle ", t2.timeit(number=1000000), "milliseconds")

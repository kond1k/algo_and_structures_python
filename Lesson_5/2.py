"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры
числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""
import collections


def hex_val(num):
    hex_v = 0
    for i in range(len(num)):
        hex_v += int(num[i], 16) * (16 ** (len(num) - i - 1))
    return hex_v


dict_h = collections.defaultdict(list)
a = input("Введите первое число\n")
b = input("Введите второе число\n")
dict_h[a] = list(a)
dict_h[b] = list(b)

sum_h = str(hex(hex_val(dict_h[a]) + hex_val(dict_h[b])))[2::]
multi_h = str(hex(hex_val(dict_h[a]) * hex_val(dict_h[b])))[2::]
dict_h[sum_h] = list(sum_h)
dict_h[multi_h] = list(multi_h)

print(f"Сумма чисел {dict_h[sum_h]}, Произведение {dict_h[multi_h]}")

"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.
"""


def from_end_to_start(num):
    if num / 10 < 1:
        return num
    return num % 10 * (10 ** (len(str(num))-1)) + from_end_to_start(num // 10)


print(from_end_to_start(345678999))

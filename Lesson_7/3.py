"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
 который не рассматривался на уроках
"""
import random


def bubble_sort(sorted_list):
    n = 1
    while n < len(sorted_list):
        for i in range(len(sorted_list) - n):
            if sorted_list[i] < sorted_list[i + 1]:
                sorted_list[i], sorted_list[i + 1] = sorted_list[i + 1], sorted_list[i]
        n += 1
    return sorted_list


m = int(input("Введите m\n"))
my_list = [random.randint(-100, 100) for _ in range(2 * m + 1)]

for i in range(len(my_list)):
    i_bigger = []
    i_smaller = []
    for j in range(len(my_list)):
        if i != j:
            if my_list[i] > my_list[j]:
                i_bigger.append(my_list[j])
            if my_list[i] < my_list[j]:
                i_smaller.append(my_list[j])
    if len(i_bigger) == len(i_smaller):
        print(my_list[i])
        break
print(my_list)

print(bubble_sort(my_list))

# 5.	Пользователь вводит две буквы. Определить, на каких местах
# алфавита они стоят, и сколько между ними находится букв.
import math

first_char = ord(input('Введите первую букву\n'))
second_char = ord(input('Введите вторую букву\n'))

if second_char < first_char:
    sign = 1
else:
    sign = +1

print(f'Первая буква стоит на метсе {first_char - 96}, вторая буква стоит на метсе {second_char - 96},'
      f' между ними {abs(first_char - second_char + sign)} букв')

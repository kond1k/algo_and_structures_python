"""
2*. Определение количества различных подстрок с использованием хэш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.
"""
import hashlib

string = input("Введите строку из малньких латинских букв\n")

s = set()
count = len(string)

for i in range(len(string)):
    if i == 0:
        count = len(string) - 1
    else:
        count = len(string)
    for j in range(count, i, -1):
        print(string[i:j])
        s.add(hashlib.sha1(string[i:j].encode('utf-8')).hexdigest())
print(s)

print(f"Разных подстрок в стровке {string} равно {len(s)}")


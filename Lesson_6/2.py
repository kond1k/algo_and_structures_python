"""
2. Создать пользовательский класс данных (или использовать) один из классов,
реализованных в курсе Python.Основы. Реализовать класс с применением слотов
и обычным способом. Для объекта обычного класса проверить отображение словаря
атрибутов. Сравнить, сколько выделяется памяти для хранения атрибутов обоих
классов.
"""
from pympler import asizeof


class MySimpleClass:
    pass


class MySlotClass:
    __slots__ = ('a', 'b', 'c')

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


simple = MySimpleClass()
simple.a = 123
simple.b = 456
simple.c = 789

slot = MySlotClass(123, 456, 789)

print(simple.__dict__)
print(asizeof.asizeof(simple))
print(asizeof.asizeof(slot))
# На экземпляр класса со слотом тратиться почти в 3 раза меньше памяти

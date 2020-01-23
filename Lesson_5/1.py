"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""
import collections

count = int(input("Введите колличество предприятий\n"))
Company = collections.namedtuple('Company', ['name', 'profit'])
company_list = []
for i in range(count):
    name_c = input(f"Введите название {i + 1} Компании\n")
    profit = [int(i) for i in input(f"Введите прибыль {name_c} за 4 квартала через пробел\n").split()]
    company_list.append(Company(name=name_c, profit=sum(profit) / 4))

profit_sum = 0
for i in company_list:
    profit_sum += i.profit
avg = profit_sum / len(company_list)
print(f"Средняя прибыль {company_list}")
print(f"Средняя прибыль всех компаний {avg}")
print(f"Выше среднего {[i for i in company_list if i.profit > avg]}")
print(f"Ниже среднего{[i for i in company_list if i.profit < avg]}")

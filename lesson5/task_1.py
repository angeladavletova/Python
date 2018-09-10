from collections import namedtuple

Company = namedtuple('Company', 'name profit1 profit2 profit3 profit4 total_profit')
n = int(input('Введите количество предприятий: '))

company_list = []
for i in range(n):
    name = input('Введите наименование предприятия: ')
    print('Введите прибыль за 4 квартала')
    profit1 = int(input('Прибыль за первый квартал:'))
    profit2 = int(input('Прибыль за второй квартал:'))
    profit3 = int(input('Прибыль за третий квартал:'))
    profit4 = int(input('Прибыль за четвертый квартал:'))
    total_profit = profit1 + profit2 + profit3 + profit4
    company_list.append(Company(name, profit1, profit2, profit3, profit4, total_profit))
    print('-' * 40)

sum_profit = 0
for company in company_list:
    sum_profit += company.total_profit
average_profit = sum_profit / n

print('Предпрития с прибылью выше среднего:')
for company in company_list:
    if company.total_profit > average_profit:
        print(company.name)

print('Предпрития с прибылью не выше среднего:')
for company in company_list:
    if company.total_profit <= average_profit:
        print(company.name)
# 4. Определить, какое число в массиве встречается чаще всего.

import random

LIMIT = 10
SIZE = 20
array = [random.randint(0, LIMIT) for _ in range(SIZE)]
print(array)

max_count = 0
num = 0
for el in array:
    count_ = array.count(el)
    if max_count < count_:
        max_count = count_
        num = el

print('Чаще всего встречается число', num)

# способ 2 с дополнительной памятью
dict_count = {}

for el in array:
    dict_count.setdefault(el, 0)
    dict_count[el] += 1

max_count = 0
num = 0
for key, value in dict_count.items():
    if value > max_count:
        max_count = value
        num = key

print('Чаще всего встречается число', num, '(способ 2)')

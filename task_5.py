# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random

LIMIT = 100
SIZE = 10
array = [random.randint(-LIMIT, LIMIT) for _ in range(SIZE)]
print(array)

max_neg_el = 0
max_neg_index = 0

for i in range(SIZE):
    if array[i] < 0 and (max_neg_el < array[i] or max_neg_el == 0):
        max_neg_el = array[i]
        max_neg_index = i

if max_neg_el < 0:
    print('Элемент', max_neg_el, 'на позиции', max_neg_index)
else:
    print('Все елементы неотрицательные')
# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

LIMIT = 100
SIZE = 10
array = [random.randint(0, LIMIT) for _ in range(SIZE)]
print(array)

max_el = min_el = array[0]
max_index = min_index = 0

for i in range(SIZE):
    if array[i] > max_el:
        max_el = array[i]
        max_index = i
    if array[i] < min_el:
        min_el = array[i]
        min_index = i

array[max_index], array[min_index] = array[min_index], array[max_index]
print(array)
# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

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

print(sum(array[min_index + 1:max_index]) or sum(array[max_index + 1:min_index]))




# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

LIMIT = 10
SIZE = 10
array = [random.randint(0, LIMIT) for _ in range(SIZE)]
print(array)

min1 = array[0]
min2 = array[1]

for i in range(1, SIZE):
    if array[i] <= min1:
        min2 = min1
        min1 = array[i]
    elif array[i] < min2:
        min2 = array[i]

print(min1, min2)

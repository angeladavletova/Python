# 2. Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив
# со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 0, 3, 4, 5.

import random

LIMIT = 100
SIZE = 10
array = [random.randint(0, LIMIT) for _ in range(SIZE)]
indices = []

for i in range(SIZE):
    if array[i] % 2 == 0:
        indices.append(i)

print(array)
print(indices)
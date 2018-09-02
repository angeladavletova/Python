# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random
ROW = 3
COLUMN = 4
matrix = [[random.randint(1, 10) for _ in range(COLUMN)] for _ in range(ROW)]
for line in matrix:
    print(line)

min_el = matrix[0]
for row in matrix:
    for i, item in enumerate(row):
        if item < min_el[i]:
            min_el[i] = item

max = min_el[0]
for el in min_el:
    if max < el:
        max = el

print('Максимальный элемент среди минимальных элементов столбцов матрицы равен', max)


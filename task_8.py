# 8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк. Программа должна вычислять сумму
# введенных элементов каждой строки и записывать ее в ее последнюю ячейку. В конце следует вывести полученную матрицу.

ROW = 5
COLUMN = 4
array = []
print('Последовательно заполните матрицу размером 5x3')
for i in range(ROW):
    sum_line = 0
    for j in range(COLUMN - 1):
        a = int(input('строка {}, столбец {}: '.format(i + 1, j + 1)))
        array.append(a)
        sum_line += a
    array.append(sum_line)


def print_matrix(matrix, n, m):
    for i in range(n):
        for j in range(m):
            print('{:>5}'.format(matrix[i * m + j]), end = ' ')
        print()

print_matrix(array, ROW, COLUMN)

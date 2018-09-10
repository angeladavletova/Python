from collections import deque

NOTATION = 16

d = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12,
     'D': 13, 'E': 14, 'F': 15}
c = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
     13: 'D', 14: 'E', 15: 'F'}

a = list(input('Введите первое число в шестнадцатеричной системе счисления: ')) # ['C', '4', 'F']
b = list(input('Введите второе число в шестнадцатеричной системе счисления: ')) # ['A', '2']

def sum_16(a, b):
    len_a = len(a)
    len_b = len(b)
    n = max(len_a, len_b)
    res_sum = deque()
    transfer = 0
    for i in range(-1, -n - 1, -1):
        if -i > len_a:
            s = d[b[i]] + transfer
        elif -i > len_b:
            s = d[a[i]] + transfer
        else:
            s = d[a[i]] + d[b[i]] + transfer

        transfer = s // NOTATION
        curr_sum = s % NOTATION
        res_sum.appendleft(c[curr_sum])

    return list(res_sum)

print('Сумма =', sum_16(a, b))

prod = []
res_prod = 0
len_a = len(a)
len_b = len(b)
for i in range(len_b):
    curr_prod = deque()
    transfer = 0
    for j in range(len_a):
        p = d[a[len_a - j - 1]] * d[b[len_b - i - 1]] + transfer
        transfer = p // NOTATION
        curr_prod.appendleft(c[p % NOTATION])
    if transfer != 0:
        curr_prod.appendleft(c[transfer])
    prod.append(curr_prod)

res_prod = ['0']
for i in range(len_b):
    a = list(prod[i]) + ['0'] * i
    res_prod = sum_16(a, res_prod)

print('Произведение =', res_prod)
import random
import cProfile
import timeit

LIMIT = 10
SIZE = 10000
array = [random.randint(0, LIMIT) for _ in range(SIZE)]

#--------------------------------------------

# 100 loops, best of 3: 10.8 usec per loop - SIZE = 10
# 100 loops, best of 3: 31.5 usec per loop - SIZE = 100
# 100 loops, best of 3: 266 usec per loop  - SIZE = 1 000
# 100 loops, best of 3: 2.29 msec per loop - SIZE = 10 000

# сложность алгоритма O(n logn), доп память O(n)

def find_max_count1():
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

    print(num)

#--------------------------------------------

# 100 loops, best of 3: 16.1 usec per loop - SIZE = 10
# 100 loops, best of 3: 640 usec per loop  - SIZE = 100
# 100 loops, best of 3: 54 msec per loop   - SIZE = 1 000

# сложность алгоритма O(n ** 2), доп память O(1)

def find_max_count2():
    num = array[0]
    max_frq = 1
    for i in range(SIZE - 1):
        frq = 1
        for k in range(i + 1, SIZE):
            if array[i] == array[k]:
                frq += 1
        if frq > max_frq:
            max_frq = frq
            num = array[i]

    if max_frq > 1:
        print(num)
    else:
        print('All items are unique')

#--------------------------------------------

# 100 loops, best of 3: 2.36 usec per loop - SIZE = 10
# 100 loops, best of 3: 118 usec per loop  - SIZE = 100
# 100 loops, best of 3: 11.3 msec per loop - SIZE = 1 000

# сложность алгоритма O(n ** 2), доп память O(1)
# работает быстрее перебора с помощью for из-за использования встроенной функции count

def find_max_count3():
    max_count = 0
    num = 0
    for el in array:
        count_ = array.count(el)
        if max_count < count_:
            max_count = count_
            num = el

    print(num)

#--------------------------------------------

# cProfile.run('find_max_count1()')
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.003    0.003    0.004    0.004 task_4.py:12(find_max_count1) - 10 000
#        1    7.033    7.033    7.033    7.033 task_4.py:29(find_max_count2) - 10 000
#        1    0.003    0.003    2.022    2.022 task_4.py:46(find_max_count3) - 10 000

find_max_count1()
find_max_count2()
find_max_count3()
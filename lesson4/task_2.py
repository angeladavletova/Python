import math
import cProfile
import timeit

#idx = int(input('Введите порядковый номер простого числа: '))

# Нахождение i-ого числа с помощью решета Эратосфена
#
# Гипотеза Лежандра:
# для любого n >= 2 найдётся простое число p в интервале n ** 2 < p < (n + 1) ** 2.
# Тогда i-ое простое будет меньше, чем (i + 2) ** 2
#
# 100 loops, best of 3: 51.3 usec per loop - 10
# 100 loops, best of 3: 3.95 msec per loop - 100
# 100 loops, best of 3: 204 msec per loop  - 500
def search_prime_number_with_sieve(idx):
    n = (idx + 2) ** 2
    sieve = [i for i in range(n)]
    sieve[1] = 0

    for i in range(2, n):
        if sieve[i] != 0:
            j = i * 2
            while j < n:
                sieve[j] = 0
                j += i

    res = [i for i in sieve if i != 0]
    print(res[idx - 1])

# Нахождение i-ого простого числа без использования "решета"
#
# 100 loops, best of 3: 74.4 usec per loop - 10
# 100 loops, best of 3: 667 usec per loop  - 100
# 100 loops, best of 3: 6.29 msec per loop - 500
# 100 loops, best of 3: 17 msec per loop   - 1000
def is_prime(n):
    if n == 1:
        return False
    for d in range(2, int(math.sqrt(n)) + 1):
        if n % d == 0:
            return False
    return True

def search_prime_number(idx):
    num = 1
    count = 0
    while count < idx:
        if is_prime(num):
            count += 1
        num += 1
    print(num - 1)

# cProfile.run('search_prime_number(1000)')
#        1    0.564    0.564    0.695    0.695 task_2.py:5(search_prime_number_with_sieve) - 1000
#        1    0.002    0.002    0.022    0.022 task_2.py:31(search_prime_number)           - 1000

#search_prime_number(idx)
#search_prime_number_with_sieve(idx)
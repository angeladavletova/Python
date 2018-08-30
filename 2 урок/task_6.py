# 6. В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за
# 10 попыток. После каждой неудачной попытки должно сообщаться, больше или меньше загаданного введенное
# пользователем число. Если за 10 попыток число не отгадано, то вывести его.

import random

print('Угадайте число от 0 до 100')

n = random.randint(0, 100)
i = 0
step = 10
while i < step:
    m = int(input('Введите число: '))
    if m < n:
        print('Введенное число меньше загаданного')
    elif m > n:
        print('Введенное число больше загаданного')
    else:
        print('Правильно!')
        break
    i += 1
else:
    print('Попытки закончились. Загаданное число', n)
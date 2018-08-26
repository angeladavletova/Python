# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

print ('Введите три разных числа')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if (a > b and a < c) or (a > c and a < b):
    print('Среднее число', a)
elif (b > a and b < c) or (b > c and b < a):
    print('Среднее число', b)
else:
    print('Среднее число', c)







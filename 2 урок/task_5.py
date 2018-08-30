# 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар «код-символ» в каждой строке.

start = 32
end = 128
column = 10
row = str()
while start < end:
    for i in range(min(10, end - start)):
        row += str(start + i) + ' - ' + chr(start + i) + '    '
    print(row)
    row = str()
    start += column

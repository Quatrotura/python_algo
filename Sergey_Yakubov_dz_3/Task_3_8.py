# 3.8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

# Андрей, проверки при пользовательском вводе не делал. Думаю из прошлых дз понятно, что я их умею делать :-)

a = []
MATRIX_SIZE = 5
for i in range(MATRIX_SIZE - 1):
    line_sum = 0
    line = input(f'Введите четыре числа для {i+1} строки через пробел:\n')
    a.append(list(map(int, line.split())))
    for j in a[i]:
        line_sum += j
    a[i].append(line_sum)

[print(a[i]) for i in range(len(a))]

# реализация с рандомным неручным наполнением:

print('~' * 20)
from random import random

MATRIX_SIZE = 5

a = []
for i in range(MATRIX_SIZE - 1):
    b = []
    row_sum = 0
    for j in range(MATRIX_SIZE - 1):
        b.append(int(random()*10))
        row_sum += b[j]
    b.append(row_sum)
    a.append(b)
    print(a[i])

# вид вывода:
# [1, 2, 3, 4, 10]
# [5, 6, 7, 8, 26]
# [5, 2, 1, 9, 17]
# [3, 0, 1, 6, 10]
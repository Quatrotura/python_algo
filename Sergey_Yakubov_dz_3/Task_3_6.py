# 3.6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

from random import random

a = []
for i in range(10):
    a.append(int(random()*20))

max_n = a[0]
min_n = a[0]
min_n_pos = 0
max_n_pos = 0
max_min_between_sum = 0

for i in range(len(a)):
    if a[i] > max_n:
        max_n = a[i]
        max_n_pos = i
    elif a[i] < min_n:
        min_n = a[i]
        min_n_pos = i

if max_n_pos < min_n_pos:
    max_n_pos, min_n_pos = min_n_pos, max_n_pos

for i in range(min_n_pos+1, max_n_pos):
    max_min_between_sum += a[i]

print(a)
print(f'Первое минимальное число {min_n}, первое максимальное число {max_n}, сумма чисел между ними {max_min_between_sum}.')




# 3.7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.
# т.к. в задаче не уточнили, будем исходить из того, что надо найти первые два наименьших элемента

from random import random
a = []
for i in range(30):
    a.append(int(random() * 300))

min_n_1 = a[0]
min_n_2 = a[0]
min_n_1_pos = 0

for i in range(len(a)):
    if a[i] < min_n_1:
        min_n_1 = a[i]
        min_n_1_pos = i
    if a[i] > min_n_2:
        min_n_2 = a[i]  # пока будем записывать сюда максимальное число

for j in range(len(a)):
    if a[j] < min_n_2 and j != min_n_1_pos and a[j] >= min_n_1:
        min_n_2 = a[j]

# print(a)
# print(sorted(a)) # для проверки
print(f'Первые два минимальных числа: {min_n_1}, {min_n_2}.')

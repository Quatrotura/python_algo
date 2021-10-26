# 3.3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
# со звездочкой
# пример Андрея [0, 0, 1, 2, 3, 3, 3]
#               [3, 3, 1, 2, 0, 0, 0]

from random import randint

a = []
for i in range(20):
    a.append(randint(0, 8))

min_n = a[0]
max_n = a[0]

for i in range(1, len(a)):  # элемент a[0] прогонять не надо, мы изначально присвоили min_n значение этого элемента
    if a[i] <= min_n:
        min_n = a[i]
    elif a[i] >= max_n:
        max_n = a[i]

print(min_n, max_n)
print(a)

for i in range(len(a)):
    if max_n == a[i]:
        a[i] = min_n
    elif min_n == a[i]:
        a[i] = max_n
print(a)

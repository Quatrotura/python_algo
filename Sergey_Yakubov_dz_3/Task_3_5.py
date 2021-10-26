# 3.5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.
# * если элементов несколько, то выводим инфу по всем

from random import randint
a = []
for i in range(40):
    a.append(randint(-10, 10))

print(a)

max_negative = min(a)
max_negative_pos = []
for i in range(len(a)):
    if 0 > a[i] >= max_negative:
        max_negative = a[i]

# честно говоря не придумал ничего более оригинального
# кроме такого очевидного решения со вторым циклом...

for i in range(len(a)):
    if max_negative == a[i]:
        max_negative_pos.append(i)

print(f'Максимальный отрицательный элемент {max_negative}. Его индексы: {max_negative_pos}')
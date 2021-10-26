# 3.4. Определить, какое число в массиве встречается чаще всего.

from random import randint
a = []
for i in range(20):
    a.append(randint(0, 7))
print(a)

b = []
already = set()
for i in range(len(a)):
    counter = 1
    b.append([])
    if a[i] not in already:  # чтобы вхолостую не запускал цикл, если след цифра уже была в подсчетах своих повторений
        for j in range(i+1, len(a)):
            if a[i] == a[j]:
                counter += 1
                already.add(a[i])
    b[i].append(a[i])
    b[i].append(counter)

c = b[:] # для экспериментов
e = b[:] # для экспериментов

b = sorted(b, key = lambda b: b[1], reverse = True)
print(f'Через sorted(). Максимальное количество повторений у цифры {b[0][0]}: {b[0][1]} повторений.')

# можно конечно обойтись без sorted для тренировки:

max_count = 0
max_count_number = 0
for i in range(len(a)):
    if c[i][1] > max_count: # если укажем >= то в итоге возвратится последнее число в списке b с наибольшими
        # повторениями, если чисел с максимально-одинаковыми повторениями много
        max_count = c[i][1]
        max_count_number = c[i][0]
print(f'Без sorted(), через поиск максимального числа. Максимальное количество повторений у цифры {max_count_number}: {max_count} повторений.')

# можно также и попробовать написать функцию реверсивной сортировки двумерного массива с учетом параметра key самостоятельно,
# для тренировочки
def sort_by_index(my_list, index):
    """ Функция принимает:

    - my_list: двумерный список,
    где my_list[0][0] - цифра из исходного списка, по которой мы считали повторения,
    а my_list[0][1] - количество повторений;

    - index: индекс list второго уровня по которому требуется сделать сортировку. """
    for i in range(len(my_list) - 1):
        for j in range(i+1, len(my_list)):
            if my_list[i][index] < my_list[j][index]:
                pos = j
                while pos > i:  # если делать простой перестановкой my_list[i], my_list[j] = my_list[j], my_list[i]
                                # то, цифры с одинаковым кол-вом повторений могут поменяться местами, что
                                # не соответствует требованию устойчивой сортировки
                    my_list[pos], my_list[pos-1] = my_list[pos-1], my_list[pos]
                    pos -= 1
    return my_list

d = sort_by_index(c,1)
print(f'Через самописную сортировку. Максимальное количество повторений у цифры {d[0][0]}: {d[0][1]} повторений.')

## проверочка работы sort_by_index со встроенной функцией sorted:
## e = sorted(e, reverse = True)
# e = sorted(e, key = lambda e: e[1], reverse = True)
# d = sort_by_index(c,1)
#
# for i in range(len(e)):
#     if e[i][0] == d[i][0] and e[i][1] == d[i][1]:
#         print(e[i],d[i], 'ok')
#     else:
#         print(e[i], d[i], 'not ok')
# Разберем задачу 3.3.
# 3.3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
# со звездочкой
# пример Андрея [0, 0, 1, 2, 3, 3, 3]
#               [3, 3, 1, 2, 0, 0, 0]

from random import randint
import cProfile

N = 99000
# наполнение списка случайными числами. Сложность линейная O(n). 20 чисел на входе - 20 итераций
a = []
for i in range(N):
    a.append(randint(0, 10000))

min_n = a[0]
max_n = a[0]

# Поиск максимального элемента.
# Операции присваивания не учитываем. Сложность линейная O(n).
# На входе список из n элементов и n итераций для поиска макс и мин числа
def list_max(n):
    max_n = 0
    for i in range(0, N):
        if a[i] >= max_n:
            max_n = a[i]
    return max_n


# Разберем задачу 3.4. Определить, какое число в массиве встречается чаще всего.

from random import randint
a = []
for i in range(N):
    a.append(randint(0, 10000))

b = []
already = set()

# Здесь, в худшем случае, и если убрать простенькое кэширование через запись во множество, сложность квадратичная O(n^2), т.к.
# тут два вложенных цикла, в каждом цикле кол-во итераций равно n (длине списка), соответственно всего n^2 итераций
# С кэшированием (ввел переменную iterations, за 30 запусков выдало максимум 143 итерации при n = 20 и аргументами в randint 0 и 7)
# будет примерно O((n^2)/3), если же увеличить множество рандомных чисел до 30, то сложность будет уже O((n^2)/2),
# то есть по сути та же квадратичная сложность только чуть более оптимизирована.

for i in range(len(a)):
    counter = 1
    b.append([])
    if a[i] not in already:
        for j in range(i+1, len(a)):
            if a[i] == a[j]:
                counter += 1
                already.add(a[i])
    b[i].append(a[i])
    b[i].append(counter)

c = b[:] # для экспериментов
e = b[:] # для экспериментов

# сделаем функцию для профайлера:
def get_sorted(calc_repeats):
    return sorted(calc_repeats, key = lambda calc_repeats: calc_repeats[1], reverse = True)

# cProfile.run('get_sorted(b)')
# при N = 99000
# 99005 function calls in 0.032 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.001    0.001    0.032    0.032 <string>:1(<module>)
#         1    0.000    0.000    0.031    0.031 Task_4_1.py:61(get_sorted)
#     99000    0.012    0.000    0.012    0.000 Task_4_1.py:62(<lambda>)
#         1    0.000    0.000    0.032    0.032 {built-in method builtins.exec}
#         1    0.019    0.019    0.031    0.031 {built-in method builtins.sorted}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# не знаю какую сортировку использует питон для ф-ции sorted, но если предположить, что не пузырьковую, то сложность самой быстрой
# устойчивой сортировки, которую мне удалось найти - O(nlogn), тогда вытащить число из сформированного массива с количеством повторений,
# будет дешевле и быстрее через поиск максимального числа чем через сортировку и вытаскивания первого элемента,
# т.к. поиск максимального числа - это один прогон по всем массиву, то есть линейная сложность в худшем случае O(n).
# Статистика профайлеров доказывает мое предположение (0.19 tottime при sorted() vs 0.11 tottime при поиске макс числа.

def get_max(calc_repeats, max_count = 0, max_count_number = 0):

    for i in range(len(calc_repeats)):
        if calc_repeats[i][1] > max_count:
            max_count = calc_repeats[i][1]
            max_count_number = calc_repeats[i][0]

    return f'{max_count_number}: {max_count}'

# cProfile.run('get_max(c)')
# при N = 99000
#  5 function calls in 0.011 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.011    0.011 <string>:1(<module>)
#         1    0.011    0.011    0.011    0.011 Task_4_1.py:83(get_max)
#         1    0.000    0.000    0.011    0.011 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# здесь ниже как оказалось у меня вроде пузырьковая сортировка, сложность O(n^2), то есть это наименее эффективный вариант
# статистика профайлера это доказывает
# достать из сформированного массива с количеством повторений число с максимальным количеством повторений (если предположить,
# что сложность sorted() - O(nlogn).

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

# cProfile.run('sort_by_index(c,1)')
#         99004 function calls in 830.943 seconds
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000  830.943  830.943 <string>:1(<module>)
#         1  830.844  830.844  830.943  830.943 Task_4_1.py:110(sort_by_index)
#         1    0.000    0.000  830.943  830.943 {built-in method builtins.exec}
#     99000    0.099    0.000    0.099    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Андрей, хотел у вас уточнить про сложность кода, представленного в методичке №3,
# реализуюзщий задачу обмена значений матрицы по главной и побочной диагоналям
# генерация матрицы:
from random import random
a = []
N = 500
for i in range(N):
    b = []
    for j in range(N):
        b.append(int(random() * 10))
    a.append((b))

# код из методички ниже. Сложность О(n^2) без учета проверки условия. Но с условием тут всегда (!) сложность будет O(2n)
# y = (x^2)/0.5x = 2x - это линейная фукнция. Правильно ли в данном случае оценивать сложность этого кода как O(2n)?
iterator = 0

for i in range(N):
    for j in range(N):
        if i == j:
            b = a[i][j]
            a[i][j] = a[i][N - 1 - j]
            a[i][N - 1 - j] = b

# В любом случае данный код можно оптимизировать до строго линейной сложности O(n) следующим образом:

for i in range(len(a)//2):
    a[i][i], a[i][len(a)-i-1] = a[i][len(a)-i-1], a[i][i]

for i in range(len(a)//2, len(a)):
    a[i][len(a)-i-1], a[i][i] = a[i][i], a[i][len(a)-i-1]

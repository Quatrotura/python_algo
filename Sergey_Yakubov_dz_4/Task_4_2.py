# 4.2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования Решета Эратосфена;
# Использовать алгоритм решето Эратосфена

# Без использования Решета Эратосфена, последовательный перебор делителей
# до первого третьего по счету делителя b (a%b == 0)
# сложность алгоритма O(n^2) стремится даже к O(n^3) от значения user_i

import cProfile

user_i = 4865 #i-го по счёту простого числа.

def not_eratosfen(user_i):

    i = 1
    prime_counter = 0  # счетчик простых чисел
    while True:
        divider = 1 # делитель
        counter_mod_oper_zero = 0 # считает кол-во делителей
        while counter_mod_oper_zero <= 2 and divider <= i:
            if i % divider == 0:
                counter_mod_oper_zero += 1
            divider += 1
        if counter_mod_oper_zero <= 2 and i != 1:
            prime_counter += 1
        if prime_counter == user_i:
            return i # возврат iтого по счету простого числа
        i += 1

cProfile.run('not_eratosfen(user_i)')
# 4 function calls in 25.232 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000   25.232   25.232 <string>:1(<module>)
#         1   25.232   25.232   25.232   25.232 Task_4_2.py:13(not_eratosfen)
#         1    0.000    0.000   25.232   25.232 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# решетом Эратосфена

# решето Эратосфена описывает алгоритм нахождения всех простых чисел до некоторого целого числа n (!!), то есть на входе надо задать длину списка,
# однако задача - найти i-е по счету простое число. В силу того, что у нас нет длины списка на входе, предположим, что длины списка 10i нам хватит для большинства случаев
# Исходя из статистики профайлера - предполагаю, что сложность линеарифметическая

def eratosfen(user_i):
    a = []
    prime_counter = 0
    for i in range(user_i * 10):
        a.append(i)

    a[1] = 0
    m = 2
    while m < user_i * 10:
        if a[m] != 0:
            prime_counter += 1
            j = m * 2
            while j < user_i * 10:
                a[j] = 0
                j = j + m
        if prime_counter == user_i:
            return m
        m += 1
print(eratosfen(user_i))

cProfile.run('eratosfen(user_i)')

#         48654 function calls in 0.046 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.045    0.045 <string>:1(<module>)
#         1    0.041    0.041    0.045    0.045 Task_4_2.py:46(eratosfen)
#         1    0.000    0.000    0.046    0.046 {built-in method builtins.exec}
#     48650    0.004    0.000    0.004    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
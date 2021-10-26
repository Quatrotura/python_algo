# Найти максимальный элемент среди минимальных элементов столбцов матрицы.
from random import random

MATRIX_ROW_SIZE = 6
MATRIX_COL_SIZE = 7

a = []
for i in range(MATRIX_ROW_SIZE):
    b = []
    row_sum = 0
    for j in range(MATRIX_COL_SIZE):
        b.append(int(random()*10))
    a.append(b)
    # print(a[i])

mins_array = []
for k in range(MATRIX_COL_SIZE):
    column_min = a[0][k]
    for l in range(MATRIX_ROW_SIZE):
        if a[l][k] < column_min:
            column_min = a[l][k]
    mins_array.append(column_min)

print(f'Максимальный элемент среди минимальных элементов каждого столбца {sorted(mins_array)[-1]}.')
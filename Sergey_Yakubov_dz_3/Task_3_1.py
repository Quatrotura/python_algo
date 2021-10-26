# 3.1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

def list_gen(start, end):

    a = []
    for i in range(start, end):
        a.append(i)
    return a

ARR_START_POINT = 2
ARR_END_POINT = 99

COMPARING_RANGE_START = 2
COMPARING_RANGE_END = 9

sequence = list_gen(ARR_START_POINT, ARR_END_POINT + 1)
b = []
for i in range(len(sequence)):
    flag = 0
    for j in range(COMPARING_RANGE_START, COMPARING_RANGE_END + 1):
        if sequence[i] % j == 0:
            flag += 1
    if flag == (COMPARING_RANGE_END - COMPARING_RANGE_START +1):
        b.append(sequence[i])

print(f'В диапазоне натуральных чисел от {ARR_START_POINT} до {ARR_END_POINT} \
следующие числа кратны каждому из чисел в диапазоне от {COMPARING_RANGE_START} до {COMPARING_RANGE_END}:\n\
{" ".join(list(map(str, b)))}')

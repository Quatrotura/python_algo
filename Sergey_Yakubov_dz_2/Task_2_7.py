# Напишите программу, доказывающую или проверяющую,
# что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число.

n = 4
left_side = 0

for i in range(1,n+1):
    left_side += i
if left_side == n * (n + 1) / 2:
    print('True')
else:
    print('False')

# с функцией код будет почище

# def get_proof(n, left_side=0):
#     for i in range(1, n + 1):
#         left_side += i
#     if left_side == n * (n + 1) / 2:
#         return True
#     else:
#         return False
#
#
# print(get_proof(4))

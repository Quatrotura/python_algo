# 5.2.	Написать программу сложения и умножения двух шестнадцатеричных чисел. 
# При этом каждое число представляется как коллекция, элементы которой это цифры числа.
# Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. 
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import defaultdict, deque
from itertools import zip_longest
a = input('Enter first hex number: ')
b = input('Enter second hex number: ')

# a = 'F4240'
# b = '16E360'

a, b = deque(a), deque(b)
hex_nums = '0123456789ABCDEF'
hex_table = defaultdict(int)
hex_table_reversed = defaultdict()
deс_nums = 0

for i in hex_nums:
	hex_table[i] = deс_nums
	hex_table_reversed[deс_nums] = i
	deс_nums += 1


def hex_sum(a, b, in_memory = 0):
	register_pairs = deque(zip_longest(reversed(a),reversed(b), fillvalue = 0))
	result = deque()
	for register in register_pairs:
		register_sum = hex_table[register[0]] + hex_table[register[1]] + in_memory

		if register_sum >= 10 and register_sum < 16:
			register_sum = hex_table_reversed[register_sum]
			in_memory = 0
		elif register_sum >= 16:
			register_sum = register_sum % 16
			in_memory = 1
		else:
			in_memory = 0

		result.appendleft(register_sum)

	if in_memory == 1:
		result.appendleft(1)

	return result

def hex_product(a,b):
	
	a_10 = 0
	b_10 = 0
	result_16 = deque()

	for i in range(len(a)):
		a_10 += hex_table[a[i]] * 16 ** (len(a) - i - 1)
	for i in range(len(b)):
		b_10 += hex_table[b[i]] * 16 ** (len(b) - i - 1)

	result_10 = a_10 * b_10

	while result_10 > 0:

		result_16.appendleft(hex_table_reversed[result_10 % 16])
		result_10 //= 16


	return result_16


hex_plus_hex = hex_sum(a,b)
hex_times_hex = hex_product(a,b)
print(hex_plus_hex)
print(hex_times_hex)

# 5.2.	Написать программу сложения и умножения двух шестнадцатеричных чисел. 
# При этом каждое число представляется как коллекция, элементы которой это цифры числа.
# Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. 
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import defaultdict

a = input('Enter first hex number: ')
b = input('Enter second hex number: ')

a, b = list(a), list(b)
print(a, b)
hex_nums = '0123456789ABCDEF'
hex_table = defaultdict(int) # сделать заполнение zipом
bin_nums = 0

for i in hex_nums:
	hex_table[i] = bin_nums
	bin_nums += 1

print(hex_table)

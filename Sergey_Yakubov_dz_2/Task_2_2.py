# Посчитать четные и нечетные цифры введенного натурального числа. 
# Например, если введено число 34560, 
# то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

# традиционно:

a = input('Enter your number: ')

even, odd = 0, 0

if a.isdigit() == True and a[0] != '0':
	a = int(a)
	while a > 0:		
		if a % 2 == 0:
			even += 1
		else:
			odd += 1
		a = a // 10
	print(f'There are {even} even digits and {odd} odd digits in your number.')
else:
	print('Enter only natural numbers')


# рекурсия для закрепления пройденного :-)

def get_qty_of_odd_even(a, even = 0, odd = 0):
	if a == 0:
		return print(f'There are {even} even digits and {odd} \
odd digits in your number.')
	else:
		if a % 2 == 0:
			even += 1
		else:
			odd += 1
		return get_qty_of_odd_even(a//10, even, odd)

a = input('Enter your number: ')

if a.isdigit() == True and a[0] != '0':
	a = int(a)
	get_qty_of_odd_even(a)
else: 
	print('Enter only natural numbers')

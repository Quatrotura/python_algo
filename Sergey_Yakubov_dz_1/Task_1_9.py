# 1.9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

try:
	a = int(input('Введите первое число: '))
	b = int(input('Введите второе число: '))
	c = int(input('Введите третье число: '))

	mid = c

	if a != b and b!= c and a != c:
		if (a > b and a < c) or (a > c and a < b):
			mid = a
		elif (b > a and b < c) or (b > c and b < a):
			mid = b		
		print(f'Среднее число: {mid}')
		# else:  - можно и не добавлять, чтобы не дублировать код
		# 	mid = c	

	else: 
		print('Введите три разных числа')	

except ValueError:
	print('Можно вводить только числа.')

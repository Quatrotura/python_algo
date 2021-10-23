# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.


n = input('Введите кол-во элементов ряда чисел: ')
if n.isdigit() == True:
	n = int(n)
	dig = 1
	total = 0

	for i in range(n):
		total += dig
		dig = dig / 2 * -1

	print(total)
else:
	print('Вводите только целые положительные числа.')	

 # рекурсия:

def get_sum(n, dig = 1, total = 0):
	if n == 0:
		return print(total)
	else:
		total += dig
		return get_sum(n - 1, dig / 2 * -1, total)

n = input('Введите кол-во элементов ряда чисел: ')
if n.isdigit() == True:
	get_sum(int(n))
else:
	print('Вводите только целые положительные числа.')	

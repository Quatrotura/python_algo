# 1.4. Написать программу, которая генерирует в указанных пользователем границах
# случайное целое число,
# случайное вещественное число,
# случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона. 
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы. 
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

from random import randint
from random import uniform

try:
	start_int     = int(input("\nВведите начальную границу целочисленного диапазона: "))
	end_int       = int(input("Введите конечную границу целочисленного диапазона: "))

	start_float   = float(input("Введите начальную границу диапазона вещественных чисел: "))
	end_float     = float(input("Введите конечную границу диапазона вещественных чисел: "))

	start_letter  = input("Введите начальную границу символьного диапазона: ")
	end_letter    = input("Введите конечную границу cимвольного диапазона: ")
	
	if start_letter.isalpha() == True and end_letter.isalpha() == True and len(start_letter) == 1 and len(end_letter) == 1: # проверка на ввод только букв и только одной буквы
		start_letter, end_letter = ord(start_letter), ord(end_letter)
	else: 
		raise ValueError

	result_int    = randint(start_int, end_int)
	result_float  = uniform(start_float, end_float)
	result_letter = chr(randint(start_letter, end_letter))

	print(f'\nСлучайное целое число в заданном диапазоне: {result_int}')
	print(f'Случайное вещественное число в заданном диапазоне: {result_float}')
	print(f'Случайный символ в заданном диапазоне: {result_letter}')

except ValueError:
	print('Введенные данные не соответствуют заданному условию.')

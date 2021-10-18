# Пользователь вводит две буквы. 
# Определить, на каких местах алфавита они стоят, 
# и сколько между ними находится букв.
try: 
	start_idx = ord('a')

	first_idx  = input('\nВведите первую букву: ')
	second_idx  = input('Введите вторую букву: ')

	if first_idx.isalpha() == True and second_idx.isalpha() == True and len(first_idx) == 1 and len(second_idx) == 1: # проверка на ввод только букв и только одной буквы
		first_idx, second_idx = ord(first_idx), ord(second_idx)
	else:
		raise ValueError

	first_position  = first_idx - start_idx + 1
	second_position = second_idx - start_idx + 1
	distance = abs(second_position - first_position) - 1 # модуль необходим, если индекс первой буквы больше индекса второй

	print(f'\nПозиция первой буквы: {first_position}')
	print(f'Позиция второй буквы: {second_position}')
	print(f'Кол-во букв между первой и второй: {distance}')

except ValueError:
	print('Вводите только буквы и только одну букву')


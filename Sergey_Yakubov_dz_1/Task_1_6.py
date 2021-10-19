# 1.6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

start_idx = ord('a')
user_abc_pos = input('\nВведите номер буквы: ')

if user_abc_pos.isdigit() == True and int(user_abc_pos) >= 1 and int(user_abc_pos) <= 26 : # проверка на ввод только числа с диапазоном соответствующим кол-ву букв в англ алфавите

	user_letter_idx = chr(int(start_idx)+ int(user_abc_pos) - 1)
	print(f'Введенный номер буквы в алфавите - это буква: {user_letter_idx}\n')

else:

	print('Введенное значение не соответствует требуемому формату.\nN.B. В англ. алфавите 26 букв.')



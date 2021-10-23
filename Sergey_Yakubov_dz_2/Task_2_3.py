# Сформировать из введенного числа обратное по порядку входящих 
# в него цифр и вывести на экран. 
# Например, если введено число 3486, то надо вывести число 6843.


n = input('enter the number: ')
if n.isnumeric() == True and n[0] != '0': #   проверку на ноль в начале конечно можно убрать, но тогда на входе будет не число...
	n = int(n)
	res = ''
	while n > 0:
		res = res + str(n % 10)
		n //= 10
	print(res)
else:
	print('enter only natural numbers')

# совсем оказаться от строк можно только если последняя цифра не равна 0,
# т.к. перевернутое целое число (если оно целое число) 
# не может начинаться с нуля, если подставлять 0 в начало, то все равно
# нужна строка:

n = input('enter the number: ')
if n.isnumeric() == True and n[0] != '0':
	n = int(n)
	res = 0
	while n > 0:
		res = res * 10 + n % 10
		n //= 10
	print(res)
else:
	print('enter only natural numbers')


# рекурсия для закрепления теории

def get_reversed(n, res=''):
	if n == 0:
		return print(res)
	else:
		res = res + str(n % 10)
		return get_reversed(n//10, res)

n = input('enter the number: ')
if n.isnumeric() == True and n[0] != '0':
	n = int(n)
	get_reversed(n)
else:
 	print('enter only natural numbers')	

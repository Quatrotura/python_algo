# Написать программу, которая будет складывать, вычитать, умножать или делить два числа. 
# Числа и знак операции вводятся пользователем. 
# После выполнения вычисления программа не должна завершаться, 
# а должна запрашивать новые данные для вычислений. 
# Завершение программы должно выполняться при вводе символа '0' в качестве знака операции. 
# Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), 
# то программа должна сообщать ему об ошибке и снова запрашивать знак операции. 
# Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.

 # попробуем освоить match case
op = '' # оператор
while op != '0':
	a, op, b = input('Enter operands and operator (first - left operand , second - operator, third - right operand).\n\
Use one whitespace to separate symbols:\n').split()
	if a.isdigit() and b.isdigit():
		match op:
			case '0': break
			case '+': print(f'{int(a) + int(b)}')
			case '-': print(f'{int(a) - int(b)}')
			case '*': print(f'{int(a) * int(b)}')
			case '/' if b == '0': print('Cannot divide by zero')
			case '/' if b != '0': print(f'{int(a) / int(b)}')
			case _: print("It's allowed to input only these signs for operator: + - * /.")
	else:
		print('Sorry. One cannot enter anything for operands except for numbers.')

# по-старому (без проверок .isdigit())
#
# can_enter_for_op = '+-*/'
# op = '' # оператор
#
# while op != '0':
# 	res = 0  # результат
# 	a, op, b = input('Enter operands and operator (first - left operand , second - operator, third - right operand).\n\
# Use one whitespace to separate symbols:\n').split()
# 	if op == '0':
# 		break
# 	while op not in can_enter_for_op and op != '0':
# 		op = input("It's allowed to input only these signs for operator: + - * / and 0 for exit.\n\
# Please type operator again:\n")
# 	if op == '+':
# 		res = float(a) + float(b)
# 		print(res)
# 	elif op == '-':
# 		res = float(a) - float(b)
# 		print(res)
# 	elif op == '*':
# 		res = float(a) * float(b)
# 		print(res)
# 	elif op == '/' and b == '0':
# 		print("Can't divide by zero!")
# 		print(res)
# 	elif op =='/':
# 		res = float(a) / float(b)
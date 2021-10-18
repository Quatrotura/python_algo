# 1.7. По длинам трех отрезков, введенных пользователем, 
# определить возможность существования треугольника, 
# составленного из этих отрезков. 
# Если такой треугольник существует, то определить, 
# является ли он разносторонним, равнобедренным или равносторонним.


try:
	a = float(input('Введите длину первого отрезка: '))
	b = float(input('Введите длину второго отрезка: '))
	c = float(input('Введите длину третьего отрезка: '))

	if (a + b) > c and (a + c) > b and (b + c ) > a: # сумма любых двух сторон всегда должна быть больше третьей
		print('Треугольник существует')

		if a != b != c:
			print('Треугольник разносторонний.')
		elif a == b == c:
			print('Треугольник равносторонний.')
		else:
			print('Треугольник равнобедренный.')

	else:
		print('Треугольник не существует.')
		
except ValueError:
	print("Длина вводится только с помощью чисел.")
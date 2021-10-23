# В программе генерируется случайное целое число от 0 до 100. 
# Пользователь должен его отгадать не более чем за 10 попыток. 
# После каждой неудачной попытки 
# должно сообщаться больше или меньше введенное пользователем число, чем то, что загадано. 
# Если за 10 попыток число не отгадано, то вывести загаданное число.

from random import randint

counter = 10
x = randint(0, 100)
print(x)

while counter != 0:
    user_x = input('Угадайте число от 0 до 100.')
    if user_x.isnumeric():
        user_x = int(user_x)
        if user_x == x:
            print('Вы угадали')
            break
        elif user_x < x:
            counter -= 1
            print(f'Не угадали. Ваше число слишком маленькое. Берите больше. Осталось {counter} попыток.')
        else:
            counter -= 1
            print(f'Не угадали. Ваше число слишком большое. Берите меньше. Осталось {counter} попыток.')
    else:
        print('Вводите только числа.')
else:
    print('Сорян. Попытки закончились!')

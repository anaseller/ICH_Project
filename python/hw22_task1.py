"""1. Напишите программу, которая открывает файл, считывает из него два числа и выполняет операцию их деления.
Если число отрицательное, выбросите исключение ValueError с сообщением "Число должно быть положительным".
Обработайте исключение и выведите соответствующее сообщение."""

def read_and_divide(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

            num1 = float(lines[0].strip())
            num2 = float(lines[1].strip())

            if num1 < 0 or num2 < 0:
                raise ValueError('Число должно быть положительным')

            result = num1 / num2
            print(f'Результат деления: {result}')

    except FileNotFoundError:
        print('Ошибка: Файл не найден')
    except ZeroDivisionError:
        print('Ошибка: Деление на ноль')

read_and_divide('numbers.txt')
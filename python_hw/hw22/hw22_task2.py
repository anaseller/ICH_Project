"""2. Напишите программу, которая открывает файл, считывает его содержимое и выполняет операции над числами в файле.
Обработайте возможные исключения при открытии файла (FileNotFoundError) и при выполнении операций над числами
(ValueError, ZeroDivisionError). Используйте конструкцию try-except-finally для обработки исключений
и закрытия файла в блоке finally."""

def process_file(filename):
    file = None
    try:
        file = open(filename, 'r')
        lines = file.readlines()

        for line in lines:
            parts = line.strip().split()

            try:
                num1 = float(parts[0])
                num2 = float(parts[1])
                result = num1 / num2
                print(f'{num1} / {num2} = {result}')
            except ZeroDivisionError:
                print(f'Ошибка: Деление на ноль невозможно')
            except ValueError:
                print(f'Ошибка: Невозможно преобразовать строку в число')
            except IndexError:
                print(f'Ошибка: В строке недостаточно чисел')

    except FileNotFoundError:
        print(f'Ошибка: Файл "{filename}" не найден')

    finally:
        if file:
            file.close()

process_file('ex_data.txt')
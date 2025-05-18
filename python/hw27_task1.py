# Напишите функцию, которая принимает на вход список чисел и возвращает сумму квадратов только четных чисел из списка,
# используя функциональные подходы (например, map, filter и reduce).
#
# Пример вывода:
# Введите числа: 4, 6, 3, 4, 2, 3, 9, 0, 7
# Результат: 72

from functools import reduce


# выбираем четные
# возводим в квадрат
# суммируем

def sum_of_squares(numbers):
    even_numbers = filter(lambda x: x % 2 == 0, numbers)
    squared = map(lambda x: x ** 2, even_numbers)
    return reduce(lambda acc, x: acc + x, squared, 0)

user_num = input('Введите числа: ')
numbers = list(map(int, user_num.replace(',', ' ').split()))

print('Результат:', sum_of_squares(numbers))
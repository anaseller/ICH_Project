# 3. Напишите программу, которая запрашивает у пользователя строку и выравнивает ее по центру
# с заданной шириной. Если строка не может быть выровнена по центру из-за нечетной ширины,
# она должна быть выровнена смещением вправо. Используйте методы center() и rjust() для выравнивания строки.
#
# Пример вывода:
#
# Введите строку: Python
# Введите ширину: 10
# Результат:
#   Python


s = input('Введите строку: ')
width = int(input('Введите ширину: '))
if width % 2 == 0 and len(s) % 2 == 0 or width % 2 == 1 and len(s) % 2 == 1:
    print(s.center(width))
else:
    print(s.rjust(width))
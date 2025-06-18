# 3. Напишите программу, которая принимает словарь от пользователя и ключ, и возвращает значение
# для указанного ключа с использованием метода get или setdefault. Создайте функцию get_value_from_dict,
# которая принимает словарь и ключ в качестве аргументов, и возвращает значение для указанного ключа,
# используя метод get или setdefault в зависимости от выбранного варианта. Выведите полученное значение на экран.
#
#
# Пример словаря:
# my_dict = {'apple': 5, 'banana': 6, 'cherry': 7}
#
# Пример вывода:
# Введите ключ для поиска: banana
# Использовать метод get (y/n)? y
# Значение для ключа 'banana': 6

def get_value_from_dict(a, key, use_get=True):
    if use_get:
        return a.get(key)
    else:
        return a.setdefault(key, 'Значение по умолчанию')

my_dict = {'apple': 5, 'banana': 6, 'cherry': 7}

key = input('Введите ключ для поиска: ')
user_input = input('Использовать метод get (y/n)? ').lower()

use_get = user_input == 'y'

value = get_value_from_dict(my_dict, key, use_get)

print(f"Значение для ключа '{key}': {value}")
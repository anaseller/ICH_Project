# 1. Напишите функцию merge_dicts, которая принимает произвольное количество словарей
# в качестве аргументов и возвращает новый словарь, объединяющий все входные словари.
# Если ключи повторяются, значения должны быть объединены в список.
# Функция должна использовать аргумент **kwargs для принятия произвольного числа аргументов словаря.
#
# Пример ввода:
# {'a': 1, 'b': 2}
# {'b': 3, 'c': 4}
# {'c': 5, 'd': 6}
# Пример вывода:
# {'a': [1], 'b': [2, 3], 'c': [4, 5], 'd': [6]}

def merge_dicts(**kwargs):
    merged = {}
    for d in kwargs.values():
        for key, value in d.items():
            if key in merged:
                merged[key].append(value)
            else:
                merged[key] = [value]
    return merged

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict3 = {'c': 5, 'd': 6}

result = merge_dicts(d1=dict1, d2=dict2, d3=dict3)
print(result)
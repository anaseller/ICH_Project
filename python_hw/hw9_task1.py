# Напишите программу, которая запрашивает у пользователя строку и определяет, является ли она панграммой. 
# Панграмма - это фраза, содержащая все буквы алфавита. Программа должна игнорировать регистр букв и пробелы 
# при проверке панграммы. Выведите соответствующее сообщение на экран с помощью команды print. 
# Решить задачу для латиницы.
# 
# Пример вывода:
# Введите строку: The quick brown fox jumps over the lazy dog
# Строка является панграммой.

user_text = input('Введите строку: ')

alphabet = 'abcdefghijklmnopqrstuvwxyz'
user_text = user_text.lower()

i = 0
is_contain = True

while i < len(alphabet):
    if alphabet[i] not in user_text:
        is_contain = False
        break
    i += 1

print('Строка является панграммой.' if is_contain else 'Строка не является панграммой.')


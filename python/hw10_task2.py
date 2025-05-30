# 2. Напишите программу, которая запрашивает у пользователя строку и определяет,
# содержит ли она только уникальные символы. Если все символы в строке уникальны,
# выведите соответствующее сообщение на экран. В противном случае выведите сообщение о том, какие символы повторяются.
# Не используйте множества и подобные структуры данных, которые мы пока не изучали, для проверки уникальности символов.
#
# Пример вывода:
# Введите строку: Python
# Все символы в строке уникальны.
# Введите строку: Hello
# Символы 'l' и 'o' повторяются.

text = input('Введите строку: ')
repeated_chars = ''
unique = True

i = 0
while i < len(text):
    j = i + 1
    while j < len(text):
        if text[i] == text[j] and text[i] not in repeated_chars:
            repeated_chars += text[i] + ' '
            unique = False
        j += 1
    i += 1

if unique:
    print('Все символы в строке уникальны.')
else:
    print('Символы "' + repeated_chars.strip().replace(' ', '", "') + '" повторяются.')
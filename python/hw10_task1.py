# 1. Напишите программу, которая запрашивает у пользователя строку и преобразует ее,
# удаляя все гласные буквы из строки. Используйте метод replace() для замены гласных букв на пустую строку.
# Выведите преобразованную строку на экран с помощью команды print.
#
# Пример вывода:
# Введите строку: Hello, world!
# Результат: Hll, wrld!


text = input('Введите строку: ')
vowels = 'AEIOUaeiouАЕЁИОУЫЭЮЯаеёиоуыэюя'

for vowel in vowels:
    text = text.replace(vowel, '')

print('Результат:', text)
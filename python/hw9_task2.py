# Напишите программу, которая запрашивает у пользователя строку и выводит на экран количество гласных и
# согласных букв в ней. Используйте функцию len() для подсчета количества букв.
# Выведите результат на экран с помощью команды print. Решить задачу для латиницы.
#
# Пример вывода:
# Введите строку: Hello World
# Количество гласных букв: 3
# Количество согласных букв: 7

user_text = input('Введите строку: ')

vowels = 'aeiouAEIOU'
consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'

i = 0

vow = 0
con = 0

while i < len(user_text):
    x = user_text[i] # берем текущий символ
    if x in vowels:
        vow += 1
    elif x in consonants:
        con += 1
    i +=1

print(f'Количество гласных букв: {vow}')
print(f'Количество согласных букв: {con}')
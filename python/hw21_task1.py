# 1. Напишите программу, которая подсчитывает количество вхождений каждого слова в тексте
# и выводит на экран наиболее часто встречающиеся слова. Для решения задачи используйте класс Counter
# из модуля collections. Создайте функцию count_words, которая принимает текст в качестве аргумента
# и возвращает словарь с количеством вхождений каждого слова. Выведите наиболее часто встречающиеся слова
# и их количество.
#
#
# Пример вывода:
# Введенный текст: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sed lacinia est.
# sed: 2
# Lorem: 1

from collections import Counter

def count_words(text):
    words = text.lower().split()
    return Counter(words)

text = input('Введите текст: ')

word_count = count_words(text)

popular_w = word_count.most_common(2)

print(f'Введенный текст: {text}')
for word, count in popular_w:
    print(f'{word}: {count}')
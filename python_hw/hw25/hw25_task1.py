"""1. Напишите функцию find_longest_word, которая будет принимать список слов 
и возвращать самое длинное слово из списка. Аннотируйте типы аргументов и возвращаемого значения функции.

Пример вызова функции и ожидаемого вывода:
words = ["apple", "banana", "cherry", "dragonfruit"]
result = find_longest_word(words)
print(result)  # Ожидаемый вывод: "dragonfruit"""

from typing import List

def find_longest_word(words: List[str]) -> str:
    return max(words, key=len)

words = ["apple", "banana", "cherry", "dragonfruit"]
result = find_longest_word(words)
print(result)
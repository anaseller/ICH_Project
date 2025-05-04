# Напишите программу, которая принимает список слов и возвращает список, содержащий только анаграммы.
# Анаграммы - это слова, составленные из одних и тех же букв, но в разном порядке.
# Создайте функцию anagrams, которая принимает список слов в качестве аргумента и возвращает список анаграмм.
# Используйте множества и сортировку букв в слове для проверки на анаграмму. Выведите результат на экран.
#
# Пример переданного списка слов:
# ['cat', 'dog', 'tac', 'god', 'act']
# Пример вывода:
# Анаграммы: ['dog', 'god'], ['cat', 'tac', 'act']

from collections import defaultdict

def anagrams(words):
    groups = defaultdict(list)

    for word in words:
        key = ''.join(sorted(word))  # 'cat' -> 'act'
        groups[key].append(word)

    result = [group for group in groups.values() if len(group) > 1]
    return result


words = ['cat', 'dog', 'tac', 'god', 'act']
result = anagrams(words)
print('Анаграммы:', result)

# 2. Напишите функцию find_common_words(url_list), которая принимает список URL-адресов
# и возвращает список наиболее часто встречающихся слов на веб-страницах.
# Для каждого URL-адреса функция должна получить содержимое страницы с помощью запроса GET
# и использовать регулярные выражения для извлечения слов. Затем функция должна подсчитать
# количество вхождений каждого слова и вернуть наиболее часто встречающиеся слова в порядке убывания частоты.


import requests
import re
from collections import Counter

def find_common_words(url_list):
    all_words = []

    for url in url_list:
        try:
            response = requests.get(url)
            response.raise_for_status()

            words = re.findall(r'\b\w+\b', response.text.lower())
            all_words.extend(words)

        except requests.RequestException as e:
            print(f'Ошибка при запросе {url}: {e}')

    word_counts = Counter(all_words)
    common_words_sorted = [word for word, count in word_counts.most_common()]

    return common_words_sorted

print(find_common_words(['https://reqres.in']))
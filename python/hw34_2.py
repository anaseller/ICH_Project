# Напишите функцию highlight_keywords(text, keywords), которая выделяет все вхождения заданных ключевых слов
# в тексте, окружая их символами *. Функция должна быть регистронезависимой при поиске ключевых слов.
#
# Пример использования:
# text = "This is a sample text. We need to highlight Python and programming."
# keywords = ["python", "programming"]
# highlighted_text = highlight_keywords(text, keywords)
# print(highlighted_text)
# # Вывод: "This is a sample text. We need to highlight *Python* and *programming*."

import re

def highlight_keywords(text, keywords):
    def replacer(match):
        return f'*{match.group(0)}*'

    for word in keywords:
        pattern = re.compile(re.escape(word), re.IGNORECASE)
        text = pattern.sub(replacer, text)
    return text

text = "This is a sample text. We need to highlight Python and programming."
keywords = ["python", "programming"]
highlighted_text = highlight_keywords(text, keywords)
print(highlighted_text)
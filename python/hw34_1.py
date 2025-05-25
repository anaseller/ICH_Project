# Напишите функцию extract_emails(text), которая извлекает все адреса электронной почты из заданного текста
# и возвращает их в виде списка.
#
# Пример использования:
# text = "Contact us at info@example.com or support@example.com for assistance."
# emails = extract_emails(text)
# print(emails)  # Вывод: ['info@example.com', 'support@example.com']

import re

def extract_emails(text):
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(pattern, text)

text = "Contact us at info@example.com or support@example.com for assistance."
emails = extract_emails(text)
print(emails)  # Вывод: ['info@example.com', 'support@example.com']

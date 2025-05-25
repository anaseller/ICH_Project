# Напишите программу, которая запрашивает у пользователя URL-адрес веб-страницы и уровень заголовков,
# а затем использует библиотеку Beautiful Soup для парсинга HTML и извлекает заголовки нужного уровня
# (теги h1, h2, h3 и т.д.) с их текстом.

import requests
from bs4 import BeautifulSoup

# url = input('Введите URL-адрес: ')
url = 'https://en.wikipedia.org/wiki/REST'
# level = input('Введите уровень заголовка (например, h1, h2, h3): ')
level = 'h2'

response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

# извлекаем заголовки
titles = soup.find_all(level)
for title in titles:
    print(title)

# извлекаем текст
for title in titles:
    print('title.text:', title.text)
# Напишите программу, которая запрашивает у пользователя URL-адрес веб-страницы,
# использует библиотеку Beautiful Soup для парсинга HTML и выводит список всех ссылок на странице.

import requests
from bs4 import BeautifulSoup

# url = input('Введите URL-адрес: ')
url = 'https://en.wikipedia.org/wiki/REST'
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    links = soup.find_all('a')

    for link in links:
        print(link.get('href'))




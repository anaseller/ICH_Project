# 1. Напишите функцию get_response(url), которая отправляет GET-запрос по заданному URL-адресу
# и возвращает объект ответа.
# Затем выведите следующую информацию об ответе:
# - Код состояния (status code)
# - Текст ответа (response text)
# - Заголовки ответа (response headers)
#
# Пример использования:
# url = "https://api.example.com"
# response = get_response(url)
# print("Status Code:", response.status_code)
# print("Response Text:", response.text)
# print("Response Headers:", response.headers)

import requests

def get_response(url):
    response = requests.get(url)
    return response


url = "https://quickpizza.grafana.com/test.k6.io/"
response = get_response(url)
print("Status Code:", response.status_code)
print("Response Text:", response.text)
print("Response Headers:", response.headers)
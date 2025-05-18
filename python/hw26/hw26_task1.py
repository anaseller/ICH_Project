"""1. Напишите программу, которая принимает в качестве аргумента командной строки путь к файлу .py и запускает его.
При запуске файла программа должна выводить сообщение "Файл <имя файла> успешно запущен".
Если файл не существует или не может быть запущен, программа должна вывести соответствующее сообщение об ошибке."""

import sys
import os

if len(sys.argv) < 2:
    print('Ошибка: путь к файлу не указан')
    sys.exit()

file_path = sys.argv[1]

if not os.path.isfile(file_path):
    print(f'Ошибка: файл "{file_path}" не существует')
    sys.exit()

try:
    exec(open(file_path).read())
    print(f'Файл "{file_path}" успешно запущен')
except Exception as e:
    print(f'Ошибка при запуске файла: {e}')


# пример запуска
# python3 hw26_task1.py ex_file.py
# Вывод:
# Hello world
# Файл "ex_file.py" успешно запущен

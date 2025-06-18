"""2. Напишите программу, которая принимает в качестве аргумента командной строки путь к директории
и выводит список всех файлов и поддиректорий внутри этой директории.
Для этой задачи используйте модуль os и его функцию walk.
Программа должна выводить полный путь к каждому файлу и директории."""


import sys
import os

if len(sys.argv) < 2:
    print('Ошибка: путь к директории не указан')
    sys.exit()

directory = sys.argv[1]

if not os.path.isdir(directory):
    print(f'Ошибка: директория "{directory}" не существует')
    sys.exit()

for root, dirs, files in os.walk(directory):
    for d in dirs:
        print(os.path.join(root, d))
    for f in files:
        print(os.path.join(root, f))
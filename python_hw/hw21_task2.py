# 2. Напишите программу, которая создает именованный кортеж Person для хранения информации о человеке,
# включающий поля name, age и city. Создайте список объектов Person и выведите информацию о каждом человеке на экран.
#
#
# Пример вывода:
# Name: Alice, Age: 25, City: New York
# Name: Bob, Age: 30, City: London
# Name: Carol, Age: 35, City: Paris

from collections import namedtuple

Person = namedtuple('Person', ['name', 'age', 'city'])

people = [
    Person(name='Alice', age=25, city='New York'),
    Person(name='Bob', age=30, city='London'),
    Person(name='Carol', age=35, city='Paris')
]

for person in people:
    print(f'Name: {person.name}, Age: {person.age}, City: {person.city}')
# 1. Напишите функцию, которая принимает список кортежей от пользователя, где каждый кортеж содержит
# информацию о студенте (имя, возраст, средний балл). Программа должна вывести на экран имена студентов,
# чей средний балл выше заданного значения. Используйте методы кортежей и циклы для обработки данных.
# Выведите итоговый список на экран с помощью команды print.
#
# Пример списка кортежей:
# [("Alice", 20, 90), ("Bob", 19, 80), ("Charlie", 21, 95), ("David", 18, 85)]
# Пример вывода:
# Введите пороговое значение среднего балла: 90
# Студенты с средним баллом выше 90 : ['Charlie']

students = [("Alice", 20, 90), ("Bob", 19, 80), ("Charlie", 21, 95), ("David", 18, 85)]

x = int(input("Введите пороговое значение среднего балла: "))

good_students = [] # пустой список для подходящих студентов

for student in students:
    name = student[0]
    grade = student[2]
    if grade > x:
        good_students.append(name)

print("Студенты с средним баллом выше", x, ":", good_students)



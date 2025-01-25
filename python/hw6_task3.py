# Напишите программу, которая запрашивает у пользователя целое положительное число и проверяет,
# является ли оно простым. Простое число - это число, которое делится только на 1 и на само себя без остатка.
# Используйте цикл while и проверку деления числа на все числа от 2 до N-1 для решения задачи.
# Выведите соответствующее сообщение на экран с помощью команды print.
# Пример вывода:
# Введите целое положительное число: 17
# Число 17 является простым.

x = int(input('Введите целое положительное число: '))
a = 2
while a < x:
    if x % a == 0:
        print(f'Число {x} не является простым')
        break
    a += 1
else:
    print(f'Число {x} является простым')



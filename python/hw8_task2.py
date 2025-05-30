# Напишите программу, которая запрашивает у пользователя целое число и проверяет,
# является ли оно числом Армстронга. Число Армстронга - это число, которое равно сумме своих цифр,
# возведенных в степень, равную количеству цифр в числе. Выведите соответствующее сообщение на экран
# с помощью команды print.
#
# Пример вывода:
# Введите целое число: 153
# Число является числом Армстронга.

num = int(input('Введите целое число: '))
num_len = len(str(num))

sum_armstrong = 0
n = num

while n > 0:
    digit = n % 10  #получаем последнюю цифру через остаток от деления
    sum_armstrong += digit ** num_len  #возводим в степень и прибавлем к сумме
    n = n // 10  #удаляем последнюю цифру

if sum_armstrong == num:
    print('Число является числом Армстронга.')
else:
    print('Число не является числом Армстронга.')



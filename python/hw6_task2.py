# Напишите программу, которая запрашивает у пользователя число N и выводит первые N чисел Фибоначчи.
# Числа Фибоначчи - это последовательность чисел, где каждое следующее число
# является суммой двух предыдущих чисел (начиная с 0 и 1). Используйте цикл while для решения задачи.
# Выведите числа через запятую с помощью команды print.
# Пример вывода:
# Введите число N: 7
# Первые 7 чисел Фибоначчи: 0, 1, 1, 2, 3, 5, 8

n = int(input('Введите число N: '))

count = 2
a = 0
b = 1

print(a, end=', ')
print(b, end=', ')

while count < n:
    c = a + b
    if count == n - 1 :
        print(c)
    else:
        print(c, end=', ')
    a = b
    b = c
    count += 1



# Написать программу, вычисляющую факториал числа.
# Решить задачу с помощью рекурсии.
# !n = n * (n-1) *... * 1
# !5 = 1 * 2 * 3 * 4 * 5 =120

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

num = int(input('Введите число: '))
print(f'Факториал: {factorial(num)}')
# Приближённое значение синуса можно вычислить по формуле Тейлора.
#
# sin(x) = x^1/1! - x^3/3! + x^5/5! - x^7/7! + x^9/9! - ...
#
# Написать программу, которая
#  - приблизительно вычисляет значение синуса от вводимого значения x;
#  - оценивает погрешность вычисления с помощью этой формулы относительно настоящего значения,
#         полученного при вызове нужной функции из библиотеки math.
# Примечание: индексы в рядах начинаются с нуля

# i = 0
# while ...:
#     sign = ...      # формула вычисления знака i-того элемента последовательности
#     factorial = ... # формула факториала для i-того элемента последовательности
#     term = ...      # формула вычисления самого i-того элемента последовательности

from math import factorial
n = 8
x = ...  pi/4
i = 0
while i < 8:
   # sign = (-1) ** i   # формула вычисления знака i-того элемента последовательности
   # factorial = factorial(2 * i + 1) # потому что закономерность 0:1 1:3 2:5 3:7 # формула факториала для i-того элемента последовательности
    term = (-1) ** i * (x ** (2 * i + 1) / factorial(2 * i + 1))
    i += 1
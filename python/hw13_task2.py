# 2. Напишите программу, которая принимает список чисел и возвращает сумму, минимальное и
# максимальное значение из списка. Используйте функцию для обработки списка чисел и возврата трех значений.
# Выведите результат на экран с помощью команды print.
#
# Пример вывода:
# Введите числа:  3, 7, 2, 9, 1, 5
# Сумма чисел: 27
# Минимальное значение: 1
# Максимальное значение: 9

numbers_inp = input("Введите числа, разделённые запятой: ")

numbers_str = numbers_inp.split(",")
numbers = []
for item in numbers_str:
    numbers.append(int(item.strip()))

def analyze_list(nums):
    total = sum(nums)
    minimum = min(nums)
    maximum = max(nums)
    return total, minimum, maximum

total, minimum, maximum = analyze_list(numbers)

print("Сумма чисел:", total)
print("Минимальное значение:", minimum)
print("Максимальное значение:", maximum)
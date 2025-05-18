'''Напишите программу, которая принимает список чисел от пользователя и использует функцию reduce из модуля functools,
 чтобы найти произведение всех чисел в списке.
 Затем программа должна использовать функцию itertools.accumulate для накопления произведений чисел в новом списке.
 В результате программа должна вывести список, содержащий накопленные произведения.'''

from functools import reduce
from itertools import accumulate

input_num = input('Введите список чисел через пробел: ').split()
num = list(map(float, input_num))

product = reduce(lambda x, y: x * y, num)

acc_list = list(accumulate(num, lambda x, y: x * y))

print('Произведение всех чисел:', product)
print('Накопленные произведения:', acc_list)
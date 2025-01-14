#У нас есть две логические переменные:
#is_weekday, is_vacation (выходной день и каникулы).
#Они могут принимать разные значения, всего 4 комбинации: true - true, true - false,
#false - false, false - true. Есть правило: мы можем поспать, если день не рабочий
#или мы на каникулах. Напишите программу, которая в зависимости от значений двух
#переменных печатает, можем ли мы поспать или нет. То есть для значений
#is_weekday = False и is_vacation = True
#программа должна печатать “можете поспать”.

# Раб каникулы -
# Раб не каникулы
# Не раб каникулы -
# Не раб не каникулы -

is_weekday = input('Сегодня рабочий день?') == True
is_vacation = input('Сегодня каникулы?') == True

if not is_weekday and is_vacation:
    print('можете поспать')
elif is_weekday and is_vacation:
    print('можете поспать')
elif not is_weekday and not is_vacation:
    print('можете поспать')
else:
    print('нельзя спать')

# is_weekday = True
# is_vacation = True
#
# if not is_weekday and is_vacation:
#     print('можете поспать')
# else:
#     print('нельзя спать')


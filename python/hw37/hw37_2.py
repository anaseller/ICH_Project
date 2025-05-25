# В базе данных ich_edit три таблицы. Users с полями (id, name, age),
# Products с полями (pid, prod, quantity) и Sales с полями (sid, id, pid).
# Программа должна вывести все имена из таблицы users, дать пользователю выбрать одно из них
# и вывести все покупки этого пользователя.


import mysql.connector
from local_settings import dbconfig

dbconfig['database'] = 'ich_edit'


with mysql.connector.connect(**dbconfig) as connection:
    with connection.cursor() as cursor:

        cursor.execute('SELECT name FROM Users')
        names = [row[0] for row in cursor.fetchall()]

        print('Список пользователей:')
        for name in names:
            print('-', name)

        selected_name = input('Выберите имя пользователя: ')

        cursor.execute('SELECT id FROM Users WHERE name = %s', (selected_name,))
        user_id = cursor.fetchone()[0]

        cursor.execute('SELECT pid FROM Sales WHERE id = %s', (user_id,))
        product_ids = [row[0] for row in cursor.fetchall()]

        if product_ids:
            format_strings = ','.join(['%s'] * len(product_ids))
            cursor.execute(f'SELECT prod FROM Products WHERE pid IN ({format_strings})', tuple(product_ids))
            products = cursor.fetchall()

            print('Покупки пользователя:', selected_name)
            for product in products:
                print('-', product[0])
        else:
            print('У пользователя нет покупок.')
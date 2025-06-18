# В базе данных ich_edit три таблицы. Users с полями (id, name, age),
# Products с полями (pid, prod, quantity) и Sales с полями (sid, id, pid).
# Программа должна запросить у пользователя название таблицы и вывести все ее строки или сообщение,
# что такой таблицы нет.


import mysql.connector
from local_settings import dbconfig

dbconfig['database'] = 'ich_edit'

with mysql.connector.connect(**dbconfig) as connection:
    with connection.cursor() as cursor:
        table_name = input('Введите название таблицы (Users, Products, Sales): ')

        cursor.execute('SHOW TABLES;')
        all_tables = [table[0] for table in cursor.fetchall()]

        if table_name.lower() in [t.lower() for t in all_tables]:
            cursor.execute(f'SELECT * FROM {table_name}')
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        else:
            print('Такой таблицы нет.')
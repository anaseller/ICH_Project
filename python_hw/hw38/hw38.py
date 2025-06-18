"""
В базе данных ich_edit три таблицы. Users с полями (id, name, age), Products с полями (pid, prod, quantity) и
Sales с полями (sid, id, pid). Написать мини-интерфейс к базе данных, который умеет выполнять разные команды.
Выбрать таблицу для запроса.

1.) Предусмотреть возможность выбрать несколько таблиц. Вывести результат их соединения, если это возможно, или
сообщение об ошибке.
2.) Выбрать одно поле из выбранной таблицы и искомое значение этого поля. Вывести все подходящие строки

Доработать мини-интерфейс к базе данных, который был сделан на занятии. Новые возможности интерфейса:

Ввести список полей выбранной таблицы.

При вводе искомого значения добавить возможность выбора знака - найти записи, в которых выбранное поле больше,
меньше или равно введенному значению.

"""


from pprint import pprint

import mysql.connector
from local_settings import *

import mysql.connector
dbconfig = {
    'host': HOST,
    'user': USER,
    'password': PASSWORD,
    'database': DATABASE,
}

class MySQLConnection:
    dbconfig = {
        'host': HOST,
        'user': USER,
        'password': PASSWORD,
        'database': DATABASE
    }
    def __init__(self):
        self.config = MySQLConnection.dbconfig
        self.connection = None
        self.cursor = None

    def __enter__(self):
        try:
            self.connection = mysql.connector.connect(**self.config)
            self.cursor = self.connection.cursor(buffered=True)  # buffered защищает от "Unread result"
            return self
        except Exception as e:
            print(f"Ошибка подключения к MySQL: {e}")
            raise

    def __exit__(self, exc_type, exc_value, traceback):
        if self.cursor:
            try:
                self.cursor.close()
            except Exception as e:
                print(f" {e.__class__.__name__}: {e}")
        if self.connection:
            try:
                self.connection.close()
            except Exception as e:
                print(f" {e.__class__.__name__}: {e}")

    def fetchall(self) -> list:
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def commit(self):
        self.connection.commit()

    def execute(self, query: str, params: tuple = None):
        try:
            self.cursor.execute(query, params or ())
        except Exception as e:
            print(f"{e.__class__.__name__}: {e}")
            raise


class Table:
    '''
    Class Table for table description
    '''
    def __init__(self, table_name):
        self.table_name = table_name


    def __str__(self):
        return self.table_name

    def get_column(self):
        with MySQLConnection() as my_connect:
            my_connect.execute(f'DESCRIBE {self.table_name};')
        return [str(f"{self.table_name}.{colum[0]}") for colum in my_connect.cursor.fetchall()]

    def get_describe(self):
        with MySQLConnection() as my_connect:
            my_connect.execute(f'DESCRIBE {self.table_name};')
        return my_connect.cursor.fetchall()

class Query:

    def __init__(self, Table):
        self.table = Table
        self.fields = ["*"]
        self.joins = []
        self.wheres = []
        self.params = []

    def select(self, *fields):
        if fields:
            self.fields = fields
        return self

    def join(self, table_class, on_from, on_too, join_type="INNER"):
        self.joins.append({"type": join_type, "table": table_class, "on_from": on_from, "on_too": on_too})
        return self

    def where(self, colum: str, compare: str, value):
        compares = ['>', '<', '=', '!=', '<>', '>=', '<=']
        condition = f"{colum} {compare} '{value}'"
        self.wheres.append(condition)

        return self

    def build(self):
        query = f"SELECT {', '.join(self.fields)} FROM {self.table}"

        if self.joins:
            for join in self.joins:
                query += f" {join['type']} JOIN {join['table']} ON {join['on_from']} = {join['on_too']}"

        if self.wheres:
            query += " WHERE " + " AND ".join(self.wheres)

        return query



if __name__ == '__main__':
    users = Table('Users') #Users
    products = Table('Products') #Products
    sales = Table('Sales') #Sales

    users_column = users.get_column() #['Users.id', 'Users.name', 'Users.age']
    products_column = products.get_column() #['Products.pid', 'Products.prod', 'Products.quantity']
    sales_column = sales.get_column() #['Sales.sid', 'Sales.id', 'Sales.pid']
    all_column = users_column + products_column + sales_column #['Users.id', 'Users.name', 'Users.age', 'Products.pid', 'Products.prod', 'Products.quantity']
    sales_query = (Query(sales).select(*all_column).join(
        table_class=users,
        join_type="LEFT",
        on_from=sales_column[1],
        on_too=users_column[0]
    ).join(
        table_class=products,
        join_type="LEFT",
        on_from=sales_column[2],
        on_too=products_column[0]
    ).where(
        colum=users_column[0],
        compare='<>',
        value=1
    ).where(
        colum=users_column[1],
        compare='!=',
        value='Алиса'
    )
                   .build())

    # print(sales_query)
    with MySQLConnection() as my_connect:
        my_connect.execute(sales_query)
        # print(my_connect.fetchall())


    def interactive_choice():
        tables = {
            'Users': Table('Users'),
            'Products': Table('Products'),
            'Sales': Table('Sales')
        }

        print('Доступные таблицы:', ', '.join(tables.keys()))
        selected_tables = input('Введите через запятую названия таблиц, которые хотите использовать: ').strip().split(
            ',')

        selected_tables = [tbl.strip() for tbl in selected_tables if tbl.strip() in tables]
        if not selected_tables:
            print('Ошибка: ни одной корректной таблицы не выбрано.')
            return

        try:
            base_table = tables[selected_tables[0]]
            q = Query(base_table)
            all_columns = []

            for tbl_name in selected_tables:
                cols = tables[tbl_name].get_column()
                all_columns.extend(cols)

            q.select(*all_columns)

            if 'Sales' in selected_tables and 'Users' in selected_tables:
                q.join(tables['Users'], 'Sales.id', 'Users.id')
            if 'Sales' in selected_tables and 'Products' in selected_tables:
                q.join(tables['Products'], 'Sales.pid', 'Products.pid')

            apply_filter = input('Хотите применить фильтр по полю? (y/n): ').strip().lower()
            if apply_filter == 'y':
                print('Доступные поля:', ', '.join(all_columns))
                field = input('Выберите поле: ').strip()
                sign = input('Выберите знак (>, <, =, >=, <=, !=): ').strip()
                value = input('Введите значение: ').strip()
                q.where(field, sign, value)

            final_query = q.build()
            print('SQL-запрос:', final_query)

            with MySQLConnection() as my_connect:
                my_connect.execute(final_query)
                result = my_connect.fetchall()
                pprint(result)

        except Exception as e:
            print(f'Ошибка при выполнении запроса: {e}')


    interactive_choice()
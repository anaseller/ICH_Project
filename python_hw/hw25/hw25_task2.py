"""2. Напишите программу, которая будет считывать данные о продуктах из файла
и использовать аннотации типов для аргументов и возвращаемых значений функций. Создайте текстовый файл "products.txt",
в котором каждая строка будет содержать информацию о продукте в формате "название, цена, количество". Например:

Apple, 1.50, 10
Banana, 0.75, 15

В программе определите функцию calculate_total_price, которая будет принимать список продуктов
и возвращать общую стоимость. Продумайте, какая аннотация должна быть у аргумента! Считайте данные из файла,
разделите строки на составляющие и создайте список продуктов. Затем вызовите функцию calculate_total_price
с этим списком и выведите результат."""


from typing import List, Tuple

Product = Tuple[str, float, int]

def read_products(filename: str) -> List[Product]:
    products: List[Product] = []
    with open(filename, 'r') as file:
        for line in file:
            name, price_str, quantity_str = line.strip().split(', ')
            price = float(price_str)
            quantity = int(quantity_str)
            products.append((name, price, quantity))
    return products

def calculate_total_price(products: List[Product]) -> float:
    total = 0.0
    for name, price, quantity in products:
        total += price * quantity
    return total

products = read_products('products.txt')

total_price = calculate_total_price(products)

print(f'Общая стоимость продуктов: {total_price:.2f}')
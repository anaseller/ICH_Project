'''1. Создайте класс Rectangle для представления прямоугольника.
Класс должен иметь атрибуты width (ширина) и height (высота) со значениями по умолчанию,
а также методы calculate_area() для вычисления площади прямоугольника и calculate_perimeter()
для вычисления периметра прямоугольника.
Переопределить методы __str__, __repr__.
Затем создайте экземпляр класса Rectangle и выведите информацию о нем,
его площадь и периметр.'''

class Rectangle:
    def __init__(self, width=1, height=1):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f'Прямоугольник: ширина = {self.width}, высота = {self.height}'

    def __repr__(self):
        return f'Rectangle(width={self.width}, height={self.height})'



rect = Rectangle(3, 5)

print(rect)
print(repr(rect))
print('Площадь:', rect.calculate_area())
print('Периметр:', rect.calculate_perimeter())
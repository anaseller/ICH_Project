# 2. Реализовать класс Email, представляющий электронное письмо.
# Класс должен поддерживать следующие операции:
# - Сравнение писем по дате (операторы <, >, <=, >=, ==, !=)
# - Преобразование письма в строку (метод __str__)
# - Получение длины текста письма (метод __len__)
# - Получение хеш-значения письма (метод __hash__)
# - Проверка наличия текста в письме (метод __bool__)



from datetime import datetime

class Email:
    def __init__(self, sender, recipient, subject, body, date):
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.body = body
        self.date = date

    def __str__(self):
        return f'''\nFrom: {self.sender}\nTo: {self.recipient}\nSubject: {self.subject}\n\n{self.body}\n'''

    def __len__(self):
        return len(self.body)

    def __hash__(self):
        return hash(self.__str__())

    def __bool__(self):
        return bool(self.body)

    def __lt__(self, other):
        return datetime.strptime(self.date, '%Y-%m-%d') < datetime.strptime(other.date, '%Y-%m-%d')

    def __gt__(self, other):
        return datetime.strptime(self.date, '%Y-%m-%d') > datetime.strptime(other.date, '%Y-%m-%d')

    def __le__(self, other):
        return datetime.strptime(self.date, '%Y-%m-%d') <= datetime.strptime(other.date, '%Y-%m-%d')

    def __ge__(self, other):
        return datetime.strptime(self.date, '%Y-%m-%d') >= datetime.strptime(other.date, '%Y-%m-%d')

    def __eq__(self, other):
        return datetime.strptime(self.date, '%Y-%m-%d') == datetime.strptime(other.date, '%Y-%m-%d')

    def __ne__(self, other):
        return datetime.strptime(self.date, '%Y-%m-%d') != datetime.strptime(other.date, '%Y-%m-%d')


email1 = Email("john@example.com", "jane@example.com", "Meeting", "Hi Jane, let's have a meeting tomorrow.", "2022-05-10")
email2 = Email("jane@example.com", "john@example.com", "Re: Meeting", "Sure, let's meet at 2 PM.", "2022-05-10")
email3 = Email("alice@example.com", "bob@example.com", "Hello", "Hi Bob, how are you?", "2022-05-09")
print(email1)

print(len(email2))
print(hash(email3))
print(bool(email1))
print(email2 > email3)
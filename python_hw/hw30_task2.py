'''2. Создайте класс BankAccount для представления банковского счета.
Класс должен иметь атрибуты account_number (номер счета) и balance (баланс),
а также методы deposit() для внесения денег на счет и withdraw() для снятия денег со счета.
Затем создайте экземпляр класса BankAccount, внесите на счет некоторую сумму и снимите часть денег.
Выведите оставшийся баланс. Не забудьте предусмотреть вариант, при котором при снятии баланс может стать меньше нуля.
В этом случае уходить в минус не будем, вместо чего будем возвращать сообщение "Недостаточно средств на счете".'''

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('Сумма должна быть положительной')
        self.balance += amount
        return f'Внесено: {amount}. Текущий баланс: {self.balance}'

    def withdraw(self, amount):
        if amount > self.balance:
            return f'Вы пытаетесь снять {amount}. Недостаточно средств на счете. Текущий баланс: {self.balance}'
        elif amount <= 0:
            raise ValueError('Сумма должна быть положительной')
        else:
            self.balance -= amount
            return f'Снято: {amount}. Текущий баланс: {self.balance}'


account = BankAccount('327498238402', 1000)

print('Начальный баланс:', account.balance)
print(account.withdraw(1100))  # Проверка снятия суммы больше чем на балансе
print(account.deposit(500))
print(account.withdraw(1100))
print(account.withdraw(400))
print('Оставшийся баланс:', account.balance)
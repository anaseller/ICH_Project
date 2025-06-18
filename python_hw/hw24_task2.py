'''2. Напишите генератор, который будет генерировать арифметическую прогрессию'''

def ar_progression(a, d):
    while True:
        yield a
        a += d

x = ar_progression(3, 5)

for i in range(10):
    print(next(x))
# Даны два целых числа A и B (A < B). Найти сумму всех целых чисел от A до B
# включительно.

a = input("Введите первое число: ")
b = input("введите второе число больше первого: ")

while type(a) != int: # обработка исключений
    try:
        a = int(a)
    except ValueError:
        print("Неправильно ввели!")
        a = input("Введите первое число: ")


while type(b) != int: # обработка исключений
    try:
        b = int(b)
    except ValueError:
        print("Неправильно ввели!")
        b = input("Введите второе число: ")



s = 0
while a <= b:
    print(a)
    s += a
    a += 1
print(s)

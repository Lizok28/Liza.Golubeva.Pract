#Смоделировать простейший калькулятор,
# умеющий выполнять 4 основные арифметические операции.
a = input("Введите первое число: ")     #Обработка исключений
while type(a) != float:
    try:
        a = float(a)
        1 / a
    except ValueError and ZeroDivisionError:
        print("Неправильно ввели ")
        a = input("Введите первое число: ")


b = input("Введите второе число: ")      #Обработка исключений
while type(b) != float:
    try:
        b = float(b)
        1 / b
    except ValueError and ZeroDivisionError:
        print("Неправильно ввели")
        b = input("Введите второе число: ")


action = input("Выберите операцию: (+ - * /) : ")
if action == "+":
    print(a + b)
elif action == "-":
    print(a - b)
elif action == "*":
    print(a * b)
elif action == "/":
    if b != 0:
        print(a / b)
    else:
        print("Делить на ноль нельзя")
else:
    action = input("Некорректная операция. Выберите операцию: (+ - * /) : ")
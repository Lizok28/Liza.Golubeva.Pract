#Смоделировать простейший калькулятор,
# умеющий выполнять 4 основные арифметические операции.
a = input("Введите первое число: ")     #Обработка искоючений
while type(a) != float:
    try:
        a = float(a)
    except ValueError:
        print("Неправильно ввели ")
        a = input("Введите первое число: ")


b = input("Введите второе число: ")      #Обработка искоючений
while type(b) != float:
    try:
        b = float(b)
    except ValueError:
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
    print(a / b)
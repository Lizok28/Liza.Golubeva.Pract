# Составить функцию, которая выведет на экран строку, содержащую задаваемое с
# клавиатуры число символов


def Symbols(S):
    print("*" * S)


a = input("Введите целое число: ")
while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        print("Неправильно ввели")
        a = input("Введите целое  число: ")
Symbols(a)
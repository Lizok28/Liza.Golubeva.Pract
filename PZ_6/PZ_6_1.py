# # Даны целые числа N (>2), A и B. Сформировать и вывести целочисленный список
# # размера 10, первый элемент которого равен A, второй равен B, а каждый
# # последующий элемент равен сумме всех предыдущих.
# #

a = input("Введите целое число №1, которое будет > 2: ")
b = input("Введите целое число №2, которое будет > 2: ")

while type(a) != int:
    try:
        a = int(a)
        if a < 2:
            print("Число должно быть больше 2!!!")
            a = input("Введите целое число №1, которое будет > 2: ")
    except ValueError:
        print("Неправильно ввели")
        a = input("Введите целое число ")


while type(b) != int:
    try:
        b = int(b)
        if b < 2:
            print("Число должно быть больше 2!!!")
            b = input("Введите целое число №2, которое будет > 2: ")
    except ValueError:
        print("Неправильно ввели")
        b = input("Введите целое число")


List = [0] * 10
List[0] = a
List[1] = b
for i in range(2, 10):
        List[i] = sum(List[:i])

print(List)
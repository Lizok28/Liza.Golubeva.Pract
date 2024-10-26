# Дано целое число
# Если оно является отрицательным, то прибавить к нему 1, если положительное, то вычесть 2
# если нулевое, то заменить его на 10.
# вывести полученное число

a = input("Введите целое число: ")

while type(a) != int:   #обработка исключений
    try:
        a = int(a)
    except ValueError:
        print("Неправильно ввели!")
        a = input("Введите другое число: ")

if a < 0:     #Проверка условий и изменение числа
    a += 1
elif a > 0:
    a -= 2
else:
    a = 10
print("Полученное число: ", a)
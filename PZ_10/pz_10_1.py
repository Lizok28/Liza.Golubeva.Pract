

# Книжные магазины предлагают следующие коллекции книг.
# Магистр – Лермонтов, Достоевский, Пушкин, Тютчев
# ДомКниги – Толстой, Грибоедов, Чехов, Пушкин.
# БукМаркет – Пушкин, Достоевский, Маяковский.
# Галерея – Чехов, Тютчев, Пушкин.
# Определить в каких магазинах
# нельзя приобрести книги Грибоедова и Маяковского


magistr = {"Лермотов" ,"Достоевский", "Пушкин", "Тютчев"}
DomKnigi = {"Толстой", "Грибоедов", "Чехов", "Пущкин"}
BookMarket = {"Пушкин", "Достоевский", "Маяковский"}
Galery = {"Чехов", "Тютчев", "Пушкин"}
a = set()
for i in magistr:
    if "Грибоедов" in magistr or "Маяковский" in magistr:
        a.add("magistr")
for i in DomKnigi:
    if "Грибоедов" in DomKnigi or "Маяковский" in DomKnigi:
        a.add("DomKnigi")
for i in BookMarket:
    if "Грибоедов" in BookMarket or "Маяковский" in BookMarket:
        a.add("BookMarket")
for i in Galery:
    if "Грибоедов" in Galery or "Маяковский" in Galery:
        a.add("Galery")
print(a)
# #
# a = [4, 8, 10, 1, 16, 30, 20]
#
# t = 0
# for i in a:
#     if i % 4 == 0:
#         t = i - i
# print(t)

# lis = input()

# def Gosti(lis):
#     lis = lis.split()
#     if len(lis) == 0:
#         a = "никто не пришел"
#     elif len(lis) == 2:
#         a = f"{lis[0]} и {lis[1]}"
#     elif len(lis) >= 3:
#         a = f"{lis[0]}, {lis[1]} и {lis[2]}"
#     return a
#
# lis = input()
# dd = Gosti(lis)
# print(dd)

#
# def square_digits(number):
#     result = 0
#     multiplier = 1
#
#     while number > 0:
#         digit = number % 10
#         squared_digit = digit ** 2
#
#         # Обновляем multiplier в зависимости от длины squared_digit
#         if squared_digit < 10:
#             multiplier *= 10
#         else:
#             multiplier *= 100
#
#         result += squared_digit * multiplier
#         number //= 10
#
#     return result
#
# user_input = int(input("Введите число: "))
#
# # Вызов функции и вывод результата
# output = square_digits(user_input)
# print("Результат:", output)

# Ввод числа от пользователя
# number = int(input("Введите число: "))
#
# result = 0
# multiplier = 1
#
# # Обрабатываем каждую цифру числа
# while number > 0:
#     digit = number % 10  # Получаем последнюю цифру числа
#     squared_digit = digit ** 2  # Возводим цифру в квадрат
#
#     # Обновляем multiplier в зависимости от длины squared_digit
#     if squared_digit < 10:
#         multiplier *= 10
#     else:
#         multiplier *= 100
#
#     # Добавляем квадрат цифры к результату с учётом разряда
#     result += squared_digit * multiplier
#     number //= 10  # Убираем последнюю цифру из числа
#
# # Выводим результат
# print("Результат:", result)


# number = int(input("Введите число: "))  # Ввод числа
# result = 0  # Переменная для хранения результата
# place = 1  # Место для цифры (единицы, десятки и т.д.)
#
# while number > 0:
#     digit = number % 10  # Извлекаем последнюю цифру
#     squared_digit = digit * digit  # Возводим цифру в квадрат
#
#     # Добавляем к результату, учитывая место цифры
#     result += squared_digit * place
#     place *= 100  # Увеличиваем место на два порядка для двухзначного квадрата
#     number //= 10  # Убираем последнюю цифру из числа
#
# print(result)


#
# magistr = {"Лермотов", "Достоевский", "Пушкин", "Тютчев"}
# DomKnigi = {"Толстой", "Грибоедов", "Чехов", "Пущкин"}
# BookMarket = {"Пушкин", "Достоевский", "Маяковский"}
# Galery = {"Чехов", "Тютчев", "Пушкин"}
#
# # Множество для хранения уникальных названий магазинов
# unique_stores = set()
#
# # Проверяем каждый магазин
# if "Грибоедов" in magistr or "Маяковский" in magistr:
#     unique_stores.add("Магистр")
#
# if "Грибоедов" in DomKnigi or "Маяковский" in DomKnigi:
#     unique_stores.add("ДомКниги")
#
# if "Грибоедов" in BookMarket or "Маяковский" in BookMarket:
#     unique_stores.add("БукМаркет")
#
# if "Грибоедов" in Galery or "Маяковский" in Galery:
#     unique_stores.add("Галерея")
#
# # Преобразуем множество в список для вывода
# result = list(unique_stores)
# print("Магазины, где можно приобрести книги Грибоедова или Маяковского:", result)








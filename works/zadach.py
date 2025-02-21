from turtledemo.forest import doit1

from PIL.ImImagePlugin import split
from numpy.ma.core import product
from sympy import resultant

# strr = "Петров Иван Покс-29 5 4 3 2 5 4 4 5 4"
# student = {}
# strr = strr.split()
# student["Фамилия"] = strr[0]
# student["Имя"] = strr[1]
# student["Группа"] = strr[2]
#
# student["Оценки"] = []
#
# for i in strr[3: ]:
#     student["Оценки"].append(int(i))
#
# sra = sum(student["Оценки"]) / len(student["Оценки"])
#
# print(student)
# print(sra)


# Дана строка 'апельсины 45 991 63 100 12 яблоки 13 47 26 0 16',
# отражающая продажи продукции по дням в кг. Преобразовать информацию из
# строки в словари, с использованием функции найти максимальные продажи по
# каждому виду продукции, результаты вывести на экран.
# ss = "апельсины 45 991 63 100 12 яблоки 13 47 26 0 16"
#
# ss = ss.split()
#
# product = {}
# product["фрукт1"] = ss[0]
# product["ап_кг"] = []
#
# for i in ss[1:5]:
#     product["ап_кг"].append(int(i))
#
# product["фрукт2"] = ss[6]
# product["яб_кг"] = []
#
# for u in ss[7: ]:
#     product["яб_кг"].append(int(u))
#
# max_ap = max(product["ап_кг"])
#
# max_mm = max(product["яб_кг"])
#
# print(max_mm, max_ap)



# Организовать словарь на 10 англо-русских слов, обеспечивающий
# "перевод" английского слова на русский.

# ss = {"Hello": "Привет", "Summer": "Лето", "Money": "Деньги", "Box": "Коробка","Water": "Вода",}
# word = input()
# if word in ss:
#     print(ss[word])

# перемнржить все цифры в словаре
# dd = {1: 22, 2: 3}
# result = 1
# for i in dd:
#     result *= dd[i]
#
# print(result)

# создать словарь с ключами от 1 до 10 и их значениями возведенными в куб

# aa = {i: i ** 3 for i in range(1,11)}
# print(aa)

#
# keys = ['red', 'green', 'blue']
# values = ['#FF0000','#008000', '#0000FF']
# color_dictionary = dict(zip(keys, values))
# print(color_dictionary)

#
# num = input()
# # list(num)
# num = str(num)
# sp = list(num)
#
#
# bb = 0
# for i in sp:
#     bb = int(i) ** 2
# #
# bb = str(bb)
# ff = list(bb)
#
# # gg = []
# for i in num:
#
# gg = ff + ff
#
# # num = bb.append
# print(gg)
# bb = 0


# num = num.split()
# for i in num[0: -1]:
#     bb = int(i) ** 2
# # num += bb.append
# print(bb)

# a1 = int(input())
# a2 = int(input())
# a3 = int(input())
# if a2 == a1 + 1:
#     if a3 == a2 + 1:
#         print("YES")
# else:
#     print('NO')

# a1 = int(input())
# a2 = int(input())
# a3 = int(input())
# a4 = int(input())
#
# d = [a1, a2, a3, a4]
#
# v = min(d)
# print(v)

# a1 = int(input())
# a2 = int(input())
# a3 = int(input())
# d = [a1, a2, a3]
# f = 0
# for i in d:
#     if i > 0:
#         f += i
# print(f)

# def draw_triangle():
#     i = 0
#     m = 0
#     while i < 10:
#         for d in range(10):
#             m = "*" * i
#             i += 1
#             print(m)
#
#
# # основная программа
# draw_triangle()


# m = int(input())
# n = int(input())
# if m < n:
#     for i in range(m, n + 1):
#         print(i)
# else:
#     for i in range(m, n - 1, -1):
#         print(i)

# m = int(input())
# n = int(input())
# for i in range(m, n):
#     if i % 2 != 0:
#         print(i)

# n = int(input())
# m = int(input())
# for i in range(n, m):
#     if i % 2 != 0:
#         print(i)


# n = int(input())
# m = int(input())
#
# if n < m:
#     for i in range(n, m + 1):
#         if i % 2 != 0:
#                 print(i)
# else:
#      for i in range(n, m - 1, -1):
#         if i % 2 != 0:
#                 print(i)

# m = int(input())
# n = int(input())
# for i in range(m, n):
#     if i % 17 == 0 or i % 10 == 9 or i % 5 == 0 and i % 3 == 0:
#         print(i)


# a = int(input())
# d = 0
# for i in range(1, 11):
#     d = a * i
#     print(a, "x", i, "=", d)

# total = 0
# for i in range(1, 6):
#     total += i
#     print(total, end='')

# a = int(input())
# b = int(input())
# m = 0
# for i in range(a, b + 1):
#     if i ** 3 % 4 and i ** 3 % 9:
#         m += 1
# print(m)

# n = int(input())
# sm = 0
# for i in range(1, n + 1):
#     if i ** 2 % 10 == 2 or i ** 2 % 10 == 5 or i ** 2 % 10 == 8:
#         sm += i
# # if sm == 0:
# #     print(0)
# print(sm)

# y = 1
# for i in range(10):
#     a = int(input())
#     if i > 0:
#         y *= i
# print(y)

# n = int(input())
# sm = 0
# for i in range(1, n + 1):
#     if i % 2 == 0:
#         sm +=
#     if i % 2 != 0:
#         sm -= 1
# print(sm)



# n = int(input())
# for i in range(n):
#     ss = int(input())
# o = 0
# for i in range(ss):
#     if i < 2:
#         o += i
#     if i > o:
#         o += i
# print(o)
#


# users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
#          {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
#          {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
#          {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
#          {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
#          {'name': 'John', 'phone': '233-421-32', 'email': ''},
#          {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
#          {'name': 'Alina', 'phone': '+7948-799-2434', 'email': 'ali.ch.b@gmail.com'},
#          {'name': 'Robert', 'phone': '420-2011', 'email': ''},
#          {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
#          {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
#          {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
#          {'name': 'Roman', 'phone': '+7459-145-8059', 'email': 'roma988@mail.ru'},
#          {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
#          {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
#          {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]
#
#
# s = []
# for i in users:
#     if i["phone"].endswith("8"):
#         s.append(i ["name"])
#
#
# print(" ".join(s))


# users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
#          {'name': 'Helga', 'phone': '555-1618'},
#          {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
#          {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
#          {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
#          {'name': 'John', 'phone': '233-421-32', 'email': ''},
#          {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
#          {'name': 'Alina', 'phone': '+7948-799-2434'},
#          {'name': 'Robert', 'phone': '420-2011', 'email': ''},
#          {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
#          {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
#          {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
#          {'name': 'Roman', 'phone': '+7459-145-8059'},
#          {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
#          {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
#          {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]
#
# s = []
# for i in users:
#     if 'email' not in i or i['email'] == '':
#         s.append(i["name"])
#     # if "" in 'email':
#     #     s.append(i["name"])
# d = sorted(s)
# print(" ".join(d))


# def ff():
#     s = int(input())
#     total = 0
#     # s = int(input())
#     while s > 0:
#         total += s % 10
#         s = s // 10
#     print(total)


# def ff(num):
#     sum = 0
#     while num > 0:
#         dig = num % 10
#         sum += dig
#         num = num // 10
#     print(sum)
#
# num = int(input())
# ff(num)



a = input()

my_dict = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}
s = []
for i in a:
    s.append(my_dict[i])
print(" ".join(s))
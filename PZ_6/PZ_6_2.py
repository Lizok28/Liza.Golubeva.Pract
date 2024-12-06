# Дан список размера N. Найти максимальный из его локальных минимумов
# (локальный минимум — это элемент, который меньше любого из своих соседей).


import random


spisok = []


n = input("Введите размер списка: ")

while type(n) != int:             # Обработка исключений
    try:
        n = int(n)
        if n < 1:
            print("Размер списка должен быть больше 1")
            n = input("Введите размер списка > 1: ")
    except ValueError:
        print("Неправильно ввели!")
        n = input("Введите размер списка: ")


for f in range(n):
    spisok += [random.randint(1, 100)]


print("Изначальный список:", spisok)


lokal_minimumy = []


# Проверяем первый элемент
if n > 1 and spisok[0] < spisok[1]:
    lokal_minimumy.append(spisok[0])


# Проверяем локальные минимумы для элементов с 1 по n-2
for i in range(1, n - 1):
    if spisok[i] < spisok[i - 1] and spisok[i] < spisok[i + 1]:
        lokal_minimumy.append(spisok[i])


# Проверяем последний элемент
if n > 1 and spisok[n - 1] < spisok[n - 2]:
    lokal_minimumy.append(spisok[n - 1])


print("Локальные минимумы:", lokal_minimumy)


# Выводим максимальный из локальных минимумов, если они есть
if lokal_minimumy:
    max_lokal_min = max(lokal_minimumy)
    print("Максимальный из локальных минимумов:", max_lokal_min)
else:
    print("Локальных минимумов нет.")


# Дан список размера N. Найти максимальный из его локальных минимумов
# (локальный минимум — это элемент, который меньше любого из своих соседей).


import random

spisok = []


n = input("Введите размер списка: ")

while type(n) != int:             #Обработка исключений
    try:
        n = int(n)
        if n < 1:
            print("Размер списка должет быть больше 1")
            n = input("Введите размер списка > 1: ")
    except ValueError:
        print("Неправильно ввели!")
        n = input("Введите размер списка: ")


for f in range(n):
    spisok += [random.randint(1, 100)]

print("Изначальный список:", spisok)


lokal_minimumy = []
for i in range(1, n - 1):
    if spisok[i] < spisok[i - 1] and spisok[i] < spisok[i + 1]:
        lokal_minimumy.append(spisok[i])


print("Локальные минимумы:", lokal_minimumy)

# Вывод максимального из локальных минимумов, если они есть
if lokal_minimumy:
    max_lokal_min = max(lokal_minimumy)
    print("Максимальный из локальных минимумов:", max_lokal_min)
else:
    print("Локальных минимумов нет.")


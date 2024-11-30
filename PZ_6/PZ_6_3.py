# Дан список размера N и целое число K (1 < K < N). Осуществить сдвиг элементов
# список вправо на K позиций (при этом A1 перейдет в AK+1, A2 — в AK+2, ..AN-K — в
# AN, а исходное значение K последних элементов будет потеряно). Первые K
# элементов полученного списка положить равными 0.


import random

Spisok = []

n = input("Введите размер списка: ") # размер списка (например)

while type(n) != int:
    try:
        n = int(n)
    except ValueError:
        print("Неправильно ввели!")
        n = input("Введите размер списка: ")


k = input("Введите на сколько вы хотите сдвинуть элементы (1 < k < n) : ")   # количество сдвигов

while type(k) != int:
    try:
        k = int(k)
        if k <= 1 or k >= n:
            print("Ошибка: K должно быть в пределах (1 < k < n)")
            k = input("Введите на сколько вы хотите сдвинуть элементы 1 < k < n : ")
    except ValueError:
        print("Неправильно ввели!")
        k = input("Введите на сколько вы хотите сдвинуть элементы: ")


for u in range(n):
    Spisok += [random.randint(1, 100)]

print("Изначальный список", Spisok)


# Сдвиг вправо на K позиций
for i in range(n - k - 1, -1, -1):
    Spisok[i + k] = Spisok[i]

# Заполнение первых K элементов нулями
for i in range(k):
    Spisok[i] = 0

# Вывод результата
print("Список после сдвига:", Spisok)





# Книжные магазины предлагают следующие коллекции книг.
# Магистр – Лермонтов, Достоевский, Пушкин, Тютчев
# ДомКниги – Толстой, Грибоедов, Чехов, Пушкин.
# БукМаркет – Пушкин, Достоевский, Маяковский.
# Галерея – Чехов, Тютчев, Пушкин.
# Определить в каких магазинах
# можно приобрести книги Грибоедова и Маяковского


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








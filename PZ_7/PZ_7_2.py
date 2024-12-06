# Дана строка-предложение на русском языке.
# Зашифровать ее, выполнив циклическую замену каждой буквы на следующую за ней в алфавите и сохранив при этом регистр букв («А» перейдет в «Б», «а» — в «б», «Б» — в «В», «я» — в «а» и т. д.).
# Букву «ё» в алфавите не учитывать («е» должна переходить в «ж»). Знаки препинания и пробелы не изменять.



input_string = input("Введите строку для шифрования: ")
output_string = ""

for char in input_string:
    if char.islower():  # для строчных букв
        if char == 'я':
            output_string += 'а'
        else:
            output_string += chr(ord(char) + 1)
    elif char.isupper() :  # для заглавных букв
        if char == 'Я':
            output_string += 'А'
        else:
            output_string += chr(ord(char) + 1)
    else:
        output_string += char  # тут мы сохранили все остальные знаки

print("Исходное предложение:", input_string)
print("Зашифрованное предложение:", output_string)

# Дан символ C, изображающий цифру или букву (латинскую или русскую).
# Если C изображает цифру, то вывести строку «digit»,
# если латинскую букву — вывести строку «lat», если русскую — вывести строку «rus».



while True:

    C = input("Введите символ: ")

        # Проверяем, что введён только один символ
    if len(C) != 1:
        print("Пожалуйста, введите только один символ.")
        continue

    if C.isdigit():
        print("digit")
        break
    elif C.isalpha():
        if C.isascii():
            print("lat")
        else:
            print("rus")
        break
    else:
        print("Неизвестный символ.")
        continue




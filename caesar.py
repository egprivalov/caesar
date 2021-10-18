# Алфавиты
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # Латинский алфавит заглавных букв
alphabet = "abcdefghijklmnopqrstuvwxyz"  # Латинский алфавит строчных букв
ALFAVIT = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"  # Русский алфавит заглавных букв
alfavit = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"  # Русский алфавит строчных букв

check = False  # Переменная проверки корректности ввода
# Проверка корректности данных ввода
while not check:
    try:
        check = True
        chse = int(input("Введите 1 для шифрования шифром Цезаря или 2 для дешифровки: "))-1  # Переменная выбора режима (шифрования/дешифрования)
    except ValueError:
        check = False
        print("Некорректный ввод\nПопробуйте снова")

print("Программа поддерживает Русский и Английский алфавит. При вводе на других языках строка выведется без изменений.")
str_in=input("Введите строку для шифрования: ") if not chse else input("Введите строку для дешифрования: ")  # Строчка ввода
str_out=""  # Строчка вывода

check = False  # Переменная проверки корректности ввода
# Проверка корректности данных ввода
while not check:
    try:
        check = True
        sdvig=abs(int(input("Введите сдвиг: ")))
    except ValueError:
        check = False
        print("Некорректный ввод\nПопробуйте снова")

sdvig=sdvig if not chse else -1*sdvig+1

for i in str_in:
    if (i >= "A") and (i <= "Z"):  # Проверка на принадлежность заглавным латинским буквам
        sdvig = sdvig % 26
        str_out += ALPHABET[(ALPHABET.find(i)+sdvig) % 26]
    elif (i >= "А") and (i <= "Я") or i == "Ё":  # Проверка на принадлежность заглавным русским буквам
        sdvig = sdvig % 33
        str_out += ALFAVIT[(ALFAVIT.find(i)+sdvig) % 33]
    elif i>="a" and i<="z":  # Проверка на принадлежность строчным латинским буквам
        sdvig=sdvig % 26
        str_out+=alphabet[(alphabet.find(i)+sdvig) % 26]
    elif i>="а" and i<="я" or i=="ё":  # Проверка на принадлежность строчным русским буквам
        sdvig=sdvig % 33
        str_out += alfavit[(alfavit.find(i)+sdvig) % 33]
    else:  # Символы, не лежащие ни в одном алфавите
        str_out+=i

print("Зашифрованная строка: "+str_out)
